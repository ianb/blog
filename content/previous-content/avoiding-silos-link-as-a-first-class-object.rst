Avoiding Silos: "link" as a first-class object
##############################################
:date: 2008-12-27 13:09
:author: Ian Bicking
:tags: HTML, Programming, Python, Web

One of the constant annoyances to me in web applications is the self-proclaimed need for those applications to know about everything and do everything, and only spotty ad hoc techniques for including things from other applications.

An example might be blog navigation or search, where you can only include data from the application itself.  Or "Recent Posts" which can only show locally-produce posts.  What if I post something elsewhere?  I have to create some shoddy placeholder post to refer to it.  Bah!  Underlying this the data is usually structured in a specific way, with the HTML being a sort of artifact of the database, the markup transient and a slave to the database's structure.

An example of this might be a recent post listing like::

  <ul>
    for post in recent_posts:
      <li>
        <a href="/post/{{post.year}}/{{post.month}}/{{post.slug}}">
          {{post.title}}</a>
      </li>
  </ul>

There's clearly no room for exceptions in this code.  I am thus proposing that any system like this should have the notion of a "link" as a first-class object.  The code should look like this::

  <ul>
    for post in recent_posts:
      <li>
        {{post.link()}}
      </li>
  </ul>

Just like with `changing IDs to links <http://blog.ianbicking.org/2008/10/24/hypertext-driven-urls />`_ in service documents, the template doesn't actually look any more complicated than it did before (simpler, even).  But now we can use simple object-oriented techniques to create first-class links.  The code might look like::

  class Post(SomeORM):
      def url(self):
          if self.type == 'link':
              return self.body
          else:
              base = get_request().application_url
              return '%s/%s/%s/%s' % (
                  base, self.year, self.month, self.slug)
          
      def link(self):
          return html('<a href="%s">%s</a>') % (
              self.url(), self.title)

The addition of the ``.url()`` method has the obvious effect of making these offsite links work.  Using a ``.link()`` method has the added advantage of allowing things like HTML snippets to be inserted into the system (even though that is not implemented here).  By allowing arbitrary HTML in certain places you make it possible for people to extend the site in little ways -- possibly adding markup to a title, or allowing an item in the list that actually contains two URLs (e.g., ``<a href="url1">Some Item</a> (<a href="url2">via</a>)``).

In the context of Python I recommend making these into methods, not properties, because it allows you to later add keyword arguments to specialize the markup (like ``post.link(abbreviated=True)``).

One negative aspect of this is that you cannot affect all the markup through the template alone, you may have to go into the Python code to change things.  Anyone have ideas for handling this problem?
