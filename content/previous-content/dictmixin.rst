DictMixin
#########
:date: 2007-08-17 00:02
:author: Ian Bicking
:tags: Programming, Python

Quite some time ago I gave a little presentation on `DictMixin <http://python.org/doc/current/lib/module-UserDict.html>`_ at `ChiPy <http://chipy.org>`_.  If you haven't used DictMixin before, it's a class that implements all the derivative methods of dictionaries so you only have to implement the most minimal set: ``__getitem__``, ``__setitem__``, ``__delitem__``, and ``keys``.  It's a lot better than subclassing ``dict`` directly, as you have to implement a lot more, and ``dict`` implies a specific kind of storage.  With DictMixin you can get the information from anywhere.

I thought of a couple examples, and wrote some `doctests <http://python.org/doc/current/lib/module-doctest.html>`_ for them; I thought satisfying the doctests would itself be the presentation. I'm not sure how it worked; it was a fairly experienced crowd, but the switch from code to test can be disorienting.

One of the examples I used was a filesystem access layer. Representing a filesystem as a dictionary is nothing new, but the simplicity of the representation worked well.  Here's how it works:

* An ``FSDict`` represents one directory.
* The keys are the filenames in the directory.
* The values are the contents of the files (strings).
* When there is a subdirectory, it is another FSDict instance.
* When you assign a dictionary-like object to a key, it creates a   FSDict from that object.

Dictionaries have lots of methods, like ``items()``, ``update()``, etc.  But using DictMixin you just implement the four methods.  First, the setup::

    class FSDict(DictMixin):
        def __init__(self, path):
            self.path = path

*Creation* of a dictionary is not part of the dictionary interface. This seems a little strange at first, but the ``dict`` *class* interface isn't the same as the dictionary *instance* interface.  So ``FSDict.__init__`` doesn't bear any particular relation to ``dict.__init__``.

Now the other methods... in each case, strings and dictionaries (files and directories) are treated differently.

::

    def __getitem__(self, item):
        fn = os.path.join(self.path, item)
        if not os.path.exists(fn):
            raise KeyError("File %s does not exist" % fn)
        if os.path.isdir(fn):
            return self.__class__(fn)
        f = open(fn, 'rb')
        c = f.read()
        f.close()
        return c

Note the use of ``self.__class__(fn)`` instead of ``FSDict(fn)``. This makes the class subclassable if you retain the ``FSDict.__init__`` signature.  This way subclasses will create new instances using the subclass.  Note also that ``KeyError`` is part of the dictionary interface (an important part!), so we can't raise ``IOError``.

Now, assignment...

::

    def __setitem__(self, item, value):
        if item in self:
            del self[item]
        fn = os.path.join(self.path, item)
        if isinstance(value, str):
            f = open(fn, 'wb')
            f.write(value)
            f.close()
        else:
            # Assume it is a dictionary
            os.mkdir(fn)
            f = self[item]
            f.update(value)

Note that with subdirectories (represented as nested dictionaries) we let ``DictMixin.update`` do all the hard work, and just create an empty directory to be filled.

Deletion...

::

    def __delitem__(self, item):
        fn = os.path.join(self.path, item)
        if not os.path.exists(fn):
            raise KeyError("File %s does not exist" % fn)
        if os.path.isdir(fn):
            ## one way...
            self[item].clear()
            os.rmdir(fn)
            ## another way...
            #shutil.rmtree(fn)
        else:
            os.unlink(fn)

Enumeration...

::

    def keys(self):
        return os.listdir(self.path)

So, to recursively copy ``'/foo/bar'`` to ``'/dest/path/bar'`` you do::

    FSDict('/dest/path')['bar'] = FSDict('/foo')['bar']

It doesn't really matter if ``'/foo/bar'`` is a directory or file. There's a number of other clever things that come out of this.  I think it's an example of the power of `a closed set <http://en.wikipedia.org/wiki/Closure_%28mathematics%29>`_ -- dictionaries are expressable from these four operations, and all the other methods can be derived from there.  If you find this interesting, you might want to read the `source for DictMixin <http://svn.python.org/view/python/trunk/Lib/UserDict.py?view=markup>`_; it's only about 95 lines.

My article `templating via dict wrappers <http://blog.ianbicking.org/templating-via-dict-wrappers.html>`_ has some other similar dict tricks.
