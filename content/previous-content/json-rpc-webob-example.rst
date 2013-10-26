JSON-RPC WebOb Example
######################
:date: 2008-04-02 22:37
:author: Ian Bicking
:tags: Programming, Python, Web

I just saw `this json-rpc recipe <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/552751>`_ go by as a popular link on del.icio.us.  It's yet-another-\*Server based recipe (BaseHTTPServer, XMLRPCServer, etc).  I don't know why people keep writing these.  WSGI is in all ways easier, clearer, and more useful.

So I figured I'd give it a go myself, using `WebOb <http://pythonpaste.org/webob />`_.  Then I figured it might make a good document, and I annotated it and turned it `into a tutorial <http://pythonpaste.org/webob/jsonrpc-example.html>`_.  It's also an example of using WebOb as a client library.

I've added several tutorials in the past months, which I thought I should also point out.  The `wiki example <http://pythonpaste.org/webob/wiki-example.html>`_ is fairly pedestrian, but shows how to do typical application-style development with WebOb.  A more interesting example is `the comment middleware example <http://pythonpaste.org/webob/comment-example.html>`_, which shows how much easier it can be to write middleware using WebOb than traditional WSGI middleware.

I think WebOb's particular strong points are with middleware (where it makes middleware vastly easier to write) and web services of various kinds (RESTful or not).

