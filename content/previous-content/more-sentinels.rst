More Sentinels
##############
:date: 2010-04-02 12:26
:author: Ian Bicking
:tags: Programming, Python

I've been casually perusing `Paradigms of Artificial Intelligence Programming: Case Studies in Common Lisp <http://norvig.com/paip.html>`_.  One of the things I am noticing is that Lisp traditionally has a terrible lack of sentinels: special objects denoting some kind of meaning.  Specifically in Common Lisp the empty list and false and nil are all the same thing.  As a result there's all these cases where you want to distinguish false from empty, especially when false represents a failure of some sort.  In these AI examples, usually a failure to find something, while in many cases the empty list could mean "the thing is already found, no need to look".  But there's also lots of other examples when this causes problems.

More modern languages usually distinguish between these objects. Python for instance has ``[]``, ``False`` and ``None``.  They might all test as "falsish", but if you care to tell the difference it is easy to do; especially common is a test for ``x is None``.  Modern Lisps also stopped folding together all these notions (Scheme for example has ``#f`` for false as a completely distinct object, though null and the empty list are still the same).  XML-RPC is an example of a language missing null... and though JSON is almost the same data model, it is a great deal superior for having null.  In comparison no one seems to care much one way or the other about making a strong distinction between True/False and 1/0.

These are all examples of sentinels: special objects that represent some state.  None doesn't *mean* anything in particular, but it means lots of things specifically.  Maybe it means "not found" in one place, or "give me anything I don't care" in another.  But sometimes you need more than one of these in the same place, or None isn't entirely clear.

One thing I noticed while reading some Perl 6 examples is that they've added a number of new sentinels.  One is ``*``.  So you could write something like ``item(*)`` to mean "give me any item, your choice". While the Perl tendency to use punctuation is legend, words work too.

I wonder if we need a few more sentinel conventions?  If so what?

Of course any object can become a sentinel if you use it like that, None isn't *more* unique than any other object.  (None *is* conveniently available everywhere.)

``Any`` seems useful, ala Perl's ``*``.  But... there's already an `any <http://docs.python.org/library/functions.html#any>`_ available everywhere as well.  It happens to be a function, but it's also a unique named object... would it be entirely too weird to do ``obj is any``?  And there's very few cases where the actual function ``any`` would be an appropriate input, making it a good sentinel.
