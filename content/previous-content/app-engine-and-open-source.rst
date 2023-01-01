App Engine and Open Source
##########################
:date: 2008-04-09 13:13
:author: Ian Bicking
:tags: Programming, Python, Web

This is about `Google App Engine <http://code.google.com/appengine />`_ which probably everyone has read about already.

I'm quite excited about it.  Hosting has been the bane of the Python web world for a long time.  This provides a very compelling hosting situation for Python applications.

I'm not as interested in this from a competitive perspective as I am from a simple this-is-awesome perspective.  Regardless of how this positions Python relative to other languages, this is something Python needs.  But even looking beyond that, I think this is something the open source world needs.  Open source web development is in a funny place.  There's a lot of reasons why web programming is a good domain for open source.  The barrier to entry for web development is extremely low.  Developers have choice in their tools, as browsers don't really care what software you use so long as you serve up HTML.  This leads to experimentation and excitement and the kind of self-direction that is very motivating to developers.  It leads to the kind of personal excitement that underlies most open source development.

Despite this, open source web application development doesn't seem sustainable.  There's *some* applications, sure.  WordPress, Trac, MediaWiki, MoinMoin.  But most wiki software doesn't have a vibrant community.  Many a bug tracker has fallen by the wayside.  Blog software projects have a horrible time building a viable community.  Other website software hardly gets anywhere at all.  A lot of the development that might *appear* to be application development really is more like a framework when you look closely (e.g., Plone, Drupal).

I think deployment concerns are a huge part of this.  And, `given its better deployment story <http://ianbicking.org/2008/01/12/what-php-deployment-gets-right />`_, it's no surprise PHP is the basis of most viable open source web applications.  Being interested in a project requires that you be able to *use* the product (and usually use it casually, as that's the point of entry for many developers).  Right now most people can't use open source web applications.

But people *can use* hosted applications, and that's where all the effort has gone in the past few years.  I am comfortable saying that Trac is a better issue tracker than Google Code's issue tracker.  But I'd probably recommend Google Code to someone starting a new project, because it's so much less work.  Similarly I'd try to dissuade most people from installing their own blog software.  I still don't know what to tell people about a CMS.

Many people are excited about how far up you might be able to scale something based on App Engine, but (like `Dave <http://www.scripting.com/stories/2008/04/08/earlyNotesOnGoogleapps.html>`_) I'm excited about how far it could be scaled down.  For the majority of sites the free quota will be more than enough.  But that alone isn't the point: there's lots of free services people can use.  The difference here is that the free services can be modified and controlled by the anyone who signs up and installs an application.

From the perspective of open source it's a bit awkward that the platform itself is proprietary.  `Questions about sharecropping are a valid concern <http://www.tbray.org/ongoing/When/200x/2008/04/09/Google-Users-API>`_, but I'm optimistic about the ultimate outcome.  The SDK is under a permissive open source license, and the APIs are all reasonable enough that they could be reimplemented with open source backends (maybe without the same scalability, but that's not the aspect I care about anyway).  Perhaps the BigTable APIs will serve as the `basis for future storage APIs <http://radian.org/notebook/google-datastore>`_.

But even if other people make compatible implementations of these APIs, would it matter?  If Google offers free hosting, is someone else really going to be able to provide a better hosting option?  Or would these other implementations just be strawmen, a way to show that It Could Be Done?  If the libraries are just written to prove a point, I can't see them gaining much traction.  But I think these could be viable as there are other constraints to the App Engine environment that people may want to escape at some point in their application development.

As to the details of App Engine?  Can you run Pylons or Paste on it?  Well, that's a topic for another post.

**Update:** I `wrote up some more thoughts <https://ianbicking.org/2008/04/09/app-engine-commodity-vs-proprietary />`_
