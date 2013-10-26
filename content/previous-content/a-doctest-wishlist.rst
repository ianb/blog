A Doctest Wishlist
##################
:date: 2008-07-31 22:11
:author: Ian Bicking
:tags: Python

Lately I've been doing most of my testing with `doctest <http://python.org/doc/current/lib/module-doctest.html>`_, primarily using `stand-alone text files <http://python.org/doc/current/lib/doctest-simple-testfile.html>`_.  I generally like it (otherwise I wouldn't be using it), but it does make me frustrated with doctest sometimes.  On my wishlist (roughly in order):

* I wish output was always displayed, even when there's an exception.  I see no reason for the current behavior.  Really exceptions could be treated like any other output (if ELLIPSIS was on by default).

* I wish you could turn on options like ELLIPSIS from within a doctest, for all expressions.  (``# doctest: +ELLIPSIS`` on every line is beyond ugly.)

* ``<BLANKLINE>`` is terribly ugly.

* There's no way of saying "I don't care what this prints".  You can't do::

    >>> some_function()
    ...

  because the ``...`` is treated like a continuation.

* Plugging in an alternate output checker is kind of tedious, and can't be done from within a doctest (without horrible hacks).

* I'd like to be able to easily jump into an interactive state from doctest.  Maybe `pdb <http://python.org/doc/current/lib/module-pdb.html>`_ can do this, but I've never figured that out exactly.

* Getting `nose <http://code.google.com/p/python-nose />`_ to run ``.txt`` files as doctests is really hard, involving a combination of options I always forget.

* There's no way to abort the doctest.  Sometimes I'd like to run some environment checks early on, and be able to stop the test if they fail.

* I wish it was easier to apply to non-Python code.  (I've adapted it via subclassing `for Logo <http://pylogo.org />`_ but I wouldn't do that often.)

* I wish I could copy and paste from doctests to consoles.  But I don't see any solution to this problem.

* The `integration <http://python.org/doc/current/lib/doctest-unittest-api.html>`_ with `unittest <http://python.org/doc/current/lib/module-unittest.html>`_ is pretty hacky.  Not that I've used unittest in years.  But some other test frameworks build off this integration.

* ``python -m doctest sometest.txt`` doesn't do what it should do.  Instead it runs doctest's self-tests.
