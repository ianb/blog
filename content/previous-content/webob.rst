WebOb
#####
:date: 2007-08-18 19:37
:author: Ian Bicking
:tags: Programming, Python, Web

I've have it in my head to extract/rewrite parts of `Paste <http://pythonpaste.org>`_ lately.  `Tempita <http://blog.ianbicking.org/2007/08/06/tempita />`_ was one example.

The request and response functions in Paste grew very organically.  I wasn't trying to create a framework, so I studiously avoided anything that might look like a request or response object.  I felt that would be stepping on toes or something.  Eventually, though, `Ben Bangert <http://groovie.org />`_ really wanted a request object for `Pylons <http://pylonshq.com />`_, and it went in `paste.wsgiwrappers <http://pythonpaste.org/module-paste.wsgiwrappers.html>`_.  And at a certain point I decided that the class-based access was really just fine, and doing lots of ``function(environ, ...)`` was no better than ``Request(environ).function(...)``.

So I started `WebOb <http://pythonpaste.org/webob />`_.  WebOb has Request, Response, and some exceptions, incorporating the functionality of Paste's ``paste.request``, ``paste.response``, ``paste.wsgilib``, ``paste.httpexceptions``, and ``paste.httpheaders``.  And some extra stuff.

I've included a comparison with `a few other framework request/response objects <http://pythonpaste.org/webob/differences.html>`_.  What this doesn't note, though, is that WebOb has a much larger `Request <http://pythonpaste.org/webob/class-webob.Request.html>`_ and `Response <http://pythonpaste.org/webob/class-webob.Response.html>`_ objects.  I've taken almost all the `HTTP headers <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_ and mapped them to parsed attributes.  So ``req.if_modified_since`` returns a ``datetime`` object, and ``req.if_none_match`` returns a somewhat set-like object, as a few examples.  I created a lot of view-like objects for this, representing the canonical form of the information in several other forms (the WSGI request environment, and the status/headers/body of the response).

It's fairly well tested and includes almost everything I think it should include, but I reserve the right to change the API any way I want until 1.0; this means if you have *any* opinion on the API I have nothing to stop me from taking your opinions into account.

Oh, and it has `docs <http://pythonpaste.org/webob />`_, really.  They may not be the best docs, but they mention most everything and are automatically tested for accuracy.  If you just want a sense of the feel, maybe the `file-serving example <http://pythonpaste.org/webob/file-example.html>`_ would be a good place to start (though really you'll only read about the Response object there).
