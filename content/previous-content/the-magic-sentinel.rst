The Magic Sentinel
##################
:date: 2008-12-03 22:59
:author: Ian Bicking
:tags: Programming, Python

In an effort to get back on the blogging saddle, here's a little note on default values in Python.

In Python there are often default values.  The most typical default value is None -- None is a object of vague meaning that almost screams "I'm a default".  But sometimes None is a valid value, and sometimes you want to detect the case of "no value given" and None can hardly be called *no value*.

Here's an example::

    def getuser(username, default=None):
        if not user_exists(username):
            return default
        ...

In this case there is *always* a default, and so anytime you call ``getuser()`` you have to check for a None result.  But maybe you have code where you'd really just like to get an exception if the user isn't found.  To get this you can use a `sentinel <http://en.wikipedia.org/wiki/Sentinel_(computer_science)>`_.  A sentinel is an object that has no particular meaning except to signal the end (like a NULL byte in a C string), or a special condition (like no default user).

Sometimes people do it like this::

    _no_default = ()
    def getuser(username, default=_no_default):
        if not user_exists(username):
            if default is _no_default:
                raise LookupError("No user with the username %r" % username)
            return default
        ...

This works because that zero-item tuple ``()`` is a unique object, and since we are using the comparison ``default is _no_default`` only that *exact* object will trigger that LookupError.

Once you understand the pattern, this is easy enough to read.  But when you use ``help()`` or other automatic generation it is a little confusing, because the default value just appears as ``()``.  You could also use ``object()`` or ``[]`` or anything else, but the automatically generated documentation still won't look that nice.  So for a bit more polish I suggest::

    class _NoDefault(object):
        def __repr__(self):
            return '(no default)'
    NoDefault = _NoDefault()
    del _NoDefault

    def getuser(username, default=NoDefault):
        ...

You might then think "hey, why isn't there one NoDefault that everyone can share?"  If you do share that sentinel you run the risk of accidentally passing in that value even though you didn't intend to.  The value "NoDefault" will become overloaded with meaning, just as None is.  By having a more private sentinel object you avoid that.  A single nice sentinal factory (like ``_NoDefault`` in this example) would be nice, though.  Though really `PEP 3102 <http://www.python.org/dev/peps/pep-3102 />`_ will probably make sentinals like this unnecessary for Python 3.0.

Note that you can also implement arguments with no default via ``*args`` and ``**kwargs``, e.g.::

    def getuser(username, *args):
        if not user_exists(username): 
            if not args:
                raise LookupError(...)
            else:
                return args[0]

But to do this right you should test that ``len(args)<=1``, raise appropriate errors, maybe consider keyword arguments, and so one.  It's a pain in the butt, and when you're finished the signature displayed by ``help()`` will be wrong anyway.
