Atom Models
###########
:date: 2007-08-02 10:30
:author: Ian Bicking
:tags: Javascript, Programming, Python

I've been doing a bit more with Atom lately.

First, I started writing a library to manipulate Atom feeds and entries.  For the moment this is located in `atom.py <http://svn.colorstudy.com/home/ianb/atom.py>`_.  It uses `lxml <http://codespeak.net/lxml />`_, as does everything markup related I do these days.

I came upon a revelation of sorts when I was writing the library.  I first started with a library that looked like this::

  class Feed(object):
      def __init__(self, title, ...):
          self.title = title
          ..
      @classmethod
      def parse(cls, xml):
          if isinstance(xml, basestring):
              xml = etree.XML(xml)
          title = xml.xpath('//title').text
          ...
          return cls(title, ...)
      def serialize(self):
          el = etree.Element('{%s}feed' % atom_ns)
          title = etree.Element('{%s}title' % atom_ns)
          title.text = self.title
          el.append(title)
          ...
          return el

Obviously there's ways to improve this and make it less verbose, and I went down that path for a while.  But then I decided the whole path was wrong.  Atom *is* XML.  It's not the representation of some object I'm creating.  If I have something that can't be represented in XML, it isn't Atom, and it doesn't belong in my Atom-related objects.

So instead I started making lxml more convenient when using Atom.  I don't keep any information except what is in the markup, I just make it more convenient to access that information.

I used lots of `descriptors
<http://users.rcn.com/python/download/Descriptor.htm>`_ to do this, as the same patterns happened over and over.  For instance, the Feed object is fairly simple::

  class Feed(AtomElement):
      entries = _findall_property('entry')
      author = _element_property('author')

Which basically means that ``feed.entries`` returns all ``<entry>`` elements, and ``feed.author`` returns the single ``author`` element.

There's also accessors for text elements (like ``<id>``) and date containing elements (like ``<updated>``) and just to access XML attributes as Python attributes.

There's a number of advantages:

* No hidden state.

* No deferred errors, since everything is always represented in the   `XML infoset <http://en.wikipedia.org/wiki/XML_Information_Set>`_.

* All XML extensions work, even though my classes don't know anything   in particular about them.  There's a full API for manipulating the   XML that you can use, you don't have to use my APIs.

* Even more obscure kinds of extensions work fine, like a custom attribute on an element.  There's absolutely zero normalization that happens.

* I only have to write the parts where the normal XML (lxml) APIs are inconvenient, so the implementation stays simple.

* There's no confusion over which object I might be talking about in my code.  There's no distinction between the XML object and the domain object.

Since then I've been working on a `Javascript library
<https://svn.openplans.org/svn/TaggerClient/trunk/javascript/atom.js>`_ for handling Atom.  It's not as elegant.  I am trying to keep to this same principle, but of course I can't actually extend the DOM and so I can't add convenience methods.  So instead I'm making a class that lightly wraps the DOM objects, with explicit getters and setters that simply read and modify those DOM objects.

One thing that I have found very useful in my development on the Javascript side is doctest-style testing.  You can see the `test <https://svn.openplans.org/svn/TaggerClient/trunk/javascript/tests/test.html>`_, but to run it you have to check it out (it uses some ``svn:externals`` which you don't get through the direct svn access).  After using that testing some more and being pleased with the result, I decided to package the Javascript doctest runner a bit better.  I removed the framework dependencies, did a bit of renaming (now it is *doctestjs* or ``doctest.js`` instead of *jsdoctest*), wrote up `fairly comprehensive docs <http://svn.colorstudy.com/doctestjs/trunk/docs/index.html>`_, and uploaded it to `JSAN
<http://openjsan.org/doc/i/ia/ianb/doctestjs/0.9 />`_ (though at the moment the trunk from svn is probably better to use).  I think it's an excellent way of doing unit testing in Javascript, much better than any of the alternatives I've seen.  It even has some notable advantages over `Python's doctest <http://python.org/doc/current/lib/module-doctest.html>`_, like if you are using `Firebug <http://www.getfirebug.com />`_ (which you must if you do Javascript development) you get a console session that runs in the same namespace as your tests, so you can easily do inspection of the objects if there's a failure.

I'm not sure about JSAN.  It's nice to have an index.  But I think they copy stuff from CPAN a bit too much.  Why should you have a text README file?  That's just silly; of course Javascript documentation should be HTML.  They batch processing.  Processing one package a day
on the fly shouldn't be overwhelming.  They want a MANIFEST file.  The standard metadata file is YAML, not JSON.  This should all be a little more Javascripty in my opinion.  But they also accept any kind of upload, so there's nothing stopping you from ignoring what you don't
care about.  I'll probably improve the packaging of doctestjs a bit in the future, and still ignore the parts I think are silly.
