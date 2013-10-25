Defaults & Inheritance
######################
:date: 2007-08-10 17:45
:author: Ian Bicking
:tags: Programming, Python

I thought I'd note a way I try to make classes reasonably customizable without creating lots of classes, but letting other people create classes if they want.

Here's a common technique; I'm going to use a class from `WSGIProxy <http://pythonpaste.org/wsgiproxy />`_ as an example, because that's where I was about to use this technique when I thought it might make an okay post.

In this example there's a WSGI application that forwards requests to another HTTP server.  There's different ways to forward requests, depending on what kind of data you want to give the remote server about the original request.  One example is Zope's VirtualHostMonster, which takes requests like ``/VirtualHostBase/http/example.org:80/rootdir/VirtualHostBase/path`` -- the idea is that the server can then realize that the original request was for ``http://example.org/path`` (and should ignore any Host headers), and that Zope is supposed to serve that from the internal path ``/rootdir/path``.

There's a problem with this particular pattern, because there's no way to mount, say, ``/blog`` onto some Zope ``/sitename/blog-application`` path, because there's no concept like in WSGI or CGI of SCRIPT_NAME -- the base *path* of the request.  It only handles the base *host*.  So I didn't just want to settle on that.

I'm kind of inclined to prefer headers, like ``X-Script-Name: /blog``, ``X-Forwarded-Server: example.org``, etc.  But I want to support both forms.

The common way to do this is::

    class WSGIProxyApp(object):

        def __init__(self, host): ...

        def __call__(self, environ, start_response):
            # actual application interface...
            # Constructs the base request:
            request = self.construct_request(environ)
            # Uses one of these conventions:
            self.update_headers(environ, request)
            ... do stuff with request ...

        def update_headers(self, orig_environ, request):
            raise NotImplementedError

    class VirtualHostMonsterApp(WSGIProxyApp):

        def update_headers(self, orig_environ, request):
            request.environ['SCRIPT_NAME'] = (
                '/VirtualHostRoot/%(wsgi.scheme)s/%(HTTP_HOST)s/VirtualHostRoot/'
                % orig_environ)
    
    class HeaderSetterApp(WSGIProxyApp):

        def update_headers(self, orig_environ, request):
            request.environ['HTTP_X_SCRIPT_NAME'] = orig_environ['SCRIPT_NAME']            
            # and so on...

Then you use one of the subclasses depending on your needs. Personally I think this really sucks.  For one thing, you may have to determine which class to use based on some configuration parameter, which can get awkward.  And you might want to subclass the class to change the functionality some yourself, but you have to subclass *both* of them.  There's patterns to handle this, with policies and factories and other crap; but it's *not a hard problem*, and those patterns are hard solutions to a problem that *shouldn't* be hard.

Also, it's harder to inform people about the options available to them, and somewhat harder to use these classes.  So I tend to do something like::

    class WSGIProxyApp(object):
        default_forwarding_style = 'headers'

        def __init__(self, host, forwarding_style=None):
            ...
            if forwarding_style is None:
                forwarding_style = self.default_forwarding_style
            self.forwarding_style = forwarding_style

        def __call__(self, environ, start_response):
            ...
            method = self.forwarding_style
            if isinstance(method, str):
                method = getattr(self, 'forward_'+self.forwarding_style)
            method(environ, request)
            ...

        def forward_headers(self, orig_environ, request): ...
        def forward_virtual_host_monster(self, orig_environ, request): ...

This way it's just a simple parameter to change the style.  You can pass in your own function, or use one of the named methods already available.  The ``default_forwarding_style`` class variable lets you change the default in subclasses.  If the default was in the function signature it would be much more awkard to change it, because you'd have to override the method and its signature with just that one change, then delegate back to the superclass method.
