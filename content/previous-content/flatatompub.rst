FlatAtompub
###########
:date: 2007-09-12 20:50
:author: Ian Bicking
:tags: Programming, Python, Web

A little while ago I decided to whip up a small `Atompub <http://atompub.org />`_ server to get my head around the Atom Publishing Protocol.  I called it FlatAtomPub because it was just storing stuff in flat files.  I'm not committing to that name.  It was also a chance to kick the tires on `WebOb <http://pythonpaste.org/webob />`_.

What I take out of the process:

* `APE <http://www.tbray.org/ape />`_ was very handy.  I lazily did   very little unit testing, instead relying on APE to do the work for   me.  This seemed to work quite well.  It is fun doing test driven   development when someone else develops the tests.

* I wrote a `little decorator   <http://svn.pythonpaste.org/Paste/apps/FlatAtomPub/trunk/flatatompub/dec.py>`_   that serves as a kind of framework.  It worked pretty well, I think.   This might be the prototype of what the   ``PylonsController.__call__`` method does in some WebOb-using   future.

* Stuff like conditional requests and responses are mostly implemented   in WebOb itself, which works well.  HTTP is clear about how   conditional requests work, so if you can just setup the basic info   (ETag, Last-Modified) you can let the library handle the rest.  I   could probably save a little work by paying closer attention to   ETags and Last-Modified up-front, but since there's no complicated   template rendering the work saved doesn't seem significant.

* The `atom library   <https://svn.openplans.org/svn/TaggerClient/trunk/taggerclient/atom.py>`_   removed most concern about the XML itself.

* I don't know what to with `collections   <http://bitworking.org/projects/atom/draft-ietf-atompub-protocol-17.html#rfc.section.8.3.3>`_.   I guess I could allow multiple collections via configuration.  If   the store wasn't a dumb store (e.g., it was plugged directly into a   blog, it didn't just passively store things) it would be clearer   what a collection would mean.  As it is, collections are just a way   of aggregating multiple Atompub servers into one service document,   which doesn't seem very useful.

* Handling links and slugs is kind of annoying.  I took the lazy way   out for this, using relative links and treating the slug and link as   the same thing.  This isn't a good long-term solution, as it can   mess things up if you start handing entries around, or worse move a   server, and I don't even set ``xml:base`` on elements.  In theory   it should all work, but it makes the client do more effort than I   would like.  On the other hand, I suppose a client *should* do that   extra work anyway, as it shouldn't rely on the server not being   lazy.  So maybe I'm better off sticking with a lazy solution, and   making sure I work with non-lazy clients.

* I considered pluggable storage, but ultimately decided it didn't   matter.  Storing entries in files is fine; files are easy, and they   work.  I put in pluggable indexing instead.  `Amplee   <http://trac.defuze.org/wiki/amplee>`_ is another Python Atompub   server, and I looked at `Amplee storage backends   <https://svn.defuze.org/oss/amplee/amplee/storage />`_.  It's kind of   clever to have things like svn or S3 backends.  But I'm not sure   what use I'd actually *do* with that.

* I haven't yet considered transactions; if something fails part way   through, stuff will be inconsistent.  Admittedly this is where files   make things harder.  Probably a clear way to re-index would be   useful too, as at least there's a clear location for the canonical   data (the files).

* The dependencies are still a little tangled; even though the library   doesn't *use* a great deal of stuff, there's enough pieces that some   people have had a hard time getting it setup.

* Ignoring authentication is nice.  I should see what it takes to   setup some authentication, but implementing it directly is out of   scope for FlatAtomPub.

Interested people can look at the `svn repository <http://svn.pythonpaste.org/Paste/apps/FlatAtomPub/trunk>`_.

This makes me wonder how hard WebDAV would be...
