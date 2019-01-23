Title: A Product Journal: Objects
Slug: product-journal-objects
Category: mozilla
Tags: product-journal
Date: 2015-07-16

> I'm blogging about the development of a new product in Mozilla, [look here for my other posts in this series](http://www.ianbicking.org/tag/product-journal.html)

I've been reading the [Early History Of Smalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/), notes by Alan Kay, and [this](http://worrydream.com/EarlyHistoryOfSmalltalk/#coda) small note jumped out at me:

> Another late-binding scheme that is already necessary is to get away from direct protocol matching when a new object shows up in a system of objects. In other words, if someone sends you an object from halfway around the world it will be unusual if it conforms to your local protocols. At some point it will be easier to have it carry even more information about itself–enough so its specifications can be “understood” and its configuration into your mix done by the more subtle matching of inference.
>
> [...]
>
> This higher computational finesse will be needed as the next paradigm shift–that of pervasive networking–takes place over the next five years. Objects will gradually become active agents and will travel the networks in search of useful information and tools for their managers. Objects brought back into a computational environment from halfway around the world will not be able to configure themselves by direct protocol matching as do objects today. Instead, the objects will carry much more information about themselves in a form that permits inferential docking. Some of the ongoing work in specification can be turned to this task.

An object, sent over the network; it does not exactly have a common protocol, class, or API, but enough information so it can be understood, matched up with some function or purpose according to inference.  We could also assume given this is from Alan Kay that the vision here is that code, not just data, is part of the object and information (though to consider *code* to be *information*: that is quite a challenge to our modern sensibilities).

When I read this, it struck me that we have these objects all around us.  The web page: remote, transferable, transformable, embodying functionality and data, with rich information suitable for inference.

The web page has a kind of minimal protocol, though nothing is entirely forbidden in how it is interpreted.  For instance the page is named in its `<title>`.  But probably it has a better name in its `<meta name=og:title>`, should one exist; nothing is truly formal except by how it will be conventionally interpreted.  The protocol is flexible.  It has internal but opaque state.  The object can initiate activity in a few ways, primarily XMLHttpRequest and a small number of [APIs](https://developer.mozilla.org/en-US/docs/WebAPI) available to it.  The page receives copious input in the form of events.

It's an impoverished object in so many ways.  And it's hardly what you would call universal, it's always representing visual pages for the browser.  When programming if the browser isn't our intended audience then we choose something like JSON or REST: one dead data, one a possessed and untransferable object (I would assert that in REST the object is the server and not the document).

And yet the web page is an incredible object!  Web pages are sophisticated and well cared for. Our understanding of them is meticulously documented, *including* the ambiguity.  The web stack is something that has not just been "defined" or "fixed", but also discovered.  Web pages contain gateways into a tremendous number of systems, defined around a surprisingly small set of operations.

But we don't look at them as objects, we don't try to deduce or infer much about them.  They don't look like the objects we would define were we to design such a system.  But if we shift our gaze from design to discovery then the wealth becomes apparent: these might not be the objects we would ask for, but given the breadth and comprehensiveness of web pages they are the objects we should use.  And they actually *work*, they do a ton of useful things.

Stepping back from the specific product of [PageShot](https://github.com/mozilla-services/pageshot), this is the broad direction that excites me: to understand and make use of these objects that are all around us.  (Objects to which Mozilla, with its user agent, has unique access.)  But we need to look more broadly at what we can do with these objects.  PageShot tries one fairly small thing: capture the visual state at one moment, [maybe do something with that state](http://www.ianbicking.org/blog/2015/04/product-journal-building-block.html).  If we just had a handful of these operations, exposed properly (not trapped in the depths of monolithic browsers) I think there are some incredible things to be done.  Maybe even a way to bridge from the ad hoc to something more formal; as crazy as the web page execution model seems, it has some nice features, and is the widest deployed sandboxing execution model we have.

In this sense [Web Assembly](http://www.2ality.com/2015/06/web-assembly.html) and [ASM.js](http://asmjs.org/) are interesting as effectively competitors to JavaScript, but not competitors to the web platform or web-page-as-object.  That makes them different from [Google Native Client](https://en.wikipedia.org/wiki/Google_Native_Client).  Yes, Web Assembly is essentially another language for the web platform.  But Native Client uses [Pepper](https://en.wikipedia.org/wiki/Google_Native_Client#Pepper) which is *not* the web platform, it's a parallel platform that attempts to mimic the web platform.  ASM.js and Web Assembler are a demonstrations that we can change significant parts of the code execution while retaining the outward API of these pages.

I find this all exciting, but I am somewhat half-hearted in my excitement.  Reading The Early History Of Smalltalk there's a certain spirit to their work that I love and often despair at recreating.  There is a visionary aspect, but I think more importantly they took a holistic approach.  There's something exciting about opening your mind to far off concepts (a vision) but then try to tie them together creatively, trying different approaches in an effort to maintain simplicity, avoid compromises.  The computing systems they worked on were like [Microworlds](http://edutechwiki.unige.ch/en/Microworld) of their own creation, they could redefine problems, throw away state, reinvent any interface they chose.  And maybe that is also available to us: only when we hopelessly despair about problems we cannot fix are we trapped by our legacy.  That is, if you accept the web as it is there is a freedom, an agency in that, because you've put aside the things you can't change.

I suspect Alan Kay would take a dim view of this whole notion.  He is not a fan of the web.  Another observation from that history:

>  Four techniques used together—persistent state, polymorphism, instantiation, and methods-as-goals for the object—account for much of the power. None of these require an "object-oriented language" to be employed—ALGOL 68 can almost be turned to this style—an OOPL merely focuses the designer's mind in a particular fruitful direction. However, doing encapsulation right is a commitment not just to abstraction of state, but to eliminate state oriented metaphors from programming.

I can't even begin to phrase web pages in these terms.  State is a mess: much hosted on remote servers, some in the URL, some in the process of the running page, some in cookies or localStorage, all of it constantly being copied and thrown away.  Is the URL the class and the HTML served over HTTP the instantiation?  These are just painful contortions to find analogs.  Methods-as-goals is the one that seems most interesting and challenging, because I cannot quite identify the goals behind this whole endeavour.  Automation?  Insight?  Detection?  Creation?  Is it different from what Google is doing with its spiders?  Is there something distinct about interpretation in the context of a user agent?  And when the objects are not willing – I am proposing we bend pages to our will, wrestling control from the expectations of site owners – can you do any delegation?  Is there an object waiting to be smithed that encapsulates the page?  

More tensions than resolutions.  Wish I had time to bathe in those tensions a bit longer.