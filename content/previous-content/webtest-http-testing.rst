WebTest HTTP testing
####################
:date: 2010-04-02 16:27
:author: Ian Bicking
:tags: Programming, Python, Web

I've yet to see another testing system for local web testing that I like as much as `WebTest <http://pythonpaste.org/webtest />`_... which is perhaps personal bias for something I wrote, but then I don't have that same bias towards everything I've written.  Many frameworks build in their own testing systems but I don't like the abstractions -- they touch lots of internal things, or skip important steps of the request, or mock out things that don't need to be mocked out.  WSGI can make this testing easy.

There's also a hidden feature here: because WSGI is basically just describing HTTP, it can be a means of representing not just incoming HTTP requests, but also outgoing HTTP requests.  If you are running local tests against your application using WebTest, with just a little tweaking you can turn those tests into HTTP tests (i.e., actually connect to a socket).  But doing this is admittedly not obvious; hence this post!

Here's what a basic WebTest test looks like::

    from webtest import TestApp
    import json

    wsgi_app = acquire_wsgi_application_somehow()
    app = TestApp(wsgi_app)

    def test_login():
        resp = app.post('/login', dict(username='guest', password='guest'))
        resp.mustcontain('login successful')
        resp = resp.click('home')
        resp.mustcontain('<a href="/profile">guest</a>')
        # Or with a little framework integration:
        assert resp.templatevars.get('username') == 'guest'

    # Or an API test:
    def test_user_query():
        resp = app.get('/users.json')
        assert 'guest' in resp.json['userList']
        user_info = dict(username='guest2', password='guest2', name='Guest')
        resp = app.post('/users.json', content_type='application/json',
                        body=json.dumps(user_info)
        assert resp.json == user_info

The ``app`` object is a wrapper around the WSGI application, and each of those methods runs a request and gets the response.  The response object is a WebOb response with several additional helpers for testing (things like ``.click()`` which finds a link in HTML and follows it, or ``.json`` which loads the body as JSON).

You *don't* have to be using a WSGI-centric framework like Pylons to use WebTest, it works fine with anything with a WSGI frontend, which is just about everything.  But the point of my post: you don't have to use it with a WSGI application at all.  Using `WSGIProxy <http://pythonpaste.org/wsgiproxy />`_::

    import os
    import urlparse

    if os.environ.get('TEST_REMOTE'):
        from wsgiproxy.exactproxy import proxy_exact_request
        wsgi_app = proxy_exact_request
        parsed = urlparse.urlsplit(os.environ['TEST_REMOTE'])
        app = TestApp(proxy_exact_request, extra_environ={
                      'wsgi.scheme': parsed.scheme,
                      'HTTP_HOST': parsed.netloc,
                      'SERVER_NAME': parsed.netloc})
    else:
        wsgi_app = acquire_wsgi_application_somehow()
        app = TestApp(wsgi_app)

It's a little crude to control this with an environmental variable (``$TEST_REMOTE``), but it's an easy way to pass an option in when there's no better way (and many test runners don't make options easy).  The ``extra_environ`` option puts in the host and scheme information into each request (the default host WebTest puts in is ``http://localhost``).  WSGIProxy lets you send a request to any host, kind of bypassing DNS, so ``SERVER_NAME`` is actually the server the request goes to, while ``HTTP_HOST`` is the value of the Host header.

Going over HTTP there are a couple features that won't work.  For instance, you can pass information about your application back to the test code by putting values in ``environ['paste.testing_variables']`` (which is how you'd make ``resp.templatevars`` work in the first example).  It's also possible to use ``extra_environ`` to pass information into your application, for example to get your application to mock out user authentication; this is fairly safe because in production no request can put those same special keys into the environment (using custom HTTP headers means you must carefully filter requests in production).  But custom environ values won't work over HTTP.

The thing that got me thinking about this is the work I'm doing on `Silver Lining <http://cloudsilverlining.org>`_, where I am taking apps and rearranging the code and modifying the database configuration ad setup to fit this deployment system.  It would be really nice having done that to be able to run some functional tests, and I really want to run them over HTTP.  If an application has tests using something like Selenium or Windmill that would also work great, but those tools can be a bit more challenging to work with and applications still need smaller tests anyway, so being able to reuse tests like these would be most useful.
