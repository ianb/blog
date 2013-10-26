Javascript Status Message Display
#################################
:date: 2008-12-17 12:03
:author: Ian Bicking
:tags: Javascript, Programming, Web

In a `little wiki I've been playing with <http://www.bitbucket.org/ianb/pickywiki />`_ I've been trying out little ideas that I've had but haven't had a place to actually implement them.  One is how notification messages work.  I'm sure other people have done the same thing, but I thought I'd describe it anyway.

A `common pattern <http://blog.ianbicking.org/web-application-patterns-status-notification.html>`_ is to accept a POST request and then redirect the user to some page, setting a status message.  Typically the status message is either set in a cookie or in the session, then the standard template for the application has some code to check for a message and display it.

The problem with this is that this breaks all caching -- at any time any page can have some message injected into it, basically for no reason at all.  So I thought: why not do the whole thing in Javascript?  The server will set a cookie, but only Javascript will read it.

The code goes like this; on the server (easily translated into any framework)::

    resp.set_cookie('flash_message', urllib.quote(msg))

I quote the message because it can contain characters unsafe for cookies, and URL quoting is a particularly easy quoting to apply.

Then I have this Javascript (using jQuery)::

    $(function () {
        // Anything in $(function...) is run on page load
        var flashMsg = readCookie('flash_message');
        if (flashMsg) {
            flashMsg = unescape(flashMsg);
            var el = $('<div id="flash-message">'+
              '<div id="flash-message-close">'+
              '<a title="dismiss this message" '+
              'id="flash-message-button" href="#">X</a></div>'+
              flashMsg + '</div>');
            $('a#flash-message-button', el).bind(
              'click', function () {
                $(this.parentNode.parentNode).remove();
            });
            $('#body').prepend(el);
            eraseCookie('flash_message');
        }
    });

Note that I've decided to treat the flash message as HTML.  I don't see a strong risk of injection attack in this case, though I must admit I'm a little unclear about what the normal policies are for cross-domain cookie setting.

I use `these cookie functions <http://www.quirksmode.org/js/cookies.html>`_ because oddly I can't find cookie handling functions in jQuery.  It's always weird to me how primitive ``document.cookie`` is.  Anyway, CSS looks like this::

    #flash-message {
      margin: 0.5em;
      border: 2px solid #000;
      background-color: #9f9;
      -moz-border-radius: 4px;
      text-align: center;
    }

    #flash-message-close {
      float: right;
      font-size: 70%;
      margin: 2px;
    }

    a#flash-message-button {
      text-decoration: none;
      color: #000;
      border: 1px solid #9f9;
    }

    a#flash-message-button:hover {
      border: 1px solid #000;
      background-color: #009;
      color: #fff;
    }

This doesn't have non-Javascript fallback, but I think that's okay.  This isn't something that a spider would ever see (since spiders shouldn't be submitting forms that result in update messages).  Accessible browsers generally implement Javascript so that's also not particularly a problem, though there may be additional hints I could give in CSS or Javascript to help make this more readable (if there's a message, it should probably be the first thing read on the page).

Another common component of pages that varies separate from the page itself is logged-in status, but that's more heavily connected to your application.  Get both into Javascript and you might be able to turn caching way up on a lot of your pages.
