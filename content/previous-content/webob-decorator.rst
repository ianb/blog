WebOb decorator
###############
:date: 2009-05-22 20:35
:author: Ian Bicking
:tags: Programming, Python, Web

Lately I've been writing a few applications (e.g., `PickyWiki <http://pickywiki.org>`_ and a revisiting a request-tracking application `VaingloriousEye <http://svn.pythonpaste.org/Paste/VaingloriousEye/trunk>`_), and I usually use no framework at all.  `Pylons <http://pylonshq.com>`_ would be a natural choice, but given that I am comfortable with all the components, I find myself inclined to assemble the pieces myself.

In the process I keep writing bits of code to make WSGI applications from simple `WebOb <http://pythonpaste.org/webob />`_ -based request/response cycles.  The simplest form looks like this::

    from webob import Request, Response, exc

    def wsgiwrap(func):
        def wsgi_app(environ, start_response):
            req = Request(environ)
            try:
                resp = func(req)
            except exc.HTTPException, e:
                resp = e
            return resp(environ, start_response)
        return wsgi_app

    @wsgiwrap
    def hello_world(req):
        return Response('Hi %s!' % (req.POST.get('name', 'You')))

But each time I'd write it, I change things slightly, implementing more or less features.  For instance, `handling methods <http://blog.ianbicking.org/2008/10/24/decorators-and-descriptors />`_, or coercing other responses, or handling middleware.

Having implemented several of these (and `reading other people's implementations <http://svn.pythonpaste.org/Paste/WebOb/contrib>`_) I decided I wanted WebOb to include a kind of reference implementation.  But I don't like to include anything in WebOb unless I'm sure I can get it *right*, so I'd really like feedback.  (There's been some `less than positive feedback <http://groups.google.com/group/paste-users/browse_thread/thread/7346e75940413f46>`_, but I trudge on.)

My implementation is in a `WebOb branch <http://svn.pythonpaste.org/Paste/WebOb/branches/ianb-decorator-experiment>`_, primarily in `webob.dec <http://svn.pythonpaste.org/Paste/WebOb/branches/ianb-decorator-experiment/webob/dec.py>`_ (along with some `doctests <http://svn.pythonpaste.org/Paste/WebOb/branches/ianb-decorator-experiment/tests/test_dec.txt>`_).

The most prominent way this is different from the example I gave is that it doesn't change the function signature, instead it adds an attribute ``.wsgi_app`` which is WSGI application associated with the function.  My goal with this is that the decorator isn't intrusive.  Here's the case where I've been bothered::

    class MyClass(object):
        @wsgiwrap
        def form(self, req):
            return Response(form_html...)

        @wsgiwrap
        def form_post(self, req):
            handle submission

OK, that's fine, then I add validation::

    @wsgiwrap
    def form_post(self, req):
        if req not valid:
            return self.form
        handle submission

This still works, because the decorator allows you to return *any* WSGI application, not just a WebOb Response object.  But that's not helpful, because I need errors...

::

    @wsgiwrap
    def form_post(self, req):
        if req not valid:
            return self.form(req, errors)
        handle submission

That is, I want to have an option argument to the ``form`` method that passes in errors.  But I can't do this with the traditional ``wsgiwrap`` decorator, instead I have to refactor the code to have a third method that both ``form`` and ``form_post`` use.  Of course, there's more than one way to address this issue, but this is the technique I like.

The one other notable feature is that you can also make middleware::

    @wsgify.middleware
    def cap_middleware(req, app):
        resp = app(req)
        resp.body = resp.body.upper()
        return resp

    capped_app = cap_middleware(some_wsgi_app)

Otherwise, for some reason I've found myself putting an inordinate amount of time into ``__repr__``.  Why I've done this I cannot say.
