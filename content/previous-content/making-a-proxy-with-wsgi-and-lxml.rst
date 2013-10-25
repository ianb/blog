Making a proxy with WSGI and lxml
#################################
:date: 2008-07-30 10:52
:author: Ian Bicking
:tags: Programming, Python

You can use WSGI to make rewriting middleware; `WebOb <http://pythonpaste.org/webob />`_ specifically makes it easy to write.  And that's cool, but it's more satisfying to use your middleware right away without having to think about writing applications that might live behind the middleware.

There's two libraries I'll describe here to make that possible: `paste.proxy <http://pythonpaste.org/modules/proxy.html#paste.proxy.Proxy>`_ to send WSGI requests out via HTTP, and `lxml.html <http://codespeak.net/lxml/lxmlhtml.html>`_ which lets you rewrite the HTML to fix up the links.

To start, we need some kind of middleware that at least is noticeable.  How about something to make a word jumble of the page?  We'll use lxml as well::

    from lxml import html
    from random import shuffle

    def jumble_words(doc):
        """Mixes up the words in an HTML document (doesn't touch tags or attributes)"""
        doc = html.fromstring(doc)
        # .text_content() gives the text without tags or attributes,
        # .body is the <body> tag:
        words = doc.body.text_content().split()
        shuffle(words)
        for el in doc.body.iterdescendants():
            # The ElementTree model puts all text in .text and .tail on elements, so that's
            # what we mix up:
            el.text = random_words(el.text, words)
            el.tail = random_words(el.tail, words)
        return html.tostring(doc)

    def random_words(text, words):
        """Pulls some words from the list words, with the same number of words in
        the previous `text`"""
        # text can be None, so we need this test:
        if not text:
            return text
        word_count = len(text.split())
        try:
            return ' '.join(words.pop() for i in range(word_count))
        except IndexError:
            # This shouldn't happen, because we should have exactly
            # the right number of words, but just in case...
            return text

    from webob import Request

    class JumbleMiddleware(object):
        """Middleware that jumbles the words of HTML responses
        """
        # This __init__ and __call__ are the basic pattern for middleware:
        def __init__(self, app):
            self.app = app
        def __call__(self, environ, start_response):
            req = Request(environ)
            # We don't want 304 Not Modified responses, because we mix up the response
            # differently every time.  So we'll make sure all the headers that could call that
            # (If-Modified-Since, etc) are removed with .remove_conditional_headers():
            req.remove_conditional_headers()
            # This calls the application with the request, and then returns a response; this
            # is the typical pattern for response-modifying middleware using WebOb:
            resp = req.get_response(self.app)
            if resp.content_type == 'text/html':
                resp.body = jumble_words(resp.body)
            return resp(environ, start_response)

Well, you don't really need to jumble up your *own* pages, right?  Much more fun to jumble other people's pages.  Enter the proxy.  Here's a basic proxy::

    from paste.proxy import Proxy
    # We use this to make sure we didn't mess up anything with JumbleMiddleware;
    # the validator checks for many WSGI requirements:
    from wsgiref.validate import validator
    import sys

    def main():
        proxy_url = sys.argv[1]
        app = JumbleMiddleware(
            Proxy(proxy_url))
        app = validator(app)
        from paste.httpserver import serve
        serve(app, 'localhost', 8080)

    if __name__ == '__main__':
        main()

If you look at the `full source <http://svn.colorstudy.com/home/ianb/recipes/rewritingproxy.py>`_ the command-line is a bit fancier, but it's all obvious stuff.

OK, so this will work, but the links will often be broken unless the server only gives relative links.  But you can rewrite the links using lxml...

::

    import urlparse

    class LinkRewriterMiddleware(object):
        """Rewrites the response, assuming the HTML was generated as though based at 
        `dest_href`, and needs to be rewritten for the incoming request"""

        # The normal __init__, __call__ pattern:
        def __init__(self, app, dest_href):
            self.app = app
            if dest_href.endswith('/'):
                dest_href = dest_href[:-1]
            self.dest_href = dest_href

        def __call__(self, environ, start_response):
            req = Request(environ)
            # .path_info (aka environ['PATH_INFO']) is the path of the request
            # (URL rewriting doesn't really have to care about query strings)
            dest_path = req.path_info
            dest_href = self.dest_href + dest_path
            # req.application_url is the base URL not including path_info or the query string:
            req_href = req.application_url
            def link_repl_func(link):
                link = urlparse.urljoin(dest_href, link)
                if not link.startswith(dest_href):
                    # Not a local link
                    return link
                new_url = req_href + '/' + link[len(dest_href):]
                return new_url
            resp = req.get_response(self.app)
            # This decodes any possible gzipped content:
            resp.decode_content()
            if (resp.status_int == 200 
                and resp.content_type == 'text/html'):
                doc = html.fromstring(resp.body, base_url=dest_href)
                doc.rewrite_links(link_repl_func)
                resp.body = html.tostring(doc)
            # Redirects need their redirect locations rewritten:
            if resp.location:
                resp.location = link_repl_func(resp.location)
            return resp(environ, start_response)


Then we rewire the application::

    app = JumbleMiddleware(
        LinkRewriterMiddleware(Proxy(proxy_url), proxy_url))

Now there's a fun little proxy for you to play with.  You can see the code `here <http://svn.colorstudy.com/home/ianb/recipes/rewritingproxy.py>`_.
