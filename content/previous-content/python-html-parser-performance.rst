Python HTML Parser Performance
##############################
:date: 2008-03-30 19:54
:author: Ian Bicking
:tags: HTML, Programming, Python

In preparation for my `PyCon talk on HTML <http://blog.ianbicking.org/2008/03/21/pycon-talks />`_ I thought I'd do a performance comparison of several parsers and document models.

The situation is a little complex because there's different steps in handling HTML:

1. Parse the HTML
2. Parse it *into* something (a document object)
3. Serialize it

Some libraries handle 1, some handle 2, some handle 1, 2, 3, etc.  For instance, `ElementSoup <http://effbot.org/zone/element-soup.htm>`_ uses `ElementTree <http://effbot.org/zone/element-index.htm>`_ as a document, but `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup />`_ as the parser.  BeautifulSoup itself has a document object included.  `HTMLParser <http://python.org/doc/current/lib/module-HTMLParser.html>`_ *only* parses, while `html5lib <http://code.google.com/p/html5lib />`_ includes tree builders for several kinds of trees.  There is also XML and HTML serialization.

So I've taken several combinations and made benchmarks.  The combinations are:

* `lxml <http://codespeak.net/lxml />`_: a parser, document, and HTML serializer.  Also can use BeautifulSoup and html5lib for parsing.
* `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup />`_: a parser, document, and HTML serializer.
* `html5lib <http://code.google.com/p/html5lib />`_: a parser.  It has a serializer, but I didn't use it.  It has a built-in document object (simpletree), but I don't think it's meant for much more than self-testing.
* `ElementTree <http://effbot.org/zone/element-index.htm>`_: a document object, and XML serializer (I think newer versions might include an HTML serializer, but I didn't use it).  It doesn't have a parser, but I used html5lib to parse to it.  (I didn't use the ElementSoup.)
* `cElementTree <http://effbot.org/zone/celementtree.htm>`_: a document object implemented as a C extension.  I didn't find any serializer.
* `HTMLParser <http://python.org/doc/current/lib/module-HTMLParser.html>`_: a parser.  It didn't parse *to* anything.  It also doesn't parse lots of normal (but maybe invalid) HTML.  When using it, I just ran documents through the parser, not constructing any tree.
* `htmlfill <http://formencode.org/htmlfill.html>`_: this library uses HTMLParser, but at least pays *a little* attention to the elements as they are parsed.
* `Genshi <http://genshi.edgewall.org />`_: includes a parser, document, and HTML serializer.
* `xml.dom.minidom <http://python.org/doc/current/lib/module-xml.dom.minidom.html>`_: a document model built into the standard library, which html5lib can parse to.  (I do not recommend using minidom for anything -- some reasons will become apparent in this post, but there are many other reasons not covered why you shouldn't use it.)

I expected lxml to perform well, as it is based on the C library `libxml2 <http://xmlsoft.org />`_.  But it performed better than I realized, far better than any other library.  As a result, if it wasn't for some persistent installation problems (especially on Macs) I would recommend lxml for just about any HTML task.

You can try the code out `here <http://svn.colorstudy.com/home/ianb/python-html-perf>`__.  I've included all the sample data, and the commands I ran for these graphs are `here <http://svn.colorstudy.com/home/ianb/python-html-perf/results.html>`__.  These tests use a fairly random selection of HTML files (355 total) taken from python.org.

**Parsing**

.. raw:: html

   <img src="http://blog.ianbicking.org/wp-content/uploads/images/parsing-results.png" alt="lxml:0.6; BeautifulSoup:10.6; html5lib ElementTree:30.2; html5lib minidom:35.2; Genshi:7.3; HTMLParser:2.9; htmlfill:4.5" style="padding: 1em">

The first test parses the documents.  Things to note: lxml is 6x faster than even HTMLParser, even though HTMLParser isn't *doing* anything (lxml is building a tree in memory).  I didn't include all the things html5lib can parse to, because they all take about the same amount of time.  xml.dom.minidom is only included because it is so noticeably slow.  Genshi is fairly fast, but it's the most fragile of the parsers.  html5lib, lxml, and BeautifulSoup are all fairly similarly robust.  html5lib has the benefit of (at least in theory) being *the* correct parsing of HTML.

While I don't really believe it matters often, lxml releases the GIL during parsing.

**Serialization**

.. raw:: html

   <img src="http://blog.ianbicking.org/wp-content/uploads/images/serialization-results.png" alt="lxml:0.3; BeautifulSoup:2.0; html5lib ElementTree:1.9; html5lib minidom:3.8; Genshi:4.4" style="padding: 1em">

Serialization is pretty fast across all the libraries, though again lxml leads the pack by a long distance.  ElementTree and minidom are only doing XML serialization, but there's no reason that the HTML equivalent would be any faster.  That Genshi is slower than minidom is surprising.  That *anything* is worse than minidom is generally surprising.  

**Memory**

.. raw:: html

   <img src="http://blog.ianbicking.org/wp-content/uploads/images/memory-results.png" alt="lxml:26; BeautifulSoup:82; BeautifulSoup lxml:104; html5lib cElementTree:54; html5lib ElementTree:64; html5lib simpletree:98; html5lib minidom:192; Genshi:64; htmlfill:5.5; HTMLParser:4.4" style="padding: 1em">

The last test is of memory.  I don't have a lot of confidence in the way I made this test, but I'm sure it means *something*.  This was done by parsing all the documents and holding the documents in memory, and using the RSS size reported by ``ps`` to see how much the process had grown.  All the libraries should be imported when calculating the baseline, so only the documents and parsing should cause the memory increase.  

HTMLParser is a baseline, as it just keeps the documents in memory as a string, and creates some intermediate strings.  The intermediate strings don't end up accounting for anything, since the memory used is almost exactly the combined size of all the files.

A tricky part of this measurement is that the Python allocator doesn't let go of memory that it requests, so if a *parser* creates lots of intermediate strings and then releases them the process will still hang onto all that memory.  To detect this I tried allocating new strings until the process size grew (trying to detect allocated but unused memory), but this didn't reveal much -- only the BeautifulSoup parser, serialized to an lxml tree, showed much extra memory.

This is one of the only places where html5lib with **c**\ ElementTree was noticeably different than html5lib with ElementTree.  Not that surprising, I guess, since I didn't find a coded-in-C serializer, and I imagine the tree building is only going to be a lot faster for cElementTree if you are building the tree from C code (as its native XML parser would do).

lxml is probably memory efficient because it uses native libxml2 data structures, and only creates Python objects on demand.

**In Conclusion**

I knew lxml was fast before I started these benchmarks, but I didn't expect it to be quite *this* fast.

So in conclusion: lxml kicks ass.  You can use it in ways you couldn't use other systems.  You can parse, serialize, parse, serialize, and repeat the process a couple times with your HTML before the performance will hurt you.  With high-level constructs many constructs can happen in very fast C code without calling out to Python.  As an example, if you do an XPath query, the query string is compiled into something native and traverses the native libxml2 objects, only creating Python objects to wrap the query results.  In addition, things like the modest memory use make me more confident that lxml will act reliably even under unexpected load.

I also am more confident about using a document model instead of stream parsing.  It is sometimes felt that streamed parsing is better: you don't keep the entire document in memory, and your work generally scales linearly with your document size.  HTMLParser is a stream-based parser, emitting events for each kind of token (open tag, close tag, data, etc).  Genshi also uses this model, with higher-level stuff like `filters <http://genshi.edgewall.org/wiki/Documentation/0.4.x/filters.html>`_ to make it feel a bit more natural.  But the stream model is *not* the natural way to process a document, it's actually a really awkward way to handle a document that is better seen as a single thing.  If you are processing gigabyte files of XML it can make sense (and both the normally document-oriented lxml and ElementTree offer options when this happens).  This doesn't make any sense for HTML.  And these tests make me believe that even *really big* HTML documents can be handled quite well by lxml, so a huge outlying document won't break a system that is appropriately optimized for handling normal sized documents.

