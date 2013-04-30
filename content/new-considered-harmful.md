Title: "new" Considered Harmful
Slug: new-considered-harmful
Category: javascript
Date: 2013-04-29

Javascript objects and classes aren't hard.  This whole "prototype" thing is blamed for too much: prototype-based programming isn't hard. `this` is really weird, but prototypes aren't.

What's prototype-based programming?  It just means every object has a "prototype" and when you look up a property on the object it searches the object, then the object's prototype, then the prototype's prototype, and so on.  It's exactly like classes except there's no special distinction between "instance" and "class".  You don't have to change paradigms to understand prototypes, you don't have to drink any Kool Aid to accept the idea.  Don't overthink it, it's fine.

The problem with Javascript isn't prototypes, it's the `new` operator. The `new` operator is terrible in all ways.  But to explain why it is bad, I want to start with the *right* way to think about prototypes: [Object.create()](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Object/create).

`Object.create` is newer than `new` and [support isn't universal](http://kangax.github.io/es5-compat-table/#Object.create) (though there's a [polyfill](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Object/create#Polyfill)), but it's much simpler.

`Object.create(obj)` creates a new object, with `obj` as the new object's prototype.  (There's a [second argument](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Object/create#Using_<propertiesObject>_argument_with_Object.create) that does fancy things, but let's ignore that part.)  That's really all you need to know, and you should probably be able to understand it.  As an example, [this tutorial by Yehuda Katz](http://yehudakatz.com/2011/08/12/understanding-prototypes-in-javascript/) uses it as the basis for explaining Javascript objects in general.

We can describe `new` in terms of `Object.create()`:

```javascript
function new_(constructor /* plus a variable number of arguments */) {
  var newObject = Object.create(constructor.prototype);
  // This gets the varargs after `constructor`:
  var restArgs = Array.prototype.slice.call(arguments, 1);
  var result = constructor.apply(newObject, restArgs);
  if (typeof result == "object") {
    // If the function returns something, ignore newObject
    return result;
  }
  return newObject;
}
```

Using this, `new Constructor(1, 2)` is equivalent to `new_(Constructor, 1, 2)`

This *might* seem reasonable, but it has a few problems:

### There's nothing to distinguish constructor functions from normal functions

So there's nothing to keep you from calling `Constructor(1, 2)` -- but the results will be bad.  If you've used Javascript much you've probably made this mistake, and added global variables as a result.

If you are not familiar with it, it works like this:

```javascript
function Constructor(a, b) {
  this.a = a;
  this.b = b;
}
var obj = Constructor(1, 2);
// Now there is a global object a==1, b==2
// because "this" was bound to the window
// obj is undefined because Constructor didn't return a value
```

### It's not actually that easy to detect when `new` was left off.

You can check if `this === window`, but that doesn't work in Node.js (you'd have to check `this === module`).  The best way is generally:

```javascript
function Foo() {
  if (! this instanceof Foo) {
    return new Foo();
  }
}
```

But then it's not clear if `new` should be used at all, you may very well need to understand [named function expressions](http://kangax.github.io/nfe/), and passing arbitrary arguments along [is hard](http://ejohn.org/blog/simple-class-instantiation/)).

### There's two ways to define the prototype: awkard or inflexible

The more common way to define the prototype is like this:

```javascript
function Foo() {
}
Foo.prototype.method = function () {
};
```

This gets kind of tedious, and you repeat the class name over and over.  A shorthand is helpful:

```javascript
function Foo() {
}
Foo.prototype = {
  method: function () {
  }
};
```

But that makes it hard to do subclassing, because you are *overwriting* the prototype.  This keeps you from overriding just the methods you care to in the subclass.  Which leads us to...

### Clean subclassing is hard to impossible because of the constructor

So here's how you are supposed to create a class `Bar` that subclasses `Foo`:

```javascript
function Bar() {
}
Bar.prototype = new Foo();
```

Now you can add methods.  But can you create a new `Foo` object so easily?  Usually the constructor will have arguments, maybe even side effects, creating peculiar artifacts in your prototype.

(Of course you could do `Bar.prototype = Object.create(Foo.prototype)` -- and you probably should -- but once you use `Object.create()` there's no reason to go back to `new`.)

## Prototypes are still okay

Given the problems with `new` some people resort to wildly different means of creating object.  For instance, the explicit method:

```javascript
function Point(x, y) {
  return {
    x: x,
    y: y,
    add: function (other) {
      return Point(this.x + other.x, this.y + other.y);
    }
  };
}
```

Or you can avoid `this` entirely:

```javascript
function Point(x, y) {
  return {
    getX: function () {
      return x;
    },
    getY: function () {
      return y;
    },
    add: function (other) {
      return Point(x + other.getX(), y + other.getY());
    }
  };
}
```

There's a wealth of quirky ways to use objects, ad hoc methods, closures, factory functions, and other techniques to create something class-like.  But prototypes don't need all that fixing!  These techniques add memory overhead, sometimes performance overhead, and make it harder for other people to read your code.  Prototypes don't need fixing.

## A modest proposal for classes

Lots of libraries include shortcuts for classes.  But they often add other features that get in the way of just replacing `new`.  I will offer my own class constructor, which in my opinion does exactly what it needs to do and nothing more:

```javascript
function Class(superclass, properties) {
  var prototype;
  if (! properties) {
    // We're creating an object with no superclass
    prototype = superclass;
  } else {
    prototype = Object.create(superclass.prototype);
    for (var a in properties) {
      if (properties.hasOwnProperty(a) {
        prototype[a] = properties[a];
      }
    }
  }
  var ClassObject = function () {
    var newObject = Object.create(prototype);
    if (newObject.constructor) {
      newObject.constructor.apply(newObject, arguments);
    }
    return newObject;
  };
  ClassObject.prototype = prototype;
  return ClassObject;
}

// Use like:
var Point = Class({
  constructor: function (x, y) {
    this.x = x;
    this.y = y;
  },
  add: function (other) {
    return Point(this.x+other.x, this.y+other.y);
  }
});
```

This doesn't have a special way to call the superclass.  Instead you just have to be explicit, for instance you might do:

```javascript
var Subclass = Class(Superclass, {
  method: function (a, b) {
    a = Math.abs(a);
    return Superclass.prototype.call(this, a, b);
  }
});
```

It's a little tedious to write out `Superclass.prototype.call(...)`, but in my experience these superclass calls don't happen that often, and trying to be clever is worse than the little bit of extra typing required.

I've chosen the name `constructor` for the constructor method because it's the one name [already used by Javascript](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Object/constructor). I prefer this over `init` or `__init__` or something else adopted from another language.

## ES6 will save us all, sometime far in the future

ES6 (EcmaScript 6, the version of Javascript currently in development) has a [class statement](http://people.mozilla.org/~jorendorff/es6-draft.html#sec-13.5) ([this is probably more readable](http://wiki.ecmascript.org/doku.php?id=strawman:maximally_minimal_classes)). Unlike some previous proposed versions of Javascript, and some previous proposed class statements, this one seems like it will actually stick.  That will resolve most of the problems with our current vague patterns (though it's unclear to me how it affects `new`).

But let's be honest: most of us will not be able to use this for quite some time (though who knows, with [source maps](http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/) we might be able to compile down to older versions of Javascript without much loss in debuggability).  So until then we must manually apply sanity when we write Javascript.
