Atompub as an alternative to WebDAV
###################################
:date: 2009-01-11 17:27
:author: Ian Bicking
:tags: HTML, Programming, Web

I've been thinking about an import/export API for `PickyWiki <http://pickywiki.org>`_; I want something that's sensible, and works well enough that it can be the basic for things like creating restorable snapshots, integration with version control systems, and being good at self-hosting documentation.

So far I've made a simple import/export system based on Atom.  You can export the entire site as an Atom feed, and you can import Atom feeds.  But whole-site import/export isn't enough for the tools I'd like to write on top of the API.

`WebDAV <http://en.wikipedia.org/wiki/WebDAV>`_ would seem like a logical choice, as it lets you get and put resources.   But it's not a great choice for a few reasons:

* It's really hard to implement on the server.

* Even clients are hard to implement.

* It uses GET to get resources.  This is probably its most fatal flaw.  There is no CMS that I know of (except `maybe one <http://www.tiddlywiki.com />`_) where the thing you view the browser is the thing that you'd actually edit.  To work around this CMSes use User-Agent sniffing or an alternate URL space.

* WebDAV is worried about "collections" (i.e., directories).  The web basically doesn't know what "collections" are, it only knows paths, and paths are strings.

* (In summary) WebDAV uses HTTP, but it is not *of the web*.

I don't want to invent something new though.  So I started thinking of Atom some more, and `Atompub <http://en.wikipedia.org/wiki/Atom_(standard)>`_.

The first thought is how to fix the GET problem in WebDAV.  A web page isn't an editable representation, but it's pretty reasonable to put an editable representation into an Atom entry.  Clients won't necessarily understand extensions and properties you might add to those entries, but I don't see any way around that.  An entry might look like::

  <entry>
    <content type="html">QUOTED HTML</content>
    ... other normal metadata (title etc) ...
    <privateprop:myproperty xmlns:privateprop="URL" name="foo" value="bar"  />
  </entry>

While there is special support for HTML, XHTML, and plain text in Atom, you can put any type of content in ``<content>``, encoded in base64.

To find the editable representation, the browser page can point to it.  I imagine something like this::

  <link rel="alternate" type="application/atom+xml; type=entry"
   href="this-url?format=atom">

The actual URL (in this example ``this-url?format=atom``) can be pretty much anything.  My one worry is that this could be confused with feed detection, which looks like::

  <link rel="alternate" type="application/atom+xml"
   href="/atom.xml">

The only difference is "; type=entry", which I'm betting a lot of clients don't pay attention to.

The Atom entries then can have an element::

  <link rel="edit" href="this-url"  />

This is a location where you can PUT a new entry to update the resource.  You could allow the client to PUT directly over the old page, or use ``this-url?format=atom`` or whatever is convenient on the server-side.  Additionally, DELETE to the same URL would delete.

This handles updates and deletes, and single-page reads.  The next issue is creating pages.

Atompub makes creation fairly simple.  First you have to get the `Atompub service document <http://bitworking.org/projects/atom/rfc5023.html#appdocs>`_.  This is a document with the type ``application/atomsvc+xml`` and it gives the collection URL.  `It's suggested <http://wiki.whatwg.org/wiki/ServiceRelExtension>`_ you make this document discoverable like::

  <link rel="service" type="application/atomsvc+xml"
   href="/atomsvc.xml">

