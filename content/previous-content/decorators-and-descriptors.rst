Decorators and Descriptors 
###########################
:date: 2008-10-24 00:18
:author: Ian Bicking
:tags: Python

So, `decorators <http://www.python.org/dev/peps/pep-0318 />`_ are neat (maybe check out a `new tutorial on them <http://www.artima.com/weblogs/viewpost.jsp?thread=240808>`_).  `Descriptors <http://users.rcn.com/python/download/Descriptor.htm>`_ are neat but may seem hard (though they hardly take a long time to describe).  Sometimes these two things intersect, and this post describes how.

Here's an example decorator where this comes up.  First, we want something that looks like a WSGI application::

    def application(environ, start_response):
        start_response('200 OK', [('content-type', 'text/html')])
        return ['hi!']

But we want to use WebOb, like::

    from webob import Request, Response
    def application(environ, start_response):
        req = Request(environ)
        resp = Response('hi!')
        return resp(environ, start_response)

(We don't use ``req`` in this example, but of course you probably would in a real WSGI application)

Now ``req = Request(environ)`` is boilerplate, and it'd be nicer to just do ``return resp`` instead of ``return resp(environ, start_response)``.  So let's make a decorator to do that::

    class wsgiapp(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, environ, start_response):
            resp = self.func(Request(environ))
            return resp(environ, start_response)

    @wsgiapp
    def application(req):
        return Response('hi!')

If you don't understand what happened there, go read up on decorators. 
Now, what if you want to decorate a method?  For instance::

    class Application(object):
        def __init__(self, text):
            self.text = text
        @wsgiapp
        def __call__(self, req):
            return Response(self.text)
    application = Application('hi!')

This won't *quite* work, because ``@wsgiapp`` will call ``Application.__call__(req)`` -- with *no self argument*.  This is generally a problem with any decorator that changes the signature, because the signature for methods has this extra ``self`` argument.  Descriptors can handle this.  First we'll have the same ``wsgiapp`` definition as we had before, but we'll add the magic descriptor method ``__get__``::

    class wsgiapp(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, environ, start_response):
            resp = self.func(Request(environ))
            return resp(environ, start_response)
        def __get__(self, obj, type=None):
            if obj is None:
                return self
            new_func = self.func.__get__(obj, type)
            return self.__class__(new_func)

So, to explain:

When you get an attribute from an instance, like ``Application().__call__``, Python will check if the object that was fetched has a ``__get__`` method.  If it does, it will call that method and use the result of that method.

This part::

    if obj is None:
        return self

is what happens when you do ``Application.__call__`` -- in other words, when get a class attribute.  In that case ``obj`` (self) will be None, and it will just return the descriptor (it *could* do something else, like in `this example <http://svn.colorstudy.com/home/ianb/recipes/classinstance.py>`_, but usually it doesn't).

Functions already have a ``__get__`` method.  You can try it yourself::

    >>> def example(*args):
    ...     print 'got', args
    >>> example_bound = example.__get__(1)
    >>> example_bound('test')
    got (1, 'test')

So in the example with ``wsgiapp`` we are just changing the decorator to wrap the new *bound* function instead of the old unbound function.  This allows ``wsgiapp`` to be compatible with both plain functions and methods.  In fact, it would probably be preferable to *always* call ``func.__get__(obj, type)`` (even if ``obj is None``), as then we could also wrap class methods or other kinds of descriptors.
