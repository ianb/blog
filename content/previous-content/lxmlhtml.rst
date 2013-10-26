lxml.html
#########
:date: 2007-09-24 08:32
:author: Ian Bicking
:tags: HTML, Python

Over the summer I did quite a bit of work on `lxml.html <http://codespeak.net/svn/lxml/trunk/doc/lxmlhtml.txt>`_.  I'm pretty excited about it, because with just a little work HTML starts to be very usefully manipulatable.  This isn't how I've felt about HTML in the past, with all HTML emerging from templates and consumed only by browsers.

The ElementTree representation (which lxml copies) is a bit of a nuisance when representing HTML.  A `few methods <http://codespeak.net/lxml/dev/lxmlhtml.html#html-element-methods>`_ improve it, but it is still awkward for content with mixed tags and text (common in HTML, uncommon in most other XML).  Looking at `Genshi Transforms <http://genshi.edgewall.org/wiki/Documentation/filters.html#transformer>`_ there are some things I wish we could do, like simply "unwrap" text and then wrap it again.  But once you remove a tag the text is thoroughly merged into its neighbors.  Another little nuisance is that ``el.text`` and ``el.tail`` can be None, which means you have to guard a lot of code.

That said, here's the Genshi example::

    >>> html = HTML('''<html>
    ...   <head><title>Some Title</title></head>
    ...   <body>
    ...     Some <em>body</em> text.
    ...   </body>
    ... </html>''')
    >>> print html | Transformer('body/em').map(unicode.upper, TEXT) \
    ...                                    .unwrap().wrap(tag.u).end() \
    ...                                    .select('body/u') \
    ...                                    .prepend('underlined ')

Here's how you'd do it with lxml.html::

    >>> html = fromstring('''... same thing ...''')
    >>> def transform(doc):
    ...     for el in doc.xpath('body/em'):
    ...         el.text = (el.text or '').upper()
    ...         el.tag = 'u'
    ...     for el in doc.xpath('body/u'):
    ...         el.text = 'underlined ' + (el.text or '')

I'm not sure if Genshi works in-place here, or makes a copy; otherwise these are pretty much equivalent.  Which is better?  Personally I prefer mine, and actually prefer it quite strongly, because it's quite simple -- it's a function with loops and assignments.  It's practically pedestrian in comparison to the Genshi example, which uses methods to declaratively create a transformer.

Some of the things now in lxml.html include:

* `Link handling   <http://codespeak.net/lxml/dev/lxmlhtml.html#working-with-links>`_,   which is particularly focused on rewriting links so you can put HTML   fragments into a new context without breaking the relative links.

* `Smart doctest comparisons   <http://codespeak.net/lxml/dev/lxmlhtml.html#running-html-doctests>`_   (attribute-order-neutral comparisons, with improved diffs, and also   whitespace neutral, based loosely on `formencode.doctest_xml_compare   <http://formencode.org/module-formencode.doctest_xml_compare.html>`_).   Inside your doctest choose XML parsing with ``from lxml import   usedoctest`` or HTML parsing with ``from lxml.html import   usedoctest``.  I consider the import trick My Worst Monkeypatch   Ever, but it kind of reads nicely.  For testing it is very nice.

* `Cleaning code   <http://codespeak.net/lxml/dev/lxmlhtml.html#cleaning-up-html>`_, to   avoid XSS attacks, in ``lxml.html.clean``.  This is still pretty   messy, because there's lots of little things you may or may not want   to protect against.  E.g., I think I can mostly clean out style tags   (at least of Javascript), but some people might want to remove all   style.  So there's an option.  There's lots of options.  Too many.

* With the cleaning code there's `word-wrapping code   <http://codespeak.net/lxml/dev/lxmlhtml.html#wordwrap>`_ and   `autolinking code   <http://codespeak.net/lxml/dev/lxmlhtml.html#autolink>`_.  I think   of these as clean-up-people's-scrappy-HTML tools.  Also important   for putting untrusted HTML in a new context.

