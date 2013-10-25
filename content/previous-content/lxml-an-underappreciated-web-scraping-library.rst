lxml: an underappreciated web scraping library
##############################################
:date: 2008-12-10 21:19
:author: Ian Bicking
:tags: HTML, Programming, Python

When people think about web scraping in Python, they usually think `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup />`_.  That's okay, but I would encourage you to also consider `lxml <http://codespeak.net/lxml />`_.

First, people think BeautifulSoup is better at parsing broken HTML.  **This is not correct.**  lxml parses broken HTML quite nicely.  I haven't done any thorough testing, but at least `the BeautifulSoup broken HTML example <http://www.crummy.com/software/BeautifulSoup/documentation.html#Parsing%20HTML>`_ is parsed better by lxml (which knows that ``<td>`` elements should go inside ``<table>`` elements).

Second, people feel lxml is harder to install.  This is correct.  **BUT**, lxml 2.2alpha1 includes an option to compile static versions of the underlying C libraries, which should improve the installation experience, especially on Macs.  To install this new way, try::

    $ STATIC_DEPS=true easy_install 'lxml>=2.2alpha1'

One you have lxml installed, you have a great parser (which happens to be `super-fast <http://blog.ianbicking.org/2008/03/30/python-html-parser-performance />`_ and that is **not a tradeoff**).  You get a fairly familiar API based on `ElementTree <http://docs.python.org/library/xml.etree.elementtree.html#module-xml.etree.ElementTree>`_, which though a little strange feeling at first, offers a compact and canonical representation of a document tree, compared to more traditional representations.  But there's more...

One of the features that should be appealing to many people doing screen scraping is that you get CSS selectors.  You can use XPath as well, but usually that's more complicated (`for example <http://css2xpath.appspot.com/?css=div.pad%20a&amp; format=html>`_).  Here's `an example I found <http://crowtheries.net/?p=60>`_ getting links from a menu in a page in BeautifulSoup::

    from BeautifulSoup import BeautifulSoup
    import urllib2
    soup = BeautifulSoup(urllib2.urlopen('http://java.sun.com').read())
    menu = soup.findAll('div',attrs={'class':'pad'})
    for subMenu in menu:
        links = subMenu.findAll('a')
        for link in links:
            print "%s : %s" % (link.string, link['href'])

Here's the same example in lxml::

    from lxml.html import parse
    doc = parse('http://java.sun.com').getroot()
    for link in doc.cssselect('div.pad a'):
        print '%s: %s' % (link.text_content(), link.get('href'))

lxml generally knows more about HTML than BeautifulSoup.  Also I think it does well with the small details; for instance, the lxml example will match elements in ``<div class="pad menu">`` (space-separated classes), which the BeautifulSoup example does not do (obviously there are other ways to search, but `the obvious and documented technique <http://www.crummy.com/software/BeautifulSoup/documentation.html#Searching%20by%20CSS%20class>`_ doesn't pay attention to HTML semantics).

One feature that I think is really useful is ``.make_links_absolute()``.  This takes the base URL of the page (``doc.base``) and uses it to make all the links absolute.  This makes it possible to relocate snippets of HTML or whole sets of documents (as with `this program <http://svn.colorstudy.com/home/ianb/PageCollector/trunk>`_).  This isn't just ``<a href>`` links, but stylesheets, inline CSS with ``@import`` statements, ``background`` attributes, etc.  It doesn't see quite *all* links (for instance, links in Javascript) but it sees most of them, and works well for most sites.  So if you want to make a local copy of a site::

    from lxml.html import parse, open_in_browser
    doc = parse('http://wiki.python.org/moin/').getroot()
    doc.make_links_absolute()
    open_in_browser(doc)

``open_in_browser`` serializes the document to a temporary file and then opens a web browser (using `webbrowser <http://docs.python.org/library/webbrowser.html>`_).

Here's `an example <http://svn.colorstudy.com/home/ianb/recipes/lxmldiff.py>`_ that compares two pages using ``lxml.html.diff``::

    from lxml.html.diff import htmldiff
    from lxml.html import parse, tostring, open_in_browser, fromstring

    def get_page(url):
        doc = parse(url).getroot()
        doc.make_links_absolute()
        return tostring(doc)

    def compare_pages(url1, url2, selector='body div'):
        basis = parse(url1).getroot()
        basis.make_links_absolute()
        other = parse(url2).getroot()
        other.make_links_absolute()
        el1 = basis.cssselect(selector)[0]
        el2 = other.cssselect(selector)[0]
        diff_content = htmldiff(tostring(el1), tostring(el2))
        diff_el = fromstring(diff_content)
        el1.getparent().insert(el1.getparent().index(el1), diff_el)
        el1.getparent().remove(el1)
        return basis

    if __name__ == '__main__':
        import sys
        doc = compare_pages(sys.argv[1], sys.argv[2], sys.argv[3])
        open_in_browser(doc)

You can use it like::

    $ python lxmldiff.py \
    'http://wiki.python.org/moin/BeginnersGuide?action=recall&rev=70' \
    'http://wiki.python.org/moin/BeginnersGuide?action=recall&rev=81' \
    'div#content'

Another feature lxml has is form handling.  All the cool sexy new sites use minimal forms, but searching for "registration forms" I get `this nice complex form <http://www.actuaryjobs.com/cform.html>`_.  Let's look at it::

    >>> from lxml.html import parse, tostring
    >>> doc = parse('http://www.actuaryjobs.com/cform.html').getroot()
    >>> doc.forms
    [<Element form at -48232164>]
    >>> form = doc.forms[0]
    >>> form.inputs.keys()
    ['thank_you_title', 'City', 'Zip', ... ]

Now we have a form object.  There's two ways to get to the fields: ``form.inputs``, which gives us a dictionary of all the actual ``<input>`` elements (and textarea and select).  There's also ``form.fields``, which is a dictionary-like object.  The dictionary-like object is convenient, for instance::

    >>> form.fields['cEmail'] = 'me@example.com'

This actually updates the input element itself::

    >>> tostring(form.inputs['cEmail'])
    '<input type="input" name="cEmail" size="30" value="test2">'

I think it's actually a nicer API than `htmlfill <http://formencode.org/htmlfill.html>`_ and can serve the same purpose on the server side.

But then you can also use the same interface for scraping, by filling fields and getting the submission.  That looks like::

    >>> import urllib
    >>> action = form.action
    >>> data = urllib.urlencode(form.form_values())
    >>> if form.method == 'GET':
    ...     if '?' in action:
    ...         action += '&' + data
    ...     else:
    ...         action += '?' + data
    ...     data = None
    >>> resp = urllib.urlopen(action, data)
    >>> resp_doc = parse(resp).getroot()

Lastly, there's `HTML cleaning <http://codespeak.net/lxml/lxmlhtml.html#cleaning-up-html>`_.  I think all these features work together well, do useful things, and it's based on an actual understanding HTML instead of just treating tags and attributes as arbitrary.  (Also if you really like jQuery, you might want to look at `pyquery <http://pypi.python.org/pypi/pyquery>`_, which is a jQuery-like API on top of lxml).
