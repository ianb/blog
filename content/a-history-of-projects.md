Title: A History Of Projects
Slug: a-history-of-projects
Date: 2020-09-08

I've [had a lot of projects](https://www.ianbicking.org/projects.html), and at this [moment of reflection](https://twitter.com/ianbicking/status/1293275255667073024) I thought I'd look back through those that felt most meaningful, and which despite my excitement I've also let go of. If there's a thread that connects them maybe I'll find it, or maybe this is just a scattering of work...

## <span id="redline-review">1. Redline Review</span>

This was my first real application, written in the early 2000s, coming out of a consulting engagement I had with a [now-defunct encyclopedia publisher](https://en.wikipedia.org/wiki/Fitzroy_Dearborn_Publishers). They needed entries reviewed by loosely-affiliated domain experts; I believe this was first used for the _Encyclopedia of Monasticism_. [Audrey Berns](https://www.linkedin.com/in/audreyberns/) conceived of the idea, brought me in, and in retrospect acted as product manager, though that wasn’t a thing at the time.

The web application didn’t use JavaScript and just put a little link to a commenting form after every sentence in the text. Most of the work was about importing, login management, and workflow. The client was pretty happy with it, and I tepidly tried to turn this into a commercial application, but I didn’t really understand what I was doing.

## <span id="landscaper">2. Landscaper</span>

This was my favorite project from my time with the (still existing!) web consulting company [Imaginary Landscape](https://www.imagescape.com/). Landscaper was a CMS that published to static files ([Server Side Includes](https://en.wikipedia.org/wiki/Server_Side_Includes), but I would have liked to add PHP). This is an idea that wasn’t that uncommon at the time (remember [Movable Type](https://www.movabletype.org/)?) but fell out of favor, and now is back in favor.

I co-developed this along with [Paste](https://pypi.org/project/Paste/) and [formencode.htmlfill](http://www.formencode.org/en/latest/modules/htmlfill.html). One of the features I was particularly proud of was the custom page types: a new page type was defined by writing (in the CMS) a template and an HTML form, and FormEncode could parse all the information from that. It wasn’t sophisticated, but it was so _simple_.

Much of the design and requirements was done by [Lisa King](https://www.linkedin.com/in/lisa-king-5013933/). I distinctly remember one of our many design reviews where we had reached a point of disagreement: when we got to the end she effectively threw up her hands, _fine, you can have your way like always_, which surprised me because I thought we had ended up someplace quite different than where we started. I thought we were participating in a generative process. But what I thought was a series of different proposals she had seen as me reiterating and reexplaining the same concept to exhaustion, and why wouldn't she? The compromises I made were all part of an internal dialog. A lesson I took from that was to be overtly explicit when I was incorporating or adopting someone else’s idea or adapting an idea to input. I _am_ stubborn, to a fault, but not nearly as stubborn as it seemed!

The CMS was proprietary, so I left it when I left the job. I don’t believe it is used any longer. Building a minimalist CMS is still on that list of things-I-probably-won’t-get-to (but still think about).

## <span id="sqlobject">3. SQLObject</span>

I’ve lost track of why I even created [SQLObject](http://sqlobject.org/). I believe it was when I was involved with [Webware](https://webwareforpython.github.io/w4py/), a Python web framework from from an earlier generation.

I like to think that it was early and perhaps influential in the use of metaprogramming in Python. It also represents some naivety on my part about database programming, embodying a style I was used to in MySQL/PHP projects, but I hadn’t encountered larger and more complicated databases.

As a project SQLObject was hard for me: I felt weighed down by early design choices, and chronically guilty about support and maintenance. [Oleg Broytman](https://phdru.name/) took over maintenance and has done an excellent job keeping it going over the years.

## <span id="formencode">4. FormEncode</span>

In some ways [FormEncode](http://www.formencode.org) represents an answer to a problem whose time has passed: how should we manage complicated HTML forms with validation and editing? Now this is mostly handled on the client side, and a “validation” framework only has to reject bad data, it doesn’t have to help the client repair that data (JavaScript can handle that part).

FormEncode also looked at the problem as a general encoding/decoding problem, and a schema definition problem.

Together with SQLObject these probably represent taking clever declarations too far. I now accept and appreciate imperative declaration for more cases. I don’t think I did a good job passing on maintainership, but [Christoph Zwerschke](https://cito.github.io/) and [Christopher Lambacher](http://whatschrisdoing.com/) kept it going despite that.

## <span id="paste-wsgi">5. Paste and WSGI everything</span>

I was frequently forced to work with [Zope](https://en.wikipedia.org/wiki/Zope#Zope_2) professionally. There are some interesting ideas in Zope, but mostly it was a very difficult environment to understand, control, and manipulate. Zope’s monolithic application server represents an approach that was common at the time, but would be unfamiliar to most web developers today.

[Web SIG](https://www.python.org/community/sigs/current/web-sig/) offered a kind of reprieve, and I became very enthusiastic about the [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) concept that [PJE](https://dirtsimple.org/) proposed (I think for him it may have come out of his work with [Chandler](<https://en.wikipedia.org/wiki/Chandler_(software)>)?)

WSGI turned web programming into something more functional, keeping application servers and web handlers separate, and turning middleware into just function composition. Application server and handler are both critical components of an application, but have every ability to be separate: application servers dispatch concurrent work and manage reliability, and they really don’t need to know much about how the work gets done. Handlers contain all the domain logic. Middleware I’m not as sure about.

Along the way I built a toolkit called Paste meant to be a neutral reusable library for doing web things. I enjoyed the power of it all, building [interactive debuggers](https://www.ianbicking.org/my-first-ajax-app.html), [test frameworks, proxying](https://www.ianbicking.org/blog/2010/04/webtest-http-testing.html), [configuration and composition](https://docs.pylonsproject.org/projects/pastedeploy/en/latest/) systems, a [command-line script framework](https://pastescript.readthedocs.io/en/latest/), [logging and monitoring](https://web.archive.org/web/20160719224005/http://pythonpaste.org/modules/exceptions.html) systems.

Those tools were used some, but the frameworks that made use of them have mostly disappeared in favor of web frameworks that are managed in a more monolithic fashion. (The frameworks might not be technically more monolithic, but I think it’s accurate to say that their _communities_ are.)

What remains of Paste is now in other projects, various people extracted the bits that were useful and reimplemented them in new packages. [Pylons](https://pylonsproject.org/) got several, [Repoze](https://repoze.readthedocs.io/en/latest/) some others.

To the degree this work had impact, it was mostly through other people: [Ben Bangert](https://be.groovie.org/) and [Philip Jenvey](https://twitter.com/pjenvey) did a lot of early work, [Chris McDonough](https://twitter.com/chrismcdonough) did the extraction work to keep the pieces alive.

## <span id="webob">6. WebOb</span>

WebOb was an effort to clean up things from Paste by creating one big WSGI request and response object, trying to be as thorough and high quality as possible. Paste could have looked like WebOb at any time, but it took me a while to acknowledge that being bland and neutral (to avoid competing with web frameworks) wasn’t very useful.

WebOb used WSGI as the basic model for requests and responses, but I found it was also a good test framework and client library. If it was timed earlier and my interest had been different I may have pushed for it to be a more “standard” set of objects for Python.

WebOb still exists and is maintained inside Pylons. Sergey Schetinin did a very solid job maintaining it until it passed to [Bert JW Regeer](https://bertjwregeer.com/) who continues to maintain it.

## <span id="deliverance">7. Deliverance</span>

As mentioned, Zope haunted me professionally. I had to deal with Zope, but I hated it, and wanted to find ways to support more heterogeneous environments.

[Deliverance](https://github.com/deliverance/Deliverance) was a project started by some Zope people (I believe [Paul Everitt](https://twitter.com/paulweveritt) specifically roped me into it). The idea was to separate styling and other aspects of “delivery” from the backend. He did it with a language that compiled into XSLT, with selectors that used XPath and I think it required XHTML content.

The goal was to be able to support sites that used Zope, other Python servers, WordPress, and whatever else may come along. But all the applications should be consistent and allow styling that would be applied across all of them.

I rewrote it as a WSGI server and used [lxml](https://lxml.de/) for the rewriting. I wrote [lxml.cssselect](https://lxml.de/cssselect.html) to support CSS instead of XPath, and extended [lxml.html](https://lxml.de/lxmlhtml.html) to enable other interesting tricks.

lxml is one of those libraries that I wish had become a standard for Python. The installation was annoying, but the functionality is great. Along with `formencode.htmlfill` this is where I started to really enjoy using parsed HTML as a first-class data representation.

Deliverance [source exists](https://github.com/deliverance/Deliverance), but hasn’t been updated for many years.

This happened around when [microservices](https://martinfowler.com/articles/microservices.html) were becoming a thing. In a sense Deliverance represents a very different idea of microservices, where the services are actually presented directly to users, and the goal is reusable interactive web applications and components. We see some of this today where the assembly is done in the browser itself (via JavaScript), but it remains an ad hoc and informal approach. [Sandstorm](https://sandstorm.io/) has some similar motivations.

## <span id="silverlining">8. Silver Lining</span>

At this point I was struggling with sharing application setup and deployment – it was hard for me to maintain for my own stack, not to mention share with teammates.

I played around with [App Engine](https://cloud.google.com/appengine) a bit, but it had so many constraints that I couldn’t advocate it or use it for my own work. Automatic server provisioning was a new thing, and [libcloud](https://libcloud.apache.org/) had come on the scene.

[Silver Lining](https://github.com/ianb/silverlining) was meant to be a way to take fairly regular applications and develop them locally or deploy them to a remote server, with a consistent approach. The model was similar to [Twelve-Factor](https://12factor.net/), emphasizing environment variables. It supported multiple applications, using lots of generated Apache configuration to do the routing in production. It strongly encouraged vendors libraries and avoided remote builds.

I _really_ liked it. It made development feel good to me, got all the bad parts out of the way. I never seriously used Heroku, I imagine it feels the same? But no one else found it interesting, and it didn’t go anywhere.

I played around with a web application specification I called [pywebapp](https://github.com/ianb/pywebapp/blob/master/docs/spec.txt), but I already had [one foot out the door](https://www.ianbicking.org/blog/2014/02/saying-goodbye-to-python.html) of Python web development.

## <span id="pip-virtualenv">9. pip and virtualenv</span>

Building and composing applications was a theme through these, and pip and virtualenv fit into the same area.

With both this and WSGI work, I was mostly making the work of Philip J. Eby (PJE) more accessible. He mapped out and largely implemented both projects, and I applied my own sense of aesthetics to them. [easy_install](https://setuptools.readthedocs.io/en/latest/easy_install.html) implemented much of what pip actually did, but people _loved_ to complain about `easy_install`. The situation was to the point where people were regularly rejecting _any_ transitive dependencies because they rejected the idea of installers.

pip changed easy_installs defaults, added a little metadata, and I’d like to think it added a bunch of attractive command line and logging aesthetics.

virtualenv took a tiny script PJE had written and again made it more pleasant to use.

These are by far my most popular works. I’ve stopped working on them long ago, but luckily other people have done great work both improving and advocating for them. I cannot even take credit for transitioning them. [Donald Stufft](https://twitter.com/dstufft) and [Carl Meyer](https://twitter.com/carljm) in particular got these projects through the lean winter months before they had a new spring. I am now [number 14](https://github.com/pypa/pip/graphs/contributors) in the list of pip contributors, which I find quite gratifying.

The irony of these projects is that I was always trying to get _past_ the operational issues of installation and deployment. I don’t like building and installing and composition, but I wanted to invest some time so that my work was spent more on the things I really wanted to do, things that felt valuable to struggle with. And this is probably why they were successful: everyone else felt the same way, so at the time the space was both open and needed. But I will also take some credit for putting significant effort into promotion, which helped center the community around the tools, both in terms of contribution and documentation. It's unfortunate that the next set of functionality – environment management, dependency bundling, executable bundling, etc – hasn't been able to gel into an agreed-upon set of tools. Someone would be doing the community a favor to try to build consensus, even though manufactured consensus will require some uncomfortable forcefulness.

## <span id="doctestjs">10. doctest.js</span>

This isn't a large project, just a path-not-taken; a failed attempt to exist in the JavaScript open source world as I had in Python.

I really liked doctest in Python. My own personal feeling about tests is that they should support forward momentum, and good test failures are the most important part of a testing framework. A failure should tell you as much as possible about what to do next. And stubbed tests should be easy to turn into real tests.

[Doctest](https://docs.python.org/3/library/doctest.html) is great for all of this: you just write some REPL-like code, and your failures are all in the form of potentially-passing tests (just copy in the output!)

I wanted to bring this to JavaScript, and did so in [doctest.js](https://github.com/ianb/doctestjs) (with [improvements!](http://www.ianbicking.org/blog/2012/10/why-doctestjs-is-better-than-pythons-doctest.html)). But no one ever cared. Sigh.

I never got the hang of the JavaScript open source world. I don’t feel like part of the JS open source community, but I also don’t even know what it would feel like or where that community is. Clearly I show my age.

## <span id="togetherjs">11. TogetherJS & Hotdish</span>

These are the kinds of projects that I had always wanted to get to: projects that meaningfully change how we interact with computers.

[TogetherJS](https://togetherjs.com/) is a drop-in library to add realtime collaborative features to any website, a category of tool known as [cobrowsing](https://en.wikipedia.org/wiki/Cobrowsing). It includes UI and infrastructure, a ton of complicated session management, and it at least tries to engage with the complicated user questions that arise with collaborative browsing. And people really liked it!

I made TogetherJS with [Aaron Druck](https://aarondruck.com/) and [Simon Wex](https://github.com/simonwex) in [Mozilla Labs](https://www.mozillalabs.com/). We knew the [end was coming for Labs](https://www.ianbicking.org/blog/2014/09/professional-transitions.html), and Aaron and [Gregg Lind](https://www.linkedin.com/in/gregg-lind/) and I tried to pivot to something more Firefox-centric with a project called [Hotdish](https://www.ianbicking.org/projects.html#hotdish). Hotdish was based on a collaborative browser window, where anything you did in that window was shared with your little group, including screensharing, ambient awareness, and cursor sharing, as we tried to think about how people could work virtually next to each other. Especially since on computers you aren’t really “next” to each other even when you are in the same room, and we wanted to change that.

But no one in Mozilla cared. Aaron was laid off when Labs closed, and I probably would have been as well if my manager hadn’t given me some cover. We’d just had a second child, my confidence was low, and I didn’t want to make big changes, so I licked my wounds and moved on.

This one really hurt. I really believed in what we were doing, in how we were doing it, even in the potential alignment with Mozilla. It was the work I _wanted_ to be doing all along. And it felt like it amounted to nothing.

I withdrew completely from TogetherJS. I felt unable to maintain a healthy relationship with it while also keeping my head above the water on other matters. Unfortunately I didn’t make it easy for other people to keep it alive, though it refused to quite die and [still exists today](https://github.com/jsfiddle/togetherjs).

The best summary of my thoughts inspired by TogetherJS and Hotdish is in [Towards a Next Level of Collaboration](https://www.ianbicking.org/blog/2014/03/towards-next-level-of-collaboration.html).

## <span id="screenshots">12. PageShot and Firefox Screenshots</span>

I started PageShot based on a hint of strategic direction from the CEO of Mozilla, and then went long with it. [Donovan Preston](http://donovanpreston.com/) was able to work on it for quite a while, until we got further on and he was feeling ready to swap out and I was ready to swap in.

The goal was to provide full-page frozen DOM renderings as a shareable resource on the web. This is a little like [archive.is](https://archive.is/), except that it’s your personal view of a site, not the public view. There are also several projects that do this locally, like [WebMemex](https://blog.webmemex.org/). I really wanted to do it as something shareable, a frankly aggressive move to give people personal autonomy over the things they see. It also could be a hub for [annotation](https://www.ianbicking.org/blog/2015/05/product-journal-as-we-may-discuss.html), data extraction, scraping, history tracking… all sorts of things.

But of course there were serious security and copyright concerns. So, when the time came to actually ship it, we dropped all the cool DOM freezing stuff and just kept the pixel screenshotting, removing even the most basic metadata we had been capturing. It was hard to let it go. We told ourselves we’d try to bring it back, but we all knew…

Then the project shipped in Firefox, and it was a quiet but very popular service. It didn’t do anything unique, but I think we created a very nice interface (with considerable effort from [Bram Pitoyo’s](https://bram.me/) and [John Gruen’s](https://johngruenprojects.com/) design work). In general it was an exercise in reducing expectations and actually being satisfied with the result. Millions of people used it, people frequently mentioned it when talking about why they liked Firefox, and we saw real retention improvements among its users. It took a big hit with the [Quantum redesign](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/), which relegated it to what I have come to call the “meatball menu” (the hamburger menu’s cousin, a line of three meatballs: ⋯). But people still found and enjoyed it (small lesson: many people love the context menu?!)

Then sharing and the server were cancelled and the project largely pushed aside because… I don’t know? We never fit into any strategy, and we were all tired. I was tired too so I didn’t fight it. It was a modest feature, it didn’t feel like “the future”. And it wasn’t, it was a rehashing of very old and well-understood things. I myself had to put in quite a bit of effort to accept that there is value in doing old and well-understood things when that’s what the people want.

Screenshots remains a feature in Firefox.

## <span id="browserlab">13. Browser Lab</span>

This is a project that never launched, but I sure did fiddle with it for a long time.

[Context Graph](https://medium.com/firefox-context-graph/context-graph-its-time-to-bring-context-back-to-the-web-a7542fe45cf3) was a Firefox initiative: _a forward button for the web_. Or: another way to get to what’s next, not links promoted by Facebook’s algorithm or scrolling ever further down some infinite scroll timeline or reflexively opening the same sites over and over. What if your browser could offer something smart for _where next_?

I was never directly involved with Context Graph, but why not see what there is to learn? PageShot was still capturing full pages at this stage, and I extract a list of all the URLs I had visited for the last two years and started to [drive it through PageShot](https://www.ianbicking.org/blog/2016/08/product-journal-oops-a-scraper.html). I did it in a window in the background while I was working, and it was surprisingly weird feeling to see all these old news articles pop up, old emails (Gmail URLs are very stable!), and every other little bit of web activity I had built up.

It felt like there was gold in there, though retroactively getting pages didn’t give me nearly as much data as I would like. So I made what I first called the Personal History Archive, and then I half-renamed [Browser Lab](https://github.com/ianb/personal-history-archive/). After installing the program and extension it will extract as much browsing data as possible, serializing it into a local SQLite database and static files, including frozen copies of pages.

The result is entirely impossible to share. It’s not like sharing URLs, which might be embarrassing, but are easy enough to scrub. For instance if you open Gmail then all the subject lines are serialized. So my goal was either self-experimentation, constructing a personal shareable set (e.g., do all my GitHub and open professional activity on it, but avoid most other normal activity), or get Mozilla to hire some temps to spend the day idly browsing with the understanding that we were recording them.

It never got that far, but I did enjoy messing around with it, and I still believe there’s gold in there. I made an accompanying Python library to handle the data, and made it usable in Jupyter. I think the idea of datasets paired with libraries is something we should do more of. I played around with [training a neural net to detect article bodies](https://github.com/ianb/personal-history-archive/blob/master/python/nn_readable.ipynb) and realized [named-entity extraction is very greedy](https://github.com/ianb/personal-history-archive/blob/master/python/named_entities.ipynb). But I never got very deep into the analysis I was trying to enable.

There’s really no reason for me to ever revisit this, even though I found it a genuinely fun and interesting project. If there was something to be learned there it was for Mozilla to learn and act upon. And Mozilla still could! I never knew how to get people’s attention.

## <span id="firefox-voice">14. Firefox Voice</span>

This is not the end of the list, just the end for now, because Firefox Voice brings us up to today. (I vow to start, maybe finish, and move past many entirely new projects!)

[Firefox Voice](https://github.com/mozilla-extensions/firefox-voice) was started shortly before I joined the Consumer Voice Products team, by [Julia Cambre](https://juliacambre.com/) and [André Natal](https://twitter.com/andrenatalbr). It was the second attempt at the idea by the team (with [Abe Wallin](https://abewallin.com/), [Janice Tsai](https://www.harraton.com/), and [Jofish Kaye](http://jofish.com/)). The concept was straight-forward: build a voice assistant for the browser. I’ve been working on the project for the last year.

This deserves a whole post, so I won’t do a retrospective here ([Thoughts on Voice Interfaces](https://www.ianbicking.org/blog/2020/08/thoughts-on-voice-interfaces.html) offers some of my general observations). I did believe in the project. As a voice assistant for desktop Firefox it wasn’t enough. But as a toehold to create a natural language interface to the web, it could have been a lot. Everything you want to interact with in your computing life is accessible one way or another through the web, and building new ways to get at that feels useful and important. And maybe it still could be, we’ll see... but it won’t happen at Mozilla.

Even before the project (and team and division) was [cancelled](https://blog.mozilla.org/blog/2020/08/11/changing-world-changing-mozilla/), I realized Mozilla wasn’t ready to invest enough to succeed. I don’t think success requires an [Alexa-sized project](https://voicebot.ai/2018/11/15/amazon-alexa-headcount-surpasses-10000-employees-here-is-the-growth-rate/), but it’s bigger than a team of four and a handful of interns, as much as I enjoyed working with them all.

## <span id="what-next">What next?</span>

I seldom think about most of the old projects now. They have long ago been [paged out](https://en.wiktionary.org/wiki/page_out) of my mind to make room for new things. It feels a little unfair to my past self, enthusiastic and full of hope around some new idea. I haven’t even lost faith in many of those ideas, but I am no longer the one suited to pursue them.

I’ve had to put aside guilt to move on, but I haven’t figured out how to balance that with the work to let a project live up to its potential. I respect those who have done the work to maintain open source projects over a long period of time, and I've accepted I'm not that kind of person.

The lesson I’m taking from this exercise of listing projects is that I have not paid enough attention over the years to the people I’ve worked with. Software can’t survive long on its own, and its intrinsic value is as limited as its longevity. Professional relationships are also impermanent. But… there’s potential I’ve missed out on.

Still, I’m hardly the only one who moves on: people, companies, industries, entire societies move on from problems. They just decide something doesn’t matter, or doesn’t matter _enough_. Often I’ve felt like the last one at the party, not able to call it quits. Who am I to blow against the wind?

So, what next?
