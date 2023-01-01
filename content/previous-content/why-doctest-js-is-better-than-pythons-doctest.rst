Why doctest.js is better than Python's doctest
##############################################
:date: 2012-10-02 21:26
:author: Admin
:tags: Javascript, Mozilla, Programming, Python

I've been trying, not too successfully I'm afraid, to get more people to use `doctest.js <http://doctestjs.org>`_.  There's probably a few reasons people don't.  They are all wrong!  Doctest.js is the best!

One issue in particular is that people (especially people in my Python-biased circles) are perhaps thrown off by Python's doctest.  I think Python's doctest is pretty nice, I enjoy testing with it, but there's no question that it has a lot of problems.  I've even thought about trying to fix doctest, and even made a repository, but I only really got as far as `creating a list of issues I'd like to fix <https://github.com/ianb/doctest2/issues?direction=desc&sort=created&state=open>`_. But, like so many before me, I never actually *made* those fixes. Doctest has, in its life, only really had a single period of improvement (in the time leading to Python 2.4).  That's not a recipe for success.

Of course doctest.js takes inspiration from Python's doctest, but I wrote it as a real test environment, not for a minimal use case.  In the process I fixed a bunch of issues with doctest, and in places Javascript has also provided helpful usability.

Some issues:

Doctest.js output is predictable
--------------------------------

The classic pitfall of Python's doctest is printing a dictionary::

    >>> print {"one": 1, "two": 2}
    {'two': 2, 'one': 1}

The print order of a dictionary is arbitrary, based on a hash algorithm that can change, or mix things up as items are added or removed.  And to make it worse, the output *usually* stable, such that you can write tests that unexpectibly fragile.  But there's no reason why ``dict.__repr__`` *must* use an arbitrary order.  Personally I take it as a bit of unfortunate laziness.

If doctest had used ``pprint`` for all of its printing it would have helped some.  But not enough, because this kind of code is fairly common::

    def __repr__(self):
        return '<ThisClass attr=%r>' % self.attr

and that ``%r`` invokes a ``repr()`` that cannot be overridden.

In doctest.js I always try to make output predictable.  One reason this is fairly easy is that there's nothing like ``repr()`` in Javascript, so doctest.js has its own implementation.  It's like I started with pprint and no other notion existed.

Good matching
-------------

In addition to unpredictable output, there's also just hard-to-match output.  Output might contain blank lines, for instance, and Python's doctest requires a very ugly ``<BLANKLINE>`` token to handle that. Whitespace might not be normalized.  Maybe there's boring output. Maybe there's just a volatile item like a timestamp.

Doctest.js includes, by default, ellipsis: ``...`` matches any length of text.  But it also includes another wildcard, ``?``, which matches just one number or word.  This avoids cases when the use of ``...`` swallows up too much when you just wanted to get a single word.

Also doctest.js doesn't use ``...`` for other purposes.  In Python's doctest ``...``` is used for continuation lines, meaning you can't just ignore output, like::

    >>> print who_knows_what_this_returns()
    ...

Or even worse, you can't ignore the beginning of an item::

    >>> print some_request
    ...
    X-Some-Header: foo
    ...

The way I prefer to use doctest.js it doesn't have *any* continuation line symbol (but if there is one, it's ``>``).

Also doctest.js normalizes whitespace, normalizes ``"`` and ``'``, and just generally tries to be *reasonable*.

Doctest.js tests are plain Javascript
-------------------------------------

Not many editors know how to syntax highlight and check doctests, with their ``>>>`` in front of each line and so forth.  And the whole thing is tweaky, you need to use a continuation (``...``) on some lines, and start statements with ``>>>``.  It's an awkward way to compose.

Doctest.js started out with the same notion, though with different symbols (``$`` and ``>``).  But recently with the rise of a number of excellent parsers (I used `Esprima <http://esprima.org />`_) I've moved my own tests to another pattern::

    print(something())
    // => expected output

This is already a fairly common way to write examples.  Like how you may have read pre-Python pseudocode and thought: *that looks like Python!*: doctest.js looks like example pseudocode.

Doctest.js tests are self-describing
------------------------------------

Python's doctest has some options, some *important* options that effect the semantics of the test, that you can only turn on in the runner.  The most important option is ELLIPSIS.  Either your test was written to use ELLIPSIS or it wasn't - that a test can't self-describe its requirements means that test running is fragile.

