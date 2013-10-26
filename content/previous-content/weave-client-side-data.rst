Weave: valuable client-side data
################################
:date: 2010-02-06 17:03
:author: Ian Bicking
:tags: HTML, Web

I've been looking at `Weave <https://mozillalabs.com/weave />`_ some lately.  The large-print summary on the page is *Synchronize Your Firefox Experience Across Desktop and Mobile*.  Straight forward enough.

Years and years ago I stopped really using bookmarks.  You lose them moving from machine to machine (which Weave could help), but mostly I stopped using them because it was too hard to (a) identify interesting content and place it into a taxonomy and (b) predict what I would later be interested in.  If I wanted to refer to something I'd seen before there's a good chance I wouldn't have saved it, while my bookmarks would be flooded with things that time would show were of transient interest.

So... synchronizing bookmarks, eh.  Saved form data and logins?  Sure, that's handy.  It would make browsing on multiple machines *nicer*.  But it feels more like a handy tweak.

All my *really* useful data is kept on servers, categorized and protected by a user account.  Why is that?  Well, of course, where else would you keep it?  In cookies?  Ha!

Why not in cookies?  So many reasons... because cookies are opaque and can't hold much data, can't be exchanged, and probably worst of all they just disappear randomly.

What if cookies weren't so impossibly lame for holding important data?  Suddenly sync seems much more interesting.  Instead of storing documents and data on a website, the website could put all that data right into your browser.  And conveniently `HTML 5 has an API for that <http://en.wikipedia.org/wiki/DOM_storage>`_.  Everyone thinks about that API as a way of handling off-line caching, because while it handles many problems with cookies it doesn't handle the problem of data disappearing as you move between computers and browser.  That's where Weave synchronization could change things.  I don't think this technique is something appropriate for every app (maybe not most apps), but it could allow a new class of applications.

Advantages: web development and scaling becomes easy.  If you store data in the browser scaling is almost free; serving static pages is a Solved Problem.  Development is easier because development and deployment of HTML and Javascript is pretty easy.  Forking is easy -- just copy all the resources.  So long as you don't hardcode absolute links into your Javascript, you can even just save from the browser and get a working local copy of the application.

Disadvantages: another silo.  You might complain about Facebook keeping everyone's data, but the data in Facebook is *still* more transparent than data held in files or locally with a browser.  Let's say you create a word processor that uses local storage for all its documents.  If you stored that document online sharing and collaboration would be really easy; but with it stored locally the act of sharing is not as automatic, and collaboration is *very hard*.  Sure, the "user" is in "control" of their data, but that would be more true on paper than in practice.  Building collaboration on top of local storage is hard, and without that... maybe it's not that interesting?

Anyway, there is an interesting (but maybe Much Too Hard) problem in there.  (DVCS in the browser?)

**Update**: in `this video <http://www.azarask.in/blog/post/you-centric-a-sketch-of-the-future-of-browsers />`_ Aza talks about just what I talk about here.  A few months ago.  The Weave APIs also allude to things like this, including collaboration.  So... they are on it!
