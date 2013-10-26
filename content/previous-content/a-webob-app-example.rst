What Does A WebOb App Look Like? 
#################################
:date: 2010-03-12 17:50
:author: Ian Bicking
:tags: Programming, Python, Web

Lately I've been writing code using WebOb and just a few other small libraries.  It's not entirely obvious what this looks like, so I thought I'd give a simple example.

I make each application a class.  Instances of the class are "configured applications".  So it looks a little like this (for an application that takes one configuration parameter, ``file_path``)::

    class Application(object):
        def __init__(self, file_path):
            self.file_path = file_path

Then the app needs to be a WSGI app, because that's how I roll.  I use `webob.dec <http://pythonpaste.org/webob/modules/dec.html>`_::

    from webob.dec import wsgify
    from webob import exc
    from webob import Response

    class Application(object):
        def __init__(self, file_path):
            self.file_path = file_path
        @wsgify
        def __call__(self, req):
            return Response('Hi!')

Somewhere separate from the application you actually instantiate ``Application``.  You can use `Paste Deploy <http://pythonpaste.org/deploy />`_ for that, configure it yourself, or just do something ad hoc (a lot of mod_wsgi ``.wsgi`` files are like this, basically).

I use `webob.exc <http://pythonpaste.org/webob/reference.html#exceptions>`_ for things like ``exc.HTTPNotFound()``.  You can raise that as an exception, but I mostly just return the object (to the same effect).

Now you have Hello World.  I then sometimes do something terrible, I start handling URLs like this::

    @wsgify
    def __call__(self, req):
        if req.path_info == '/':
            return self.index(req)
        elif req.path_info.startswith('/view/'):
            return self.view(req)
        return exc.HTTPNotFound()

This is lazy and a very bad idea.  So you want a dispatcher.  There are several (e.g., `selector <http://pypi.python.org/pypi/selector />`_).  I'll use `Routes <http://routes.groovie.org>`_ here... the latest release makes it a bit easier (though it could still be streamlined a bit).  Here's a pattern I think makes sense::

    from routes import Mapper

    class Application(object):
        map = Mapper()
        map.connect('index', '/', method='index')
        map.connect('view', '/view/{item}', method='view')

        def __init__(self, file_path):
            self.file_path = file_path

        @wsgify
        def __call__(self, req):
            results = self.map.routematch(environ=req.environ)
            if not results:
                return exc.HTTPNotFound()
            match, route = results
            link = URLGenerator(self.map, req.environ)
            req.urlvars = ((), match)
            kwargs = match.copy()
            method = kwargs.pop('method')
            req.link = link
            return getattr(self, method)(req, **kwargs)

        def index(self, req):
            ...
        def view(self, req, item):
            ...

Another way you might do it is to skip the class, which means skipping a clear place for configuration.  I don't like that, but if you don't care about that, then it looks like this::

    def index(self, req):
        ...
    def view(self, req, item):
        ...

    map = Mapper()
    map.connect('index', '/', view=index)
    map.connect('view', '/view/{item}', view=view)

    @wsgify
    def application(req):
        results = map.routematch(environ=req.environ)
        if not results:
            return exc.HTTPNotFound()
        match, route = results
        link = URLGenerator(map, req.environ)
        req.urlvars = ((), match)
        kwargs = match.copy()
        view = kwargs.pop('view')
        req.link = link
        return view(req, **kwargs)

Then ``application`` is pretty much boilerplate.  You could put configuration in the request if you wanted, or use some other technique (like `Contextual <http://pypi.python.org/pypi/Contextual>`_).

I talked some with `Ben Bangert <http://be.groovie.org />`_ about what he's trying with these patterns, and he's doing something reminiscent of Pylons controllers (but without the rest of Pylons) and it looks more like this (with my own adaptations)::

    class BaseController(object):
        special_vars = ['controller', 'action']

        def __init__(self, request, link, **config):
            self.request = request
            self.link = link
            for name, value in config.items():
                setattr(self, name, value)

        def __call__(self):
            action = self.request.urlvars.get('action', 'index')
            if hasattr(self, '__before__'):
                self.__before__()
            kwargs = req.urlsvars.copy()
            for attr in self.special_vars
                if attr in kwargs:
                    del kwargs[attr]
            return getattr(self, action)(**kwargs)

    class Index(BaseController):
        def index(self):
            ...
        def view(self, item):
            ...

    class Application(object):
        map = Mapper()
        map.connect('index', '/', controller=Index)
        map.connect('view', '/view/{item}', controller=Index,     action='view')

        def __init__(self, **config):
            self.config = config

        @wsgify
        def __call__(self, req):
            results = self.map.routematch(environ=req.environ)
            if not results:
                return exc.HTTPNotFound()
            match, route = results
            link = URLGenerator(self.map, req.environ)
            req.urlvars = ((), match)
            controller = match['controller'](req, link, **self.config)
            return controller()

That's a lot of code blocks, but they all really say the same thing ;)  I think writing apps with almost-no-framework like this is pretty doable, so if you have something small you should give it a go.  I think it's especially appropriate for applications that are an API (not a "web site").  
