Javascript on the server AND the client is not a big deal
#########################################################
:date: 2011-03-30 16:09
:author: Admin
:tags: Javascript, Programming, Web

All the cool kids love `Node.js <http://nodejs.org />`_.  I've used it a little, and it's fine; I was able to do what I wanted to do, and it wasn't particularly painful.  It's fun to use something new, and it's relatively straight-forward to get started so it's an *emotionally satisfying* experience.

There are several reasons you might want to use Node.js, and I'll ignore many of them, but I want to talk about one in particular:

    Javascript on the client and the server!

Is this such a great feature?  I think not...

You only need to know one language!
-----------------------------------

Sure.  Yay ignorance!  But really, this is *fine* but unlikely to be relevant to any current potential audience for Node.js.  If you are shooting for an very-easy-to-learn client-server programming system, Node.js isn't it.  Maybe `Couch <http://couchapp.org />`_ or something similar has that potential?  But I digress.

It's not easy to have expertise at multiple languages.  But it's not *that hard*.  It's considerably harder to have expertise at *multiple platforms*.  Node.js gives you one language across client and server, but *not* one platform.  Node.js programming doesn't *feel* like the browser environment.  They do adopt many conventions when it's reasonable, but even then it's not always the case -- in particular because many browser APIs are the awkward product of C++ programmers exposing things to Javascript, and you don't want to reproduce those same APIs if you don't have to (and Node.js doesn't have to!) -- an example is the event pattern in Node, which is similar to a browser but less obtuse.

You get to share libraries!
---------------------------

First: the same set of libraries is probably not applicable.  If you can do it on the client then you probably don't *have* to do it on the server, and vice versa.

But sometimes the same libraries are useful.  Can you really share them?  Browser libraries are often hard to use elsewhere because they rely on browser APIs.  These APIs are frequently *impossible to implement in Javascript*.

Actually they are possible to implement in Javascript using `Proxies <https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Proxy>`_ (or maybe some other new and not-yet-standard Javascript features). But not in Node.js, which uses V8, and V8 is a pretty conservative implementation of the Javascript language. (**Update**: `it is noted <https://ianbicking.org/2011/03/30/js-on-server-and-client-is-not-a-big-deal/comment-page-1/#comment-194005>`_ that you can `implement proxies <https://github.com/isaacs/node-proxy/tree/master/src>`_ -- in this case a C++ extension to Node)

Besides these unimplementable APIs, it is also just a different environment.  There is the trivial: the ``window`` object in the browser has a Node.js equivalent, but it's not named ``window``. Performance is different -- Node has long-running processes, the browser *might*.  Node can have blocking calls, which are useful even if you can't use them at runtime (e.g., ``require()``); but you can't really have any of these at any time on the browser.  And then of course all the system calls, *none* of which you can use in the browser.

All these may simply be surmountable challenges, through modularity, mocking, abstractions, and so on... but ultimately I think the motivation is lacking: the domain of changing a live-rendered DOM isn't the same as producing bytes to put onto a socket.

You can work fluidly across client and server!
----------------------------------------------

If anything I think this is *dangerous* rather than *useful*.  The client and the server are different places, with different expectations.  Any vagueness about that boundary is *wrong*.

It's wrong from a security perspective, as the security assumptions are nearly opposite on the two platforms.  The client trusts itself, and the server trusts itself, and both should hold the other in suspicion (though the client can be more trusting because the *browser* doesn't trust the client code).

But it's also the wrong way to treat HTTP.  HTTP is pretty simple until you try to make it simpler.  Efforts to make it simpler mostly make it more complicated.  HTTP lets you send serialized data back and forth to a server, with a bunch of metadata and other do-dads.  And that's all neat, but you should always be thinking about *sending* information.  And never *sharing* information.  It's not a fluid boundary, and code that touches HTTP needs to be explicit about it and not pretend it is equivalent to any other non-network operation.

Certainly you don't *need* two implementation languages to keep your mind clear.  But it doesn't hurt.

You can do validation the same way on the client and server!
------------------------------------------------------------

One of the things people frequently bring up is that you can validate data on the client and server using the same code.  And of course, what web developer hasn't been a little frustrated that they have to implement validation twice?

Validation on the client is primarily a *user experience* concern, where you focus on bringing attention to problems with a form, and helping the user resolve those problems.  You may be able to avoid errors entirely with an input method that avoids the problem (e.g., if a you have a slider for a numeric input, you don't have to worry about the user inputing a non-numeric value).

Once the form is submitted, if you've done thorough client-side validation you can also avoid *friendly* server-side validation.  Of course all your client-side validation could be avoided through a malicious client, but you don't need to give a friendly error message in that case, you can simply bail out with a simple 400 Bad Request error.

At that point there's not much in common between these two kinds of validation -- the client is all user experience, and the server is all data integrity.

You can do server-side Javascript as a fallback for the client!
---------------------------------------------------------------

Writing for clients without Javascript is becoming increasingly less relevant, and if we aren't *there* yet, then we'll certainly *get there* soon.  It's only a matter of time, the writing is on the wall. Depending on the project you might have to put in workarounds, but we should keep those concerns out of architecture decisions.  Maintaining crazy hacks is *not* worth it. There's so many terrible hacks that have turned into frameworks, and frameworks that have justified themselves because of the problems they solved that no longer matter... Node.js deserves better than to be one of those.

In Conclusion Or Whatever
-------------------------

I'm not saying Node.js is *bad*.  There are other arguments for it, and you don't need to make *any* argument for it if you just feel like using it.  It's fun to do something new.  And I'm as optimistic about Javascript as anyone.  But this one argument, I do not think it is very good.
