Atompub & OpenID
################
:date: 2007-08-06 11:38
:author: Ian Bicking
:tags: Javascript, Programming, Web

One of the thinmgs I would like to do is to interact with `Atompub (aka Atom Publishing Protocol) <http://atompub.org/rfc4287.html>`_ stores in Javascript through the browser.  Since this effectively the browser itself interacting with the Atompub server, browser-like authentication methods would be nice.  But services like Atompub don't work nicely with the kinds of authentication methods that normal websites use.  One of these is `OpenID <http://openid.net />`_, which is particularly browser-focused.

From the perspective of a client, OpenID basically works like this:

* You need to login.  You tell the original server what your OpenID   URL is, somehow.  
* The original server does some redirects, maybe some popups, etc.
* Your OpenID server (attached to your OpenID URL) authenticates you   in some fashion, and then tells the original server.
* The original server probably sets a signed cookie so that in   subsequent requests you stay logged in.  You cannot do this little   redirection dance for every request, since it's actually quite   intrusive.

So what happens when I have an XMLHttpRequest that needs to be authenticated?  Neither the XMLHttpRequest nor Javascript generally can do the authentication.  Only the browser can, with the user's interaction.

One thought I have is a 401 Unauthorized response, with a header like::

    WWW-Authenticate: Cookie location="http://original.server/login.html"

Which means I need to open up ``http://original.server/login.html`` and have the user log in, and the final result is that a cookie will be set.  XMLHttpRequest sends cookies automatically I believe, so once the browser has the cookie then all the Javascript requests get the same cookie and hence authentication.

One problem, though, is that you have to wait around for a while for the login to succede, then continue on your way.  A typical situation is that you have to return to the original page you were requesting, and people often do something like ``/login?redirect_to=original_url``.  In this case we might want something like ``/login?opener_call=reattempt_request``, where when the login process is over we call ``window.opener.reattempt_request()`` in Javascript.

Maybe it would make sense for that ``location`` variable to be a `URI Template <http://bitworking.org/projects/URI-Templates/draft-gregorio-uritemplate-01.html>`_, with some predefined variables, like opener, back, etc.

For general backward compatibility, would it be reasonable to send 307 Temporary Redirect plus WWW-Authenticate, and let XMLHttpRequests or other service clients sort it out, while normal browser requests do the normal login redirect? 

**Update:** Another question/thought: is it okay to send multiple WWW-Authenticate headers, to give the client options for how it wants to do authentication?  It seems vaguely okay, according to `RFC 2616 14.47 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.47>`_.
