Opening Python Classes
######################
:date: 2007-08-08 14:03
:author: Ian Bicking
:tags: Programming, Python

So, I was reading through comments to despam my old posts before archiving them, and came upon `this old reply <http://dan.chokola.com/journal/?user=dan&entry=2007-01-27.105426>`_ to `this old post of mine <http://blog.ianbicking.org/re-ruby-and-python-compared.html>`_ which was a reply to `this much older post <http://web.archive.org/web/20070329162213/http://www.rexx.com/~oinkoink/Ruby_v_Python.html>`_.

I won't reply to that post much, because it's mostly... well, not useful to respond to.  But people often talk about the wonders of Open Classes in Ruby.  For Python people who aren't familiar with what that means, you can do::

    # Somehow acquire SomeClassThatAlreadyExists
    class SomeClassThatAlreadyExists
        def some_method(blahblahblah)
            stuff
        end
    end

And ``SomeClassThatAlreadyExists`` has a ``some_method`` added to it (or if that method already exists, then the method is replaced with the new implementation).

In Python when you do this, you've defined an entirely new class that just happens to have the name ``SomeClassThatAlreadyExists``.  It doesn't actually effect the original class, and probably will leave you confused because of the two very different classes with the same name.  In Ruby when you define a class that already exists, you are extending the class in-place.

You can change Python classes in-place, but there's no special syntax for it, so people either think you can't do it, or don't realize that you are doing the same thing as in Ruby but without the syntactic help.  I guess this will be easier with `class decorators <http://www.python.org/dev/peps/pep-3129 />`_, but some time ago I also wrote a recipe using normal decorators that looks like this::

    @magic_set(SomeClassThatAlreadyExists)
    def some_method(self, blahblahblah):
        stuff

The only thing that is even slightly magic about the setting is that I look at the first argument of the function to determine if you are adding an instance, class, or static method to an object, and let you add it to classes or instances.  It's really not that magic, even if it is called `magicset <http://svn.colorstudy.com/home/ianb/recipes/magicset.py>`_.

I think with class decorators you could do this::

    @extend(SomeClassThatAlreadyExists)
    class SomeClassThatAlreadyExists:
        def some_method(self, blahblahblah):
            stuff

Implemented like this::

    def extend(class_to_extend):
        def decorator(extending_class):
            class_to_extend.__dict__.update(extending_class.__dict__)
            return class_to_extend
        return decorator
