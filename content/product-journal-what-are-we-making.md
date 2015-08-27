Title: A Product Journal: What Are We Making?
Slug: product-journal-what-are-we-making
Category: mozilla
Tags: product-journal
Date: 2015-04-21

> I'm blogging about the development of a new product in Mozilla, [look here for my other posts in this series](http://www.ianbicking.org/tag/product-journal.html)

I've managed to mostly avoid talking about what we're making here.  Perhaps shyness, we (the PageShot team) don't yet know where it's going, or if we'll manage to get this into Firefox.

We are making a tool for sharing on the web.  This tool creates a new kind of *thing* to share, it's not a communication medium of any kind.  We're calling it **PageShot**, similar to a screenshot but with all the power we can add to it since web pages are much more understandable than pixels.  (The things it makes we call a **Shot**.)

The tool emphasizes sharing clips or highlights from pages.  These can be screenshots (full or part of the screen) or text clippings.  Along with those clips we keep an archival copy of the entire web page, preserving the full context of the page you were looking at and the origin of each clip.  Generally we try to save as much information and context about the page as we can.  We are trying to avoid *choices*, the burdensome effort to decide what you might want in the future.  The more effort you put into using this tool, the more information or specificity you can add to your Shot, but we do what we can to save *everything* so you can sort it out later if you want.

I mentioned [earlier](http://www.ianbicking.org/blog/2015/01/product-journal-conception.html) that I started this idea thinking about how to make use of frozen copies of the DOM.  What we're working on now looks much more like a screenshotting tool that happens to keep this copy of the page.  This changed happened in part because of [user research done at Mozilla](https://blog.mozilla.org/ux/2015/02/save-share-revisit/) around saving and sharing, where I became aware of just how prevalent screenshots had become to many people.

<figure style="float: right; background-color: rgba(240, 240, 240, 0.4); padding: 5px; width: 50%; border: 1px solid #aaa; border-radius: 3px;"><a href="/static/media/pageshot-early-screenshot.png"><img style="width: 100%; height: auto" src="/static/media/pageshot-early-screenshot.png" /></a><figcaption style="font-size: 80%; line-height: 1em; text-align: center;">The current (rough) state of the tool</figcaption></figure>

It's not hard to understand the popularity of screenshots, specifically on mobile devices.  iPhone users at least have mostly figured out screenshotting, functionality that remains somewhat obscure on desktop devices (and for the life of me I can't get my Android device to make a screenshot).  Also screenshots are the one thing that works across applications – even with an application that supports sharing, you don't really know what's going to be shared, but you know what the screenshot will contain.  You can also share screenshots with confidence: the recipient won't have to log in or sign up, they can read it on any device they want, once it has arrived they don't need a network connection.  Screenshots are a reliable tool.  A lesson I try to regularly remind myself of: availability beats fidelity.

In a similar vein we've seen the rise of the animated gif over the video (though video resurging now that it's *just a file* again), and the smuggling in of long texts to Twitter via images.

A lot of this material moves through communication mediums via links and metadata, but those links and metadata are generally under the control of site owners.  It's up to the site owner what someone sees when they click a link, it's up to them what the metadata will suggest go into the image previous and description.  PageShot gives that control to the person sharing, since each Shot is *your link*, your copy and your perspective.

As of this moment (April 2015) our designs are still ahead of our implementation, so there's not a lot to try out at this moment, but this is what we're putting together.

If you want to follow along, check out the [repository](https://github.com/mozilla-services/pageshot).
