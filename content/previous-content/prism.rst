Prism
#####
:date: 2007-10-25 17:30
:author: Ian Bicking
:tags: Javascript, Web

I've seen talk of `MS Silverlight <http://en.wikipedia.org/wiki/Silverlight>`_ and `Adobe AIR <http://en.wikipedia.org/wiki/Adobe_AIR>`_.  People talk them up like the future of web applications or something.  I don't know *much* about them, but I almost completely certain I don't want anything to do with them.

Here's a general rule I have: I don't accept anything made by people who hate the web.  If you hate the web and you want to improve the web, I don't want anything to do with you.  If you think the web is some kind of *implementation detail* then I probably don't care what you are doing.  If you *still* think the web is a fad, then you are just nuts; if all you can think of is reasons why the web is stupid and awkward, and you think it's some giant step backward (from what?), then you haven't thought very deeply about what's happened in the world of technology and why.

To me Silverlight and AIR reek of a distaste for the web.

So it is with great delight that I read the `announcement of Mozilla Prism <http://labs.mozilla.com/2007/10/prism />`_: a bridge between the desktop and the web, written by people who don't hate the web.

The premise of Prism from what I can tell is this: to make a web application into a desktop application, you just give the browser a shallowly separate identity.  It lives in its own window, has its own icon, it's own launcher.  Maybe runs in its own process for reliability.  You take away the chrome (URL bars, back button, etc).  Unlike previous ideas for Mozilla (like `xulrunner <http://developer.mozilla.org/en/docs/XULRunner>`_) you *don't* add chrome back in with `XUL <http://en.wikipedia.org/wiki/XUL>`_, you just write all the controls with HTML and Javascript.

All the things that Prism *isn't* is what makes it great, because it's so damn *simple*.  The only thing that really seems weird to me is that it is very separate from the browser itself; hopefully this is just temporary, and by the time it's really "done" you'll be able to just make any page an application directly from Firefox.

This doesn't make web applications perfect, of course.  There's the offline issue.  There's usability issues, like keybindings.  There's lots of issues, but all of those issues apply just as much to the web as to a desktop application, and should be solved both places.  Those things can be worked on orthogonally (most interestingly in `Web Forms 2.0 <http://www.whatwg.org/specs/web-forms/current-work />`_ and `Web Applications 1.0 <http://www.whatwg.org/specs/web-apps/current-work />`_ at `WHAT-WG <http://www.whatwg.org />`_).  Still, HTML and Javascript *right now* are totally workable for most applications.
