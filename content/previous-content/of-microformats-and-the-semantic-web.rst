Of Microformats and the Semantic Web
####################################
:date: 2007-08-14 11:52
:author: Ian Bicking
:tags: Programming, Web

I was talking a little with `Daniel Krech <http://eikeon.com />`_ (author of `rdflib <http://rdflib.net />`_) about Semantic Web stuff and `microformats <http://microformats.org />`_ and what they all mean. And he was saying that microformats were nice, because you could *do* something with them, but it would be nice to see that generalized.

By "generalized" I think he meant a general way of expressing arbitrary relationships.  As an example, in `hCard <http://microformats.org/wiki/hcard>`_ you can do:

.. code:: html

    <span class="tel">
      <span class="type">home</span>:
      <span class="value">773-555-3821</span>
    </span>

The hCard specification (itself leaning heavily on vCard) defines ``tel``, ``type``, and there's a general pattern of what ``value`` means.  But if you want to describe some new kind of structure, there's no way to do that really; there's no marital status format, for instance (which would be useful for a singles search engine, as an example).

So I started thinking: can you really generalize it?  And I started to think about `Joe Gregorio's attack of WADL <http://bitworking.org/news/193/Do-we-need-WADL>`_:

    Here is the very `first example in the WADL specification     <http://bitworking.org/projects/pastebin/main.cgi/bin/7>`_.

    That WADL file is a description of a search interface. But `here     is how you should really do it     <http://bitworking.org/projects/pastebin/main.cgi/bin/8>`_. That's     an `OpenSearch <http://www.opensearch.org/Home>`_ document, that     also describes a search interface.

    **Q**: What's the difference?

    **A**: A mime-type.

    **Q**: That doesn't seem like much, does it make a difference?

    **A**: Yes, it makes a big difference. When you get an OpenSearch     document there is a whole data model and a set of interactions you     know are possible because you read the OpenSearch     specification. By reading that spec you know how to construct     search queries. When I get a WADL document it might describe     anything, from how to construct a search, to the `APP     <http://bitworking.org/projects/atom />`_, to `JEP     <http://bitworking.org/news/JEP>`_, to XML-RPC.

    ...

    So when I say the difference is a 'mime-type', what I mean is that     there is an entire spec somewhere which describes what that     document means, and that meaning may include hypertext     functionality, ala (X)HTML, XForms, and OpenSearch.

This made me think of shared understanding more than explicit descriptions.  OpenSearch, APP, and Atom are very well described, but I think that's only half of it: they are useful when they describe something that many people already understand.

Digressing slightly, one "semantic markup" ideal that still bugs me is ``<strong>`` and ``<em>`` vs. ``<b>`` and ``<i>``.  When I compose text I choose to make some words bold and some italic.  I have no idea what "strong" and "emphasis" are even supposed to mean.  When I'm composing text, I don't actually know *why* I choose one or the other.  If I sat down and thought about it I'm sure I could come up with a set of rules that describe when bold is appropriate and when italic is appropriate.  But that is reflecting on my choice, it is not describing my choice.  There is no intermediate semantic meaning between what I am saying and bold and italic.  I *think* in bold and italic.  Readers in turn find meaning in the text itself; they do not parse my writing into semantic markup in their brain.

I think there's some connection between this and the shared understanding that microformats represents, and a more generalized RDF model does not represent.  I know what hCard means; not just in an intellectual way, but I can imagine a dozen functional uses of it without hardly trying, and of course I am entirely clear on what contact information *means*.  Moreover, I know what it means without actually figuring out what it means; if you asked me to articulate what contact information means I'd have to think a little, and I'm sure many people would come up with bad answers or be stumped.  And yet they all actually understand what it means.

Bringing this back to Joe's post, if I write something that produces or consumes Atom, Atompub, or OpenSearch, I understand the *why* of my code.  With both WADL and RDF my code is divorced of the why.  This isn't about my personal understanding either; explaining it to *me* doesn't serve any purpose, because with any exchange format it has to make sense to many many people to be useful.  Even an education campaign won't fix this: education by description is far inferior to education by doing, and there's no "doing" to WADL and RDF right now.

That said, what is sufficiently obvious in the future may not be obvious now.  Maybe we'll all get smarter.  Maybe someone will pioneer this stuff in a way that is really useful (Facebook?), and grow the public's intuition about describing relationships in an abstract way. But *until then* I think microformats are going about this the right way, describing those things that are most easily describable.
