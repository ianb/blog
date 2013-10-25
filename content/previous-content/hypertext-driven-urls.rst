Hypertext-driven URLs
#####################
:date: 2008-10-24 12:03
:author: Ian Bicking
:tags: Programming, Web

Roy T. Fielding, author of the `REST thesis <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`_ wrote an article recently: `REST APIs must be hypertext-driven <http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven>`_.  I liked this article, it fit with an intuition I've had.  Then he wrote an article `explaining that he wouldn't really explain the other articles <http://roy.gbiv.com/untangled/2008/specialization>`_ because, I guess, he wanted a conversation with the specialists, and it seems like a kind of invitation to reinterpret his writing.  So `since others <http://www.25hoursaday.com/weblog/2008/10/24/RESTAPIDesignInventMediaTypesNotProtocolsAndUnderstandTheImportanceOfHyperlinks.aspx>`_ `are doing it <http://blog.whatfettle.com/2008/10/21/what-i-believe-roy-said />`_ I figured I'd do it too.

I'd summarize his argument thus:

* Focus on media types, i.e., resource formats, i.e., document formats.  The protocol will flow from these if they are well specified.

* URL structures are not a media type.  They are some kind of server layout.  You can't hold them, you can't pass them around, there is no notion of CRUD.  Media types have all sorts of advantages that URL structures do not.

An example of a protocol based on a URL structure would be something like:

* Do ``GET /articles/`` to get a JSON list of all the article ids, with a response like ``[1, 2, 3]``
* Do a ``GET /articles/{id}`` to get the representation of a specific article.

JSON is a reasonable structure for a media type.  It is not *itself* a fully explained type, because it's just a container for data, just like XML.  In this example you have a document, ``[1, 2, 3]`` which isn't self-describing and just isn't very useful.  A more appropriate protocol would be:

* You start with a container, in our example ``/articles/``.  Do ``GET /articles/`` to get a JSON document listing the URLs of all the articles.  These URLs are relative to the container URL.  You'll get a response like ``['./1', './2', './3']`` (actually ``['1', '2', '3']`` would be fine too).
* Do ``GET {article-url}`` to get the article representation.

It's a small difference.  Heck, the communication could look identical in practice, but by putting **URLs** in the JSON document instead of this abstract "id" notion you've created a more flexible and self-describing system.  You could probably give a name to that list of URLs, and then just talk about that name.

An example in `Atompub <http://www.atompub.org />`_ is `rel="edit" <http://bitworking.org/projects/atom/rfc5023.html#memuri>`_.  An Atom entry can look like::

    <entry>...
      <link rel="edit" href="/post/15"  />
    </entry>

Instead of the client just somehow *knowing* where to go to edit an entry, it's made explicit.  Thus you can move the entry around, while still pointing back to the canonical location to edit that entry.

There's nothing really that complicated about this, the rule is really quite simple: link to other things, don't just expect the client to know or guess where those other things are.

For a more concrete example of where this linking works well, OpenID uses ``<link rel="openid.server" href="...">`` and ``<link rel="openid.delegate" href="...">``, which allows you to add a little information to any HTML homepage so that the login can happen at a third location.  If OpenID used something like looking at ``{homepage}/openid`` for a OpenID server then you couldn't select whatever OpenID service you liked, or change services, or apply OpenID to hosted locations where you couldn't install an OpenID server.

I'll add my own little opinion in here: this is why the URL structure of applications doesn't affect their RESTfulness, nor is URL structure all that important of a concern generally.  Pretty URL structures are a nice thing to do, like indenting your code in a pleasant way, but it has nothing to do with your API, and if you can't use a crappy URL structure with that same API then probably something is wrong with that API.
