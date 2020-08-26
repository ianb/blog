PageTitle: Projects
Title: Projects
slug: projects

This is a list of projects I am working on, or have worked on. All are open source.

-   [Recent(ish) work](#currentwork)
-   [Projects I've Retired From:](#retired)
    -   [Collaboration / general](#collaboration)
    -   [Python Packaging](#packaging)
    -   [Python Web](#pythonweb)
    -   [Python Testing](#pythontest)
    -   [Smaller Python projects](#smallpy)
    -   [Miscellaneous / Small](#miscretired)
-   [Small projects](#smallcurrent)
-   [Toys](#toys)

## <span id="currentwork">Recent Work</span>

<dl>

<dt><a href="https://github.com/mozilla-extensions/firefox-voice/">Firefox Voice</a></dt>
<dd>Firefox Voice was our project out of the now-defunct Consumer Voice Products team, in the now-defunct voice program in Mozilla, part of the now-defunct Emerging Technologies division.<br><br>
Firefox Voice is a voice assistant for the browser, allowing the simple commands like "new tab" as well as routing and interpreting messages to Google ("what's the weather"), integrating with music services ("play David Bowie") and many other commands.<br><br>
At least for a while (I'm writing this in August 2020) it's available <a href="https://addons.mozilla.org/en-US/firefox/addon/firefox-voice/">on addons.mozilla.org</a>.<br><br>
I wrote some thoughts coming out of this project in <a href="https://www.ianbicking.org/blog/2020/08/thoughts-on-voice-interfaces.html">Thoughts on Voice Interfaces</a>.</dd>

<dt><a href="http://www.ianbicking.org/blog/2019/03/firefox-experiments-i-would-have-liked.html">Test Pilot Firefox experiment backlog</a></dt>
<dd>Although I was able to ship some things in Test Pilot, there was a long backlog of ideas, and experiments I started but didn't work out or weren't able to be shipped. I made a list of them!</dd>

<dt><a href="https://github.com/mozilla-services/screenshots"><strong>Firefox Screenshots</strong></a></dt>
<dd>I started Page Shot (which became Firefox Screenshots) in October 2014. During that time I went from doing it as a small side project, to managing the project during its nascent stages, then when I left management I rejoined development to get it launched as a <a href="https://testpilot.firefox.com/experiments/page-shot">Test Pilot experiment</a>. During that period it went from being a page freezing tool (similar to the Way Back Machine) to a screenshot tool.<br><br>
It was popular inside Test Pilot experiment channel, and it wasn't much later when it re-launched as a core Firefox feature in September 2017. When it launched it was the first Mozilla product built that took unencrypted user content, that used Google Analytics, the first Firefox feature to ship as a <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions">WebExtension</a>, and the first use of <a href="https://sentry.io/welcome/">Sentry</a> to monitor errors in the browser. <br><br>
For myself, Screenshots has been a lesson in managed expectations, but also a lesson in <a href="http://www.ianbicking.org/blog/2018/02/web-small-composable-tools.html">providing simple tools</a> without worrying about how hard they are to create. <br><br>
Despite being popular, in 2019 the server component of Screenshots is being shut down, though the tool will otherwise remain in Firefox. During its life 36 million people used the Screenshots server with over 100 million screenshots uploaded. About 20% of screenshots created are uploaded (instead of being downloaded or copied to the clipboard), so it would be reasonable to estimate 500 million screenshots taken in the course of two years.</dd>

<dt><a href="https://github.com/mozilla/side-view"><strong>Side View</strong></a></dt>
<dd>Another <a href="https://testpilot.firefox.com/experiments/side-view">Test Pilot experiment</a>, this makes it easy to open a mobile view of a website in the Firefox sidebar. I'm mostly proud that we kept it simple and usable.</dd>

<dt><a href="https://github.com/mozilla/email-tabs"><strong>Email Tabs</strong></a></dt>
<dd>Another <a href="https://addons.mozilla.org/en-US/firefox/addon/email-tabs/">Test Pilot experiment</a>. This was strongly influenced by <a href="https://blog.mozilla.org/ux/2015/02/save-share-revisit/">Mozilla's user research</a>. The results of our research was clear: everyone loves to save and share things by email. And yet it took me a few years to sit down and quickly hack out a tool that makes emailing articles work well. Working with email, and poking around in other company's email products, is a bit like science: you have to see what works, nothing works by default or because you want it to work a certain way.<br><br>
I'm excited by Email Tabs, in no small part because of the simplicity and power of prepopulating compositions. Composing (but not sending) an email is transparent, manipulable, and open-ended. I hope I have the chance to use this lesson elsewhere. The browser is a great location for this, because the browser can integrate with systems in the same way a user integrates with systems, which isn't just handy but also is a kind of working in the open: you can see and understand what the automation does, because it does what you might have done. I wrote some thoughts in <a href="https://www.ianbicking.org/blog/2018/11/thoughts-on-email-tabs.html">Thoughts on the Firefox Email Tabs experiment</a></dd>

<dt><a href="https://github.com/ianb/personal-history-archive/"><strong>Personal History Archive</strong></a></dt>
<dd>I've been poking around at this project for a long time, never really finishing it or deciding exactly what to do with it. The underlying goal is to support local, personal experimentation with the data that can come out of a browser. Most collection like this emphasizes data collected from many aggregate sources, either from select sources or with anonymization, and with only a rough outline of user behavior. A user agent (like a browser) sees everything! It doesn't just see that you visited a site, it sees exactly what that site displayed. It doesn't just see that you have an email, every email you read is displayed by the browser.<br><br>
So this is a tool to try to collect all that intimate data in a way that supports personal experimentation. Especially experimentation that can produce tools uniquely suited for a user agent that belongs to the user, touching data you'd never want to give to an external service.<br><br>
Also I have just been poking around with creating highly usable data dumps, where the data is clean, always well-formed, and where behavioral and more static data is mixed together in a usable way.</dd>

<dt><a href="https://github.com/ianb?tab=repositories">Other GitHub miscellany</a></dt>
<dd>Working in the open at Mozilla I have had the opportunity to try things out. Sometimes they work out, and sometimes they don't. At that stage you'll find my work in GitHub, which is updated more frequently than this page.</dd>

</dl>

## <span id="retired">Projects I've retired from</span>

Download stats [aren't necessarily accurate](https://packaging.python.org/guides/analyzing-pypi-package-downloads/), but as of June 2019 pip and virtualenv (which I originally wrote) were downloaded 980 million and 150 million times respectively. Computers are very good at downloading things! The balance of [packages I have written/started](https://gist.github.com/ianb/0a2fa5cd75f6d2ef04c71c546d2df692) have been downloaded roughly 70 million times, most notably WebOb, Paste, PasteScript, PasteDeploy, WebTest, Tempita, SQLObject, and INITools.

## <span id="collaboration">Collaboration / general</span>

<dl>

<dt><a href="https://togetherjs.com/hotdish/"><strong>Hotdish</strong></a></dt>
<dd>This took some of the ideas of TogetherJS, some of the tech from <a href="https://github.com/mozilla/browsermirror">Browser Mirror</a>, and thinking about them all in the context of a browser session.  It's implemented as a Firefox addon.  The model we came to is one where a group of people share everything they do in a specific browser, with mutual awareness of what each person is doing (both in general, and with in-page feedback using TogetherJS), and people can join and present to each other in this context.  <br><br>  Our longer-term goal was for people to be able to understand what each other are doing -- what pages they are interacting with, but also <em>how</em> they are interacting with those pages, similar to how you can understand what a person is doing when they are doing physical work.  <br><br>  Another goal is to look at how, using the same data we capture in order to share a person's actions with everyone else, we can also use that data to create a richer record of what people are doing.  We wanted knowledge capture and transfer between group members that can encompass not just one site or document, but a session, discussion, and research. <br><br> I <a href="https://www.youtube.com/watch?v=8cJQBBHfF9c&feature=youtu.be&vq=hd720">narrated a screencast that we made</a> to explain some of the concepts and things we learned from the experiment.<br><br>
Some blog posts on the topic: <a href="https://www.ianbicking.org/blog/2014/02/defaulting-to-together.html">Defaulting To Together</a>, and <a href="https://www.ianbicking.org/blog/2014/02/hubot-chat-web-working-in-the-open.html">Hubot, Chat, The Web, and Working in the Open</a>.</dd>

<dt id="togetherjs"><a href="https://togetherjs.com"><strong>TogetherJS</strong></a></dt>
<dd>TogetherJS was my last (shipped) project at the <a href="https://www.ianbicking.org/blog/2014/09/professional-transitions.html">first iteration of the now twice-defunct Mozilla Labs</a>.  TogetherJS is a library and service to enable real-time collaboration on any site. It can still be seen on <a href="https://jsfiddle.net/">JSFiddle</a> where it is used for live collaboration.<br><br>
The larger vision for TogetherJS falls under the category of <a href="https://en.wikipedia.org/wiki/Cobrowsing">Cobrowsing</a>: basically experiencing the web or a website collaboratively. We really wanted to explore what it meant to interact with things side-by-side, moving in and out of synchronous collaboration.<br><br>
Several blog posts on the topic: <a href="https://www.ianbicking.org/blog/2013/10/togetherjs-a-postmodern-tool.html">TogetherJS as a Postmodern Programming Tool</a> (talking about heuristic-based integration), <a href="https://www.ianbicking.org/blog/2013/11/nouning-the-verb-of-browsing-and-activity.html">Nouning the Verb of Browsing</a> (talking about using the on-the-wire messages as a kind of record), <a href="https://www.ianbicking.org/blog/2014/02/hubot-chat-web-working-in-the-open.html">Hubot, Chat, The Web, and Working in the Open</a> (more about creating a record of activity), <a href="https://www.ianbicking.org/blog/2014/02/collaboration-as-a-skeuomorphism-for-agents.html">Collaboration as a Skeuomorphism for Agents</a> (about using the metaphors and mechanisms of collaboration to introduce automated agents), and my thinking concludes in <a href="https://www.ianbicking.org/blog/2014/03/towards-next-level-of-collaboration.html"><strong>Towards a Next Level of Collaboration</strong></a> (which provides a taxonomy and discussion of several specific aspects).</dd>

<dt><a href="http://doctestjs.org">doctest.js</a></dt>
<dd>A testing framework for Javascript, inspired by Python's <a href="http://docs.python.org/2/library/doctest.html">doctest</a>. Something of an alternative to <a href="http://en.wikipedia.org/wiki/Behavior-driven_development">BDD</a>, based on examples and expected output. Blog post: <a href="https://www.ianbicking.org/blog/2012/10/02/why-doctest-js-is-better-than-pythons-doctest/">Why doctest.js is better than Python’s doctest</a>.</dd>

<dt><a href="https://github.com/ianb/walkabout.js">walkabout.js</a></dt>
<dd>This is something like a UI/DOM fuzzing library.  It inspects the DOM (or uses rewritten Javascript code) to determine what parts of the page are "live" (and in what way).  Then it can choose a random action to perform, like clicking on an element or entering text in a field.</dd>

<dt><a href="https://github.com/ianb/seeitsaveit">SeeItSaveIt</a></dt>
<dd>An experiment in extracting structured data from web sites.  Works as a Firefox addon.  This is basically furloughed (as of April 2013) pending progress on <a href="https://wiki.mozilla.org/WebAPI/WebActivities">Web Activities</a>.  The addon allows custom scrapers to be run on sites, with several levels of separation to both allow scraping scripts to run safely and isolated from the site receiving the data.  There is some more information <a href="https://ianb.github.io/seeitsaveit/">on this site</a>.</dd>

<dt><a href="https://github.com/ianb/thecutout/">The Cut-Out</a></dt>
<dd>A synchronization library.  This is intended for HTML/Javascript applications that keep all their data locally, but want to be able to synchronize that data between devices.  But it's perhaps overpowered for that minor task.  This includes several pieces, a client library, a protocol, a server, an on-disk database format, and some rough replication and balancing support. It was an experiment in minimalism.</dd>

<dt><a href="https://github.com/mozilla/browsermirror">Browser Mirror</a></dt>
<dd>This project has largely been superceded by <a href="https://togetherjs.com">TogetherJS.</a>.  This is like a screensharing system, except it works with the DOM instead of pixels - the page you are viewing is transmitted to the other party, but not a "live" page, literally just the things you see.  Things like clicks are transmitted back to the original browser.  Just like screensharing...?  Started out as a "this can't possibly work" project, but then it kind of worked.</dd>

<dt><a href="https://github.com/ianb/webannotate">webannotate</a></dt>
<dd>An offshoot of BrowserMirror and related ideas, taking a snapshot of the DOM and saving it, then allowing annotation of that static page.  Like inline commenting without any of the tricky web overlay ideas.</dd>

</dl>

### <span id="packaging">Python Packaging</span>

I don't currently work on these Python projects, but I authored some important (and now core) parts of the Python packaging ecosystem.

<dl>

<dt><a href="http://www.pip-installer.org/">pip</a></dt>
<dd>The Python Installer Program.  A very popular installation tool for Python.  I wrote this as a kind of response to <code>easy_install</code>, not because I hated easy_install, but because I knew it should be better and that it had relatively small problems that made people hate it.  Pip solved problems people wanted solved, and it's been very popular since then.</dd>

<dt><a href="http://www.virtualenv.org/">virtualenv</a></dt>
<dd>This is an environment isolation tool for Python.  The functionality is now going to be built more directly into Python itself, but virtualenv remains very popular for managing projects. <a href="https://pypi.python.org/pypi/workingenv.py">workingenv</a> was an early attempt at the same concept, but virtualenv stuck because it works really well.  It's just the right level of hack to get everything to work consistently and well.</dd>

</dl>

### <span id="pythonweb">Python Web</span>

There's a bunch of projects that I've worked on in the web space, either authoring or making major contributions. I'm not actively working on any of these myself any more.

Some of the projects in this list are popular, some I think were influential. Several of them I _wish_ were influential.

<dl>

<dt><a href="http://webob.org/">WebOb</a></dt>
<dd><p>WebOb is a Python request and response library (along with some other miscellaneous pieces).</p>

<p>WebOb was an extraction of the ideas in Paste (as seen below), but with a bit more opinion.  It's also the result of letting a bunch of ideas gel for a while.  WebOb has a very specific scope, and implements everything within that scope in an incredibly thorough way. Its completeness exceeds any other Python project I'm aware of (and other languages to the degree I'm aware fo them).  WebOb understands HTTP really well - and it knows how to both read and write HTTP, client and server.  It's primarily focused on being a library for servers, but it can generate requests and parse responses as well, making it uniquely appropriate for middle layers.</p>

<p>WebOb is the basis of many Python web frameworks, Pyramid/Pylons probably foremost among them.  (Django and Werkzeug/Flask being the notable exceptions.)</p></dd>

<dt><a href="http://pythonpaste.org/">Paste Core</a></dt>
<dd><p>Paste, as well as Paste Deploy and Paste Script, were part of a general effort to write a <em>web framework toolkit</em>.  Each contained low-level routines for different tasks.</p>

<p>Paste core is primarily concerned with a set of independent tools for use with <a href="http://wsgi.readthedocs.org/">WSGI</a>.  This includes things like simple routing, static file serving (later turned into <code>webob.static</code>), exception reporting and debugging (later turned into WebError), validation (would become <code>wsgiref.validate</code>), logging, testing (would turn into WebTest), CGI routing, and other stuff.</p>

<p>Where possible much of this has been moved into WebOb or other packages built on WebOb.</p>

<p>The context in which Paste was created was one with a lot of competing Python web frameworks, where there was little overlap in the technology those frameworks used.  Paste tried to create a basic foundation for sharing technology, while still allowing diversity in the actual web frameworks themselves.  It succeeded to a degree.</p>

<p>Paste contained the first web-based interactive debugger for Python (if or when similar tools were built for other languages, I don't know).  Other tools are better now, but Paste pioneered the idea.</p>
</dd>

<dt><a href="http://pythonpaste.org/deploy/">Page Deploy</a></dt>
<dd>Part of the Paste project, this is a configuration system for web apps.  It has been used for a few things; for configuration during actual deployment and for application composition primarily.</dd>

<dt><a href="http://pythonpaste.org/script/">Paste Script</a></dt>
<dd>Also part of the Paste project, this is a kind of framework for building command-line tools to build applications, and some useful commands to go with.  It includes things like a web server <em>container</em> (does that make sense?), and by far the most popular piece has been <code>paster create</code> which helps setup boilerplate files for new projects.</dd>

<dt><a href="https://bitbucket.org/ianb/silverlining/src">Silver Lining</a></dt>
<dd>This was an attempt to create a general web application hosting framework.  Vaguely like Heroku; you'd lay your application out in a certain way, and using Silver Lining you could create a new server instance and upload and update your application.  It supported both Python and PHP, with the potential for other languages in the future. I thought it was really cool, but no one else really got on board. Maybe once you decide to give up this level of control you would rather just pay for the service instead of using an open source product.  I'm not sure.  This was kind of my last hurrah for server-side web projects.</dd>

<dt id="webtest"><a href="http://webtest.pythonpaste.org/">WebTest</a></dt>
<dd>This is a WebOb rewrite of <code>paste.fixture</code>.  WebTest is a tool to make functional tests of your WSGI-using web application (not specifically WebOb applications).  It makes it easy to create artificial but full HTTP requests, send them to your application, and provides a bunch of helpers to inspect the results.  One feature I think is notable (not <em>challenging</em>, just notable) is that it always contains an implicit "this request should work" assertion. Other similar frameworks force you to write <code>assertEqual(resp.code, 200)</code> all the time; what nonsense! In WebTest this is implied unless you say otherwise.  It does form parsing and cookie storage and other stuff too.</dd>

<dt><a href="http://www.formencode.org/">FormEncode</a></dt>
<dd>A form validation and conversion toolkit for web applications. It's built on the idea of a two-way validation/conversion pipeline, structuring an destructuring the content of HTML forms.  It also includes <code>formencode.htmlfill</code>, a library to rewrite forms to insert form values; a novel approach, one that I think deserved to be used more, but like much of FormEncode probably obsolete now as client-side validation is more appropriate.  Like many Hard Problems of web development in the previous decade, this hard problem is best avoided instead of solved.</dd>

<dt><a href="http://lxml.de/lxmlhtml.html">lxml.html (and cssselect)</a></dt>
<dd><p>I didn't write lxml (the general XML and HTML Python library, based on libxml2).  But I did write the HTML-specific wrapper in lxml, which exposes HTML-specific semantics.  This adds knowledge of links to lxml, and forms, and some other stuff - all of which has made lxml an excellent <a href="http://blog.ianbicking.org/2008/12/10/lxml-an-underappreciated-web-scraping-library/">screen scraping library</a></p>

<p>I also wrote <code>lxml.cssselect</code>.  libxml2 contains an XPath parser, and cssselect translates CSS3 selectors to XPath expressions.  If you are curious what this looks like, <a href="http://css2xpath.appspot.com">css2xpath</a> is a little webapp to do those same translations.  I hope you will agree that XPath is ugly.</p></dd>

<dt><a href="http://pythonpaste.org/commentary/">Commentary</a></dt>
<dd>An experiment in commenting on web pages.  Worked as an intermediary to the web page, which turned out to be extremely fragile.  Also this was before we had good HTML parsing available, so it had to use the Old Terrible Tools (like an HTML SAX parser).  I think <a href="https://code.google.com/p/rietveld/">Rietveld's UI</a> was inspired by this.</dd>

<dt><a href="http://blog.ianbicking.org/introducing-htconsole.html">htconsole</a></dt>
<dd>This was a more ambitious take on the interactive web-based debugger.  Instead it was a generalized interactive console.  It had some clever ideas, like inline live function editing.  It exceeded by Javascript skills in some ways at the time, such that it was just a bit <em>frustrating</em> to work on, and I wasn't sure to what end I'd be using it.</dd>

<dt><a href="http://sqlobject.org/">SQLObject</a></dt>
<dd>It's been a long time since I worked on this.  This is one of my first major open source projects, that actually had pickup.  SQLObject is an ORM (Object Relational Mapper).  It pioneered many metaprogramming techniques in Python, allowing a declarative class statement to be mapped to SQL, including SQL expressions.  (NumPy championed some of these features, but I believe SQLObject was the first to use these features for SQL expressions.)  The project is still active, but not very active.  But SQLObject was an inspiration for features in frameworks like SQLAlchemy.</dd>

<dt><a href="http://pythonpaste.org/tempita/">Tempita</a></dt>
<dd>A very small templating language.  I sometimes wanted to generate strings and simply string substitution could be too hard, and I wanted a no-frills no-complications template language.  I think Tempita is really pretty slick.  It also avoids the unnecessary punctuation other template languages have.  It also supports structured content, I think <a href="http://svn.colorstudy.com/home/ianb/recipes/sqltemplate.py">sqltemplate</a> is really cool, though I stopped using SQL before I wrote it.</dd>

<dt><a href="https://bitbucket.org/ianb/referrertrack">referrertrack</a></dt>
<dd>An App Engine tool that uses the Google Analytics API to get a comprehensive list of referrers.  You could use this to watch for <em>every</em> referrer that came to your site, and check them off as you checked each one out.  No one ever cared, but I found it useful (until it bit rotted).</dd>

<dt><a href="http://www.coactivate.org/projects/deliverance/introduction">Deliverance</a></dt>
<dd>This project is now pretty much gone.  It was an HTTP proxy that would rewrite all the outgoing requests to apply styles to those requests.  The idea was to allow a diverse set of applications to be styled in a consistent way, to make up a "site".</dd>

<dt>

</dl>

### <span id="pythontest">Python Testing</span>

Like packaging, I love and hate testing. As a result I've tried a bunch of tools.

<dl>

<dt><a href="https://github.com/pypa/scripttest">ScriptTest</a></dt>
<dd>A script testing framework.  Lets you run a script in a subprocess, and inspect the results of that script: what its output was, stderr, error return codes, and any file changes.</dd>

<dt><a href="https://pypi.python.org/pypi/MiniMock">MiniMock</a></dt>
<dd>A mock library specifically for use with <a href="http://docs.python.org/2/library/doctest.html">doctest</a>. Using doctest, I found it was possible to make a pretty good mock library in almost no code.  (It's gotten <a href="https://bitbucket.org/jab/minimock/src/trunk/minimock.py">a little bigger since then</a>.)</dd>

<dt><a href="http://webtest.pythonpaste.org/">WebTest</a></dt>
<dd><a href="#webtest">Mentioned above</a></dd>

</dl>

### <span id="smallpy">Small Python Projects</span>

In addition to those bigger projects, there's a bunch of small stuff I did that is no longer active.

<dl>

<dt><a href="http://svn.colorstudy.com/PyLogo/">PyLogo</a></dt>
<dd>A Logo interpreter written in Python.  A pretty complete implementation of the language, with a lot of support for calling into and out of Logo to Python.</dd>

<dt><a href="https://github.com/ianb/apppkg">apppkg</a></dt>
<dd>A very incomplete design of an "Application Package" for Python. Some of the motivation described <a href="http://blog.ianbicking.org/2012/02/29/python-application-package/">here</a>. The <a href="https://github.com/ianb/apppkg/blob/master/docs/spec.txt">spec</a> is probably the most interesting part.</dd>

<dt><a href="http://svn.pythonpaste.org/ObConfLoader/trunk/">ObConfLoader</a></dt>
<dd>An attempt to extract a best-practice format for locating Python objects with a string, something that Paste Deploy did in a kind of half-assed way.</dd>

<dt><a href="https://svn.openplans.org/svn/standalone/CheckURL/trunk/">CheckURL</a></dt>
<dd>Check for bad URLs, why not?</dd>

<dt><a href="https://bitbucket.org/ianb/debugheaders">DebugHeaders</a></dt>
<dd>A little WSGI debugging tool to show HTTP headers.</dd>

<dt><a href="https://bitbucket.org/ianb/cmdutils">CmdUtils</a></dt>
<dd>This was intended to be a little framework to make it easier to build high-quality command line utilities.</dd>

<dt><a href="https://pypi.python.org/pypi/fassembler">fassembler</a></dt>
<dd>This was a general build tool I built at The Open Planning Project.  A dead end I suppose, but I liked the architecture.  Now mostly I try to avoid building anything.</dd>

<dt><a href="http://pythonpaste.org/initools/">INITools</a></dt>
<dd>A parser toolkit for .ini files.  Much nicer parser than ConfigParser.</dd>

<dt><a href="https://pypi.python.org/pypi/WebError">WebError</a></dt>
<dd>This was an extraction of <code>paste.evalexception</code>, the interactive debugger in Paste.</dd>

<dt><a href="https://pypi.python.org/pypi/DevAuth/0.1">DevAuth</a></dt>
<dd>A small WSGI tool to try to protect "developer" backdoor access to web applications, in a generalized way.</dd>

<dt><a href="https://github.com/ianb/emailit">EmailIt</a></dt>
<dd>A small application to email a page to a person, kind of "share by email".  Uses lxml to capture a page in a way that can be embedded in an email.</dd>

<dt><a href="http://blog.ianbicking.org/2007/09/12/flatatompub/">FlatAtomPub</a></dt>
<dd>An Atompub server library.  Atompub <em>was</em> supposed to be the culmination of <a href="https://en.wikipedia.org/wiki/Representational_state_transfer">REST</a> thinking.  This was my attempt to assimilate those ideas.  No one ever actually cared about Atompub though, go figure?  This was an interesting experiment, but never useful.</dd>

<dt><a href="http://pythonpaste.org/ohm/">OHM</a></dt>
<dd>The Object HTTP Mapper.  An attempt to create an ORM-like layer for exposing objects over HTTP.  ORMs are a little suspicious, OHM was even more suspicious.  These days I'm pretty <em>over</em> REST, mostly because attempts like this to embrace REST were so unsatisfying.</dd>

<dt><a href="FIXME">TaggerClient</a> and <a href="FIXME">TaggerStore</a></dt>
<dd>An attempt to create a generalized tagging library.  Part of a concept of postmodern, ad hoc, and eclectic components making up a web site. </dd>

<dt><a href="http://svn.pythonpaste.org/Paste/VaingloriousEye/trunk/">VaingloriousEye</a></dt>
<dd>My best project name ever.  This was a little piece of WSGI middleware (a wrapper you could apply around an application) to give live referrer statistics, so you could obsess over who came to your site.</dd>

<dt><a href="http://pythonpaste.org/waitforit/">WaitForIt</a></dt>
<dd>A silly hack of a WSGI middleware.  This would spawn threads so that a request that took a really long time could progress, while still serving up some status information to the user.  People use Celery queues and stuff like that these days, but for a little while some admin tasks could take a couple minutes, causing timeouts that would then abort the task.</dd>

<dt><a href="http://pythonpaste.org/wsgifilter/">WSGIFilter</a></dt>
<dd></dd>

<dt><a href="http://pythonpaste.org/wsgioverlay/">WSGIOverlay</a></dt>
<dd>An experiment with <a href="http://disruptive-innovations.com/zoo/20040830/HTMLoverlays.html">HTML Overlays</a>, kind of a microformat-style way of applying a template to a site, using simple directives to lay the content of a page over a template.  Deliverance was a far more complete implementation of the idea, and one that didn't require application cooperation, but this is the more refined and simple implementation of the idea.</dd>

<dt><a href="http://pythonpaste.org/wsgiproxy/">WSGIProxy</a></dt>
<dd>This would become <code>webob.client</code>.  This is a way of taking a WSGI request and sending it to another server.</dd>

<dt><a href="http://pythonpaste.org/wphp/">wphp</a></dt>
<dd>Embeds PHP in Python, as though a PHP app is another Python WSGI resource.  Basically a hack to send a FastCGI request to an embedded PHP process.</dd>

<dt><a href="http://pythonpaste.org/httpencode/">HTTPEncode</a></dt>
<dd>An overly ambitious attempt to embed structured data in web requests, in a way that they could be extracted "efficiently" in certain server layouts.  Kind of optimizing an HTTP request into a function call when both endpoints were on the same server.</dd>

<dt><a href="http://svn.pythonpaste.org/RhubarbTart/trunk/">RhubarbTart</a></dt>
<dd>Another framework!  A clone of the CherryPy interfaces.  It was kind of an attempt to bully CherryPy into using WSGI better.</dd>

<dt><a href="http://pythonpaste.org/cherrypaste/">CherryPaste</a></dt>
<dd>An attempt to wrap CherryPy in Paste-like semantics.</dd>

<dt><a href="http://pythonpaste.org/djangopaste/">DjangoPaste</a></dt>
<dd>An attempt to apply Paste containerization to Django.</dd>

<dt><a href="https://pypi.python.org/pypi/TracPaste">TracPaste</a></dt>
<dd>Trac with Paste Deploy configuration.</dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/PoorMan/trunk/">PoorMan</a></dt>
<dd>A framework I wrote!  Just for the heck of it.</dd>

<dt><a href="http://pythonpaste.org/wareweb/">Wareweb</a></dt>
<dd>Another silly little framework.</dd>

<dt><a href="https://bitbucket.org/ianb/pickywiki/">PickyWiki</a></dt>
<dd>A little App Engine wiki. <a href="https://bitbucket.org/ianb/wikistorage/">wikistorage</a> is the underlying storage library for App Engine.  I wanted to play around with the sandboxing App Engine provides, to allow more promiscuous code execution on a wiki.</dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/hReviewCollector/trunk/">hReviewCollector</a></dt>
<dd></dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/hReviewParser/trunk/">hReviewParser</a></dt>
<dd></dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/PageCollector/trunk/">PageCollector</a></dt>
<dd></dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/PageSplitter/">PageSplitter</a></dt>
<dd>This would take a really large page and try to split it up into smaller pages.</dd>

<dt><a href="http://scrapy.googlecode.com/svn/trunk/">scrapy</a></dt>
<dd>This never really got anywhere, but it was my aborted attempt to create a scraping framework for Python.  SeeItSaveIt would be my current thinking on the matter.</dd>

<dt><a href="https://pypi.python.org/pypi/ScriptTranscluder">ScriptTranscluder</a></dt>
<dd>This is a web application that lets you transclude content, by basically providing an endpoint that will fetch a given page and parse and rewrite it so it can be included inline in a page.</dd>

<dt><a href="https://pypi.python.org/pypi/dtopt">dtopt</a></dt>
<dd>My most terrible monkeypatching hack ever!  It allows you do to <code>from dtopt import ELLIPSIS</code> inside a running doctest, and add the global ELLIPSIS option based on that.  Actually looks up the stack frame and injects bytecode into a function to accomplish this.</dd>

<dt><a href="http://svn.colorstudy.com/FitLoader/trunk/">FitLoader</a></dt>
<dd>Remember <a href="http://fit.c2.com/">FIT</a>?  Nah, no one does. This was my attempt to create something like that for Python.  It's a silly idea all around.</dd>

<dt><a href="https://code.google.com/p/appengine-monkey/">appengine-monkey</a></dt>
<dd>When App Engine first started it had some things that just felt needlessly different from "normal" Python.  Probably foremost among these was that it had its own HTTP client library.  This library expressed the normal HTTP libraries in terms of this App Engine specific library.  That code was eventually integrated into App Engine itself.  (App Engine's own framework, webapp and now webapp2, also happen to use WebOb.)</dd>

<dt><a href="https://github.com/openplans/geowebdns">GeoWebDNS</a></dt>
<dd>This was an Open Plans project to give a small REST service to map locations to areas.  It used PostgreSQL, had some import tools, did it's thing.  My first and last real geospatial project.</dd>

</dl>

### <span id="miscretired">Miscellaneous / Small Retired Projects</span>

<dl>

<dt><a href="http://blog.ianbicking.org/twill-in-javascript.html">Twill/Javascript</a></dt>
<dd><a href="http://twill.idyll.org/">Twill</a> is an old timey functional testing DSL for web applications.  This was an attempt to use the same DSL in the browser for functional testing.</dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/WebClippy">WebClippy</a></dt>
<dd>An attempt to provide instructional overlays, so multi-step instructions on how to use a web page could be created.</dd>

<dt><a href="http://svn.colorstudy.com/home/ianb/htranscluder">htranscluder</a></dt>
<dd>This did client-side <a href="http://en.wikipedia.org/wiki/Transclusion">transclusion</a> using the microformat <code>&lt;a href="resource" rel="include"&gt;content&lt;/a&gt;</code></dd>

</dl>

## <span id="smallcurrent">Small (maybe not current) Stuff</span>

<dl>

<dt><a href="https://github.com/ianb/misc-recipes">Misc recipes</a></dt>
<dd>Before GitHub when I want to try out an idea, I throw it in an SVN directory.  There's a grab bag of experiments here, all from quite a while ago.</dd>

<dt><a href="https://github.com/ianb/whrandom">whrandom</a></dt>
<dd>A small Javascript library for a pseudo-random generator.</dd>

<dt><a href="https://github.com/ianb/javascript">Javascript style guide</a></dt>
<dd>Not a "project" per se, but my own customization of the <a href="https://github.com/airbnb/javascript">Airbnb</a> style guide, represents my current and ongoing opinion on Javascript style.</dd>

<dt><a href="https://github.com/ianb/browsercommander">Browser Commander</a></dt>
<dd>An incomplete prototype of a kind of file manager built in the browser.  Includes a small server and client library to provide Node.js APIs in the browser (which are proxied over WebSockets to the server).</dd>

<dt><a href="https://github.com/ianb/git-sync">git-sync</a></dt>
<dd>A small script to use git more like rsync for the purpose of deployment.  Motivation explained some in <a href="http://blog.ianbicking.org/2012/02/14/git-as-sync-not-source-control-as-deployment/">this post</a>.</dd>

<dt><a href="https://github.com/mozilla/receiptverifier">receiptverifier</a></dt>
<dd>Not very active right now.  This is a library to do client verification of <a href="https://developer.mozilla.org/en-US/docs/Apps">Open Web App</a> receipts.  It's not very exciting, but it does do a heck of a lot of error handling. It was an exercise in thoroughness. Maintained by other people now.</dd>

</dl>

## <span id="toys">Toys</span>

<dl>

<dt><a href="https://github.com/ianb/wordpool">Wordpool</a></dt>
<dd>A little HTML/Javascript word-search-like game.  The product of a two-hour hackathon.</dd>

<dt><a href="https://github.com/ianb/xmasapp">xmassapp</a></dt>
<dd>I wanted to compile Christmas carols that I liked, without any fluff.  Also it's an example of an <a href="https://developer.mozilla.org/en-US/docs/Apps">Open Web App</a>.</dd>

<dt><a href="https://github.com/ianb/deducer">deducer</a></dt>
<dd>A small Javascript/HTML game of logic.  Based on <a href="http://www.kaser.com/sherwin.html">the Sherlock game</a>. Has no instructions, is not really usable ;)</dd>

<dt><a href="https://github.com/ianb/fatfingers">fatfingers</a></dt>
<dd>An attempt to turn ambiguous touch events into modal selections, as a client library.</dd>

</dl>