This document then points to the "collection" URL, which for our purposes is where you create documents.  The service document would look like::

  <service xmlns="http://www.w3.org/2007/app"
           xmlns:atom="http://www.w3.org/2005/Atom">
    <workspace>
      <atom:title>SITE TITLE</atom:title>
      <collection href="/atomapi">
        <atom:title>SITE TITLE</atom:title>
        <accept>*/*</accept>
        <accept>application/atom+xml;type=entry</accept>
      </collection>
    </workspace>
  </service>

Basically this indicates that you can POST any media to ``/atomapi`` (both Atom entries, and things like images).

To create a page, a client then does a POST like::

  POST /atomapi
  Content-Type: application/atom+xml; type=entry
  Slug: /page/path

  <entry xmlns="...">...</entry>

There's an awkwardness here, that you can suggest (via the Slug header) what the URL for the new page is.  The client can find the actual URL of the new page from the Location header in the response. But the client can't demand that the slug be respected (getting an error back if it is not), and there's lots of use cases where the client doesn't just want to *suggest* a path (for instance, other documents that are being created might rely on that path for links).

Also, "slug" implies... well, a slug.  That is, some path segment probably derived from the title.  There's nothing stopping the client from putting a complete path in there, but it's very likely to be misinterpreted (e.g. translating ``/page/path`` to ``/2009/01/pagepath``).

Bug I digress.  Anyway, you can post every resource as an entry, base64-encoding the resource body, but Atompub also allows POSTing media directly.  When you do that, the server puts the media somewhere and creates a simple Atom entry for the media.  If you wanted to add properties to that entry, you'd edit the entry after creating it.

The last missing piece is how to get a list of all the pages on a site.  Atompub *does* have an answer for this: just ``GET /atomapi`` will give you an Atom feed, and for our purposes we can demand that the feed is complete (using paging so that any one page of the feed doesn't get too big).  But this doesn't seem like a good solution to me.  `GData <http://code.google.com/apis/gdata/overview.html>`_ specifies a useful set of queries to for feeds, but I'm not sure that this is very useful here; the kind of queries a client needs to do for this use case aren't things GData was designed for.

The queries that seem most important to me are queries by page path (which allows some sense of "collections" without being formal) and by content type.  Also to allow incremental updates on the client side, filtering these queries by last-modified time (i.e., all pages created since I last looked).  Reporting queries (date of creation, update, author, last editor, and custom properties) of course *could* be useful, but don't seem as directly applicable.

Also, often the client won't want the complete Atom entry for the pages, but only a list of pages (maybe with minimal metadata).  I'm unsure about the validity of abbreviated Atom entries, but it seems like one solution.  Any Atom entry can have something like::

  <link rel="self" type="application/atom+xml; type=entry"
   href="url?format=atom"  />

This indicates where the entry exists, though it doesn't suggest very forcefully that the actual entry is abbreviated.  Anyway, I could then imagine a feed like::

  <feed>
    <entry>
      <title>the page title</title>
      <content type="some/content-type"  />
      <link rel="self" href="..."  />
      <updated>YYYYMMDDTHH:MM:SSZ</updated>
    <entry>
    ...
  </feed>

This isn't entirely valid, however -- you can't just have an empty ``<content>`` tag.  You can use a ``src`` attribute to use indirection for the content, and then add Yet Another URL for each page that points to its raw content.  But that's just jumping through hoops.  This also seems like an opportunity to suggest that the entry is incomplete.

To actually construct these feeds, you need some way of getting the feed.  I suggest that another entry be added to the Atompub service document, something like::

  <cmsapi:feed href="URI-TEMPLATE"  />

That would be a `URI Template <http://bitworking.org/projects/URI-Templates />`_ that accepted several known variables (though frustratingly, URI Templates aren't properly standardized yet).  Things like:

* ``content-type``: the content type of the resource (allowing wildcards like ``image/*``)
* ``container``: a path to a container, i.e., ``/2007`` would match all pages in ``/2007/...``
* ``path-regex``: some regular expression to match the paths
* ``last-modified``: return all pages modified at the given date or later

All parameters would be ANDed together.

So, open issues:

* How to strongly suggest a path when creating a resource (better than Slug)
* How to rename (move) or copy a page (it's easy enough to punt on copy, but I'd rather move by a *little* more formal than just recreating a resource in a new location and deleting the original)
* How to represent abbreviated Atom entries

With these resolved I think it'd be possible to create a much simpler API than WebDAV, and one that can be applied to existing applications much more easily.  (If you think there's more missing, please comment.)
