Inverted Partials
#################
:date: 2008-09-08 21:12
:author: Ian Bicking
:tags: HTML, Programming, Python

I was talking with a coworker some time ago about `his project <http://melkjug.com />`_, and he needed to update a piece of the page in-place when you go back to the page, and setting the page as uncacheable didn't really work.  Which probably makes sense; I think at one time browsers *did* respect those cache controls, but as a result going back in history *through* a page could cause some intermediate page to be refreshed and needlessly slow down your progress.

Anyway, Rails uses `partials <http://wiki.rubyonrails.org/rails/pages/UnderstandingPartials>`_ to facilitate this kind of stuff in a general way.  Bigger chunks of your page are defined in their own template, and instead of rendering the full page you can ask just for a chunk of the page.  Then you do something like ``document.getElementById('some_block').innerHTML = req.responseText``.  Mike Bayer just `described how to do this in Mako too <http://techspot.zzzeek.org/?p=29>`_, using template functions.

When asked, another technique also occurred to me, using just HTML.  Just add a general way of fetching an element by ID.  At any time you say "refresh the element with id X", and it asks the server for the current version of that element (using a query string variable ``document_id=X``) and replaces the content of that element in the browser.

The client side looks like this (it would be much simpler if you used a Javascript library)::

    function refreshId(id) {
        var el = document.getElementById(id);
        if (! el) {
            throw("No element by id '" + id + "'");
        }
        function handler(data) {
            if (this.readyState == 4) {
                if (this.status == 200) {
                    el.innerHTML = this.responseText;
                } else {
                    throw("Bad response getting " + idURL + ": "
                          + this.status);
                }
            }
        }
        var req = new XMLHttpRequest();
        req.onreadystatechange = handler;
        var idURL = location.href + '';
        if (idURL.indexOf('?') == -1) {
            idURL += '?';
        } else {
            idURL += '&';
        }
        idURL += 'document_id='+escape(id);
        req.open("GET", idURL);
        req.send();
    }

Then you need the server-side component.  Here's something written for `Pylons <http://pylonshq.com />`_ (using `lxml.html <http://codespeak.net/lxml/lxmlhtml.html>`_, and Pylons 0.9.7 which is configured to use `WebOb <http://pythonpaste.org/webob />`_)::

    from pylons import request, response
    from lxml import html

    def get_id(response, id):
        if (response.content_type == 'text/html'
            and response.status_int == 200):
            doc = html.fromstring(response.body)
            try:
                el = doc.get_element_by_id(id)
            except KeyError:
                pass
            else:
                response.body = html.tostring(el)
        return response
            
    class BaseController(WSGIController):
        def __after__(self):
            id = req.GET.get('document_id')
            if id:
                get_id(response, id)

Though I'm not sure this is appropriate for middleware, you could do it as middleware too::

    from webob import Request
    class DocumentIdMiddleware(object):
        def __init__(self, app):
            self.app = app
        def __call__(self, environ, start_response):
            req = Request(environ)
            id = req.GET.get('document_id')
            if not id:
                return self.app(environ, start_response)
            resp = req.get_response(self.app)
            resp = get_id(resp, id)
            return resp(environ, start_response)

