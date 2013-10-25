Logo
####
:date: 2007-10-19 17:30
:author: Ian Bicking
:tags: Programming

So `Logo is 40 years old <http://blog.wired.com/wiredscience/2007/10/forward-40-wher.html>`_. I'll take this as an opportunity to talk about Logo-the-language (as opposed to Logo-the-graphics or Logo-the-educational-experience).  It's a much better language than most people appreciate.

Logo is Lisp.  It's an old Lisp but it's very Lisp.  Let's look at a classic example::

  TO square :size
    REPEAT 4 [FD :size RT 90]
  END

This translates to something like this (in Scheme)::

  (define (square size)
    (repeat 4 (lambda () 
               (begin (fd size) 
                      (rt 90)))))

Well, technically it translates to this::

  (define (square size)
    (repeat 4 '(fd size rt 90)))

That is, ``[...]`` is a quoted list; nothing inside it is evaluated. This is actually a lot like Tcl::

  proc square {size} {
    repeat 4 {
      fd $size 
      rt 90
    }
  }

In Tcl ``{...}`` is just a string literal, but one without substitution, and where you can nest your braces.  It's a lot like a quoted list in Lisp, except where lists are the fundamental type in Lisp, strings are the fundamental type in Tcl.

To get an idea of how this works, here's the implementation of ``repeat`` in these different languages::

  TO repeat :count :block
    IF :count > 0 [EVAL :block 
                   REPEAT (:count - 1) :block]
  END

  (define (repeat count block)
    (if (> count 0) 
        (begin (block) (repeat (- count 1) block))))

  proc repeat {count block} {
    while {$count > 0} {
        uplevel 1 $block
        set count [expr {$count - 1}]
    }
  }

Tcl doesn't really encourage recursion, and it's only partially encouraged in Logo -- some implementations implement `tail call optimization <http://en.wikipedia.org/wiki/Tail_recursion>`_, but not all of them.

Scoping is an interesting difference here.  In Scheme the scoping is lexical, which is the norm in modern languages.  That is, any variables you refer to in a ``lambda`` (like ``size`` in the example) are bound according to where in the source you define that anonymous function.  In Tcl the ``uplevel`` statement says to evaluate the block in the calling scope.  In Logo it's all implicit because Logo is `dynamically scoped <http://en.wikipedia.org/wiki/Scope_%28programming%29#Dynamic_scoping>`_. That is, each function call inherits all the variables from the calling function.  So you can write something like this::

    TO house :size
      square
      FD :size
      RT 60
      triangle
    END

    TO square
      REPEAT 4 [FD :size RT 90]
    END

    TO triangle
      REPEAT 3 [FD :size RT 120]
    END

Here ``:size`` is inherited in called functions.  You can write some really bad code using dynamic scoping, with lots of magic side effects, but Logo isn't meant for writing large programs so it usually doesn't come up.  A nice side effect of dynamic scoping is that EVAL works pretty well.

Another interesting aspect of Logo (and Tcl) is that it has *very* few special forms.  In one of Logo's more `pure implementations <http://www.cs.berkeley.edu/~bh/logo.html>`_ the only special form is ``TO``, and even that wouldn't *have* to be a special form (there's a function ``DEFINE`` that does the same thing).  For instance, here's how you set a variable::

    MAKE "variable <value>

That is, you call the function ``MAKE``, give it a variable *name*, and then a value.  Some dialects allow ``MAKE :variable <value>``, but some like UCBLogo actually interpret that to mean: set the variable *named by* ``:variable``.

Another interesting aspect of Logo is how it handles parenthesis. You'll notice there aren't many.  Lisp is known (and oft criticized) for its parenthesis.  Logo shows they aren't strictly required; it
does this by using the `arity of functions <http://en.wikipedia.org/wiki/Arity>`_ to inform parsing.  An example::

    SETXY ABS :x :y

The equivalent Scheme:

    (setxy (abs x) y)

If you *know* that ``SETXY`` takes two arguments, and that ``ABS`` takes one argument, you can figure out how to parse the Logo. Comparing it to `Forth <http://en.wikipedia.org/wiki/Forth_%28programming_language%29>`_ is kind of interesting::

    y @ x @ abs setyx

Reverse the order, replace ``@`` with ``:``, and you have Logo.   ``@`` and ``:`` also share a lot in common: ``:variable`` in Logo is syntactic sugar for ``THING "variable`` (symbols in Logo are spelled ``"symbol``, like ``'symbol`` in Scheme, ``#symbol`` in Smalltalk, or ``:symbol`` in Ruby).  ``THING "variable`` tells Logo to look up the value associated with the given symbol.  Similarly in Forth, ``y`` refers to an address, and ``@`` says to lookup the value at that address.

But back to parsing - Forth is based on trust and foreknowledge.  You *know* that ``abs`` pops one thing from the stack, and ``setyx`` pops two things from the stack.  You trust those words to act that way, because there's nothing stopping them from popping more or less from the stack than they claim.  Logo isn't quite as trusting, but it does see that ``SETXY`` takes two values, and grabs two values.  In the same way in the first example, when it sees ``[FD :size RT 90]``, it can tell that it's two commands -- newlines aren't required.

One awkward part of this lack of parenthesis is that without knowing what functions you are referring to the expressions can't be trully parsed.  As a result most Logos are really interpreters.  If anyone cared enough of course you could optimize this considerably, and maybe some of the more performant Logos like `StarLogo <http://education.mit.edu/starlogo />`_ or `NetLogo <http://ccl.northwestern.edu/netlogo />`_ do, but I don't really know.  `PyLogo <http://svn.colorstudy.com/PyLogo />`_ is pretty naive about it, and it's not that fast as a result (but not terrible).

And of course I should take a chance to plug `PyLogo`_, which runs Logo from Python, and lets Logo code easily call Python, and vice versa.  Just ``easy_install PyLogo`` and you can run ``pylogo --console`` to amuse yourself with the language (the `docs from UCBLogo <http://svn.colorstudy.com/PyLogo/trunk/docs/UCBManual.txt>`_ might be helpful, and ``PROCEDURES`` shows all the functions, while ``HELP "IFELSE`` will show the help for a particular command.  

Another related language is `Rebol <http://www.rebol.com />`_, which is very close to Logo without the turtles (though with a bunch of new literals and object-oriented features as well).  Many things *called* Logo are just `turtle graphics <http://en.wikipedia.org/wiki/Logo_%28programming_language%29#Turtle_geometry_and_programming>`_ with an extremely poor "language" bolted on in front.  Don't be fooled!  On the web `Turtle Tracks <http://turtletracks.sourceforge.net/applet2.html>`_ is one of the more true implementations (though I can't get graphics, hm).