* I rewrote `htmlfill <http://formencode.org/htmlfill.html>`_ in   ``lxml.html.formfill``.  It's a bit simpler, and keeps error   messages separate from actual value filling.  They were really only   combined because I didn't want to do two passes with ``HTMLParser``   for the two steps, but that doesn't matter when you load the   document into memory.  I also stopped using markup like   ``<form:error>`` for placing error messages; it's all automatic now,   which I suppose is both good and bad.

* *After* I wrote ``lxml.html.formfill`` I got it into my head to make    smarter forms more natively.  So now you can do::

    >>> from lxml.html import parse
    >>> page = parse('http://tripsweb.rtachicago.com/').getroot()
    >>> form = page.forms[0]
    >>> from pprint import pprint
    >>> pprint(form.form_values())
    [('action', 'entry'),
     ('resptype', 'U'),
     ('Arr', 'D'),
     ('f_month', '09'),
     ('f_day', '21'),
     ('f_year', '2007'),
     ('f_hours', '9'),
     ('f_minutes', '30'),
     ('f_ampm', 'AM'),
     ('Atr', 'N'),
     ('walk', '0.9999'),
     ('Min', 'T'),
     ('mode', 'A')]
    >>> for key in sorted(f.fields.keys()):
    ...     print key
    None
    Arr
    Atr
    Dest
    Min
    Orig
    action
    dCity
    endpoint
    f_ampm
    f_day
    f_hours
    f_minutes
    f_month
    f_year
    mode
    oCity
    resptype
    startpoint
    walk
    >>> f.fields['Orig'] = '1500 W Leland'
    >>> f.fields['Dest'] = 'LINCOLN PARK ZOO'
    >>> from lxml.html import submit_form()
    >>> result = parse(submit_form(f)).getroot()

  From there I'd have to actually scrape the results to figure out   what the best trip was, which isn't as easy.

* HTML diffing and something like ``svn blame`` for a series of   documents, in ``lxml.html.diff``.  Someone noted a similarity   between htmldiff and `templatemaker   <http://code.google.com/p/templatemaker />`_, and they are   conceptually similar, but with very different purposes.  htmldiff   goes to great trouble to *ignore* markup and focus only on changes   to textual content.  As such it is great for a history page.   ``templatemaker`` focuses on the dissection of computer-generated   HTML and extracting its human-generated components.  Templatemaker   is focused on screen scraping.  It might be handy in that form   example above...

* There's also a fairly complete implementation of `CSS 3 selectors   <http://codespeak.net/lxml/dev/cssselect.html>`_.  It would be   interesting to mix this with `cssutils   <http://code.google.com/p/cssutils />`_.

  Though `some people aren't so enthusiastic about CSS namespaces   <http://alex.dojotoolkit.org/?p=625>`_ (and I can't really blame   him), conveniently this CSS 3 feature makes CSS selectors applicable to all XML.   I don't know if anyone is actually going to use them instead of   XPath on non-HTML documents, but you *could*.  Because the implementation  just   compiles CSS to XPath, you could potentially use this module with   other XML libraries that know XPath.  Of which I only actually know   `one <http://uche.ogbuji.net/tech/4suite/amara />`_ (or `two   <http://genshi.edgewall.org />`?) -- though compiling CSS to XPath,   then having XPath parsed and interpreted in Python, is probably not   a good idea.  But if you are so inclined, there's also a parser in   there you could use.

* lxml and `BeautifulSoup   <http://www.crummy.com/software/BeautifulSoup />`_ are no longer   exclusive choices: ``lxml.html.ElementSoup.parse()`` can parse pages   with BeautifulSoup into lxml data structures.  While the native   lxml/libxml2 HTML parser works on pretty bad HTML, BeautifulSoup   works on *really* bad HTML.  It would be nice to have something   similar with `html5lib <http://code.google.com/p/html5lib />`_.