I made `the hackiest package ever <http://pypi.python.org/pypi/dtopt>`_ to get around this in Python, but it's hacky and lame.

Exception handling isn't special
--------------------------------

Python's doctest treats exceptions differently from other output.  So if you print something before the exception, it is thrown away, never to be seen.  And you can't use some of the same matching techniques.

Doctest.js just prints out exceptions, and it's matched like anything else.

This particular case is one of several places where it feels like Python's doctest is just being obstinate.  Doing it the right way isn't harder.  Python's doctest makes *debugging* exception cases really hard.

Doctest.js has a concept of "abort"
-----------------------------------

I'm actually pretty okay with Python doctest's notion that you just run all the tests, even when one fails.  Getting too many failures is a bit of a nuisance, but it's not *that bad*.  But there's no way to just give up, and there needs to be.  If you are relying on something to be importable, or some service to be available, there's no point in going on with the tests.

Doctest.js lets you call ``Abort()`` and further tests are cancelled.

Distinguishing between debugging output and deliberate output
-------------------------------------------------------------

Maybe it's my own fault for being a programming troglodite, but I use a lot of ``print`` for debugging.  This becomes a real problem with Python's doctest, as it tracks all that printing and it causes tests to fail.

Javascript has something *specifically for* printing debugging output: ``console.log()``.  Doctest.js doesn't mess with that, it adds a new function ``print()``.  Only stuff that is printed (not logged) is treated as expected output.  It's like ``console.log()`` goes to stderr and ``print()`` goes to stdout.

Doctest.js also forces the developer to print everything they care about.  For better or worse Javascript has many more expressions than Python (including assignments), so looking at the result of an expression isn't a good clue for whether you *care* about the result of an expression.  I'm not sure this is *better*, but it's part of the difference.

Doctest.js also groups your printed statements according to the example you are in (an example being a block of code and an expected output).  This is much more helpful than watching a giant stream of output go to the console (the browser console or terminal).

Doctest.js handles async code
-----------------------------

This admittedly isn't that big a deal for Python, but for Javascript it is a real problem.  Not a problem for doctest.js in particular, but a problem for any Javascript test framework.  You want to test return values, but lots of functions don't "return", instead they call some callback or create some kind of promise object, and you have to test for side effects.

Doctest.js I think has a `really great answer for this <http://doctestjs.org/tutorial.html#async>`_, which is not so much to say that Python's doctest is so much worse, but in the context of Javascript doctest.js has something really useful and unique.  If callback-driven async code had ever been very popular in Python then this sort of feature would be nice there too.

The browser is a great environment
----------------------------------

A lot of where doctest.js is much better than Python's doctest is simply that it has a much more powerful environment for displaying results.  It can highlight failed or passing tests.  When there's a wildcard in expected output, it can show the actual output without adding any particular extra distraction.  It can group console messages with the tests they go with.  It can show *both* a simple failure message, and a detailed line-by-line comparison.  All these details make it easy to identify what went wrong and fix it.  The browser gives a rich and navigable interface.

I'd *like* to get doctest.js working well on Node.js (right now it works, but is not appealing), but I just can't bring myself to give up the browser.  I have to figure out a good hybrid.

Python's doctest lacks a champion
---------------------------------

This is ultimately the reason Python's doctest has all these problems: no one cares about it, no one feels responsible for it, and no one feels empowered to make improvements to it.  And to make things worse there is a cadre of people that will respond to suggestions with their own criticisms that doctest should never be used beyond its original niche, that it's constraints are features.

Doctest is still great
----------------------

I'm ragging on Python's doctest only because I love it.  I wish it was better, and I made doctest.js in a way I wish Python's doctest was made.  Doctest, and more generally example/expectation oriented code, is a great way to explain things, to make tests readable, to make test-driven development feasible, to create an environment that errs on the side of over-testing instead of under-testing, and to make failures and resolutions symmetric.  It's still `vastly superior to BDD <https://ianbicking.org/behavior-driven-programming.html>`_, avoiding all BDD's aping of readability while still embracing the sense of test-as-narrative.

But, more to the point: `use doctest.js <http://doctestjs.org>`_, `read the tutorial <http://doctestjs.org/tutorial.html>`_, or `try it in the browser <http://doctestjs.org/try.html>`_.  I swear, it's *really nice to use*.
