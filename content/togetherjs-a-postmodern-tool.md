Title: TogetherJS as a Postmodern Programming Tool
slug: togetherjs-a-postmodern-tool
Date: 2013-10-31

One of the papers that I continue to refer to in my own thinking about technology is [Notes on Postmodern Programming](http://www.mcs.vuw.ac.nz/comp/Publications/CS-TR-02-9.abs.html). Martin Fowler has a [short summary](http://martinfowler.com/bliki/PostModernProgramming.html):

> The essence of it (at least for me) is that software development has long had a modernist viewpoint that admirable software systems are composed of uniform components, composed in a uniform and simple way. (Smalltalk and Lisp are good examples of this kind of thinking.) A post-modern view is that software is all sorts of different very different stuff glued together in all sorts of different ways (think Perl and Unix), and this style of software (big bucket of glue) isn't a bad thing.

In the built world I think of roads and rail as an interesting analog, roads as postmodern and rail as modern.  Rail has a lot of cool properties.  It's [really efficient](http://www.csx.com/index.cfm/about-csx/projects-and-partnerships/fuel-efficiency/), one driver can handle a hundred cars, you can feel confident about where the train will and won't go, and it can be a pretty smooth ride. But roads have some great properties too.  You can ride all kinds of vehicles down them.  It's easy to build a driveway to access a road. If someone stops on the road you can go around them.

Or another perspective: postmodern developments accept the world as it is, while modern developments imagine a new better world.  A cohesive modern technology can be great, completist, robust; and without those kinds of systems we couldn't build what we have, it would all fall down as the geometrically cumulative nature of failure and multiple components would doom our systems to constant collapse.  But modern systems are also more apt to fail during their development, to solve the wrong problem, to demand tolerances that are too low, or to be too ambitious.

During the design of [TogetherJS](https://togetherjs.com) -- a realtime collaboration and co-browsing library -- I've approached it as a postmodern component.

The basic integration for TogetherJS isn't an API, or a data model: it's the DOM.  It involves scanning the page, looking for changes and events that are the exposed artifacts an application can't hide even if it wanted to.

There's a lot we can do with the standard DOM, but we aren't above integrating with other components.  We scan for [CodeMirror](http://codemirror.net/) and [ACE](http://codemirror.net/) editors by looking for the attributes they attach to elements. If you opt-in to YouTube support, we load their libraries to interact with Flash elements.  We can't support *everything*, but we're not taking any principled stance on how much we're willing to poke directly into other project's artifacts.

From the perspective of code isolation, we try to insulate TogetherJS from the page.  There's only one exposed object (`TogetherJS`), there is a specific set of methods on that (our public interface).  We bundle jQuery but do not use any version of jQuery already on the page, nor do we encourage anyone to use our version of jQuery.  We try to avoid getting caught up in any messiness of the host application, but we do not judge you for your messiness.

But we also expose TogetherJS.  You can import the modules, and we are not shy about exposing "private" parts of TogetherJS.  You can see all the messages that go back and forth between clients, regardless of what part of TogetherJS produces or consumes those messages.

This creates potential fragility, but we try to mitigate that by making it very easy make your own static, stable, frozen copy of the client code.  Once you get that working, it's working.  And this is why we work hard to keep the server as simple as possible.  Any smarts go in the client unless it is *absolutely* necessary that it go in the server.  (Arguably our server is modernist in design.)

## Why?

I'm not always sure whether to say "I" or "we" -- the architectural choices I'm describing are things that we came to consensus on as a team.  But exactly *why* we consensed on them I am not sure, I mostly know my own motivations for the architecture.

We have built TogetherJS with an eye towards the breadth of the web. We considered creating a collaborative editor (with some other special features), but we didn't really want to create a cool site, we wanted to create something that could magnify *other people's* cool sites. What cool sites?  We didn't know!  There has and continues to be a tension among all of us in the team as to how generic this tool can or should be: do we want to create an awesome tool for education, or support, or collaboration, or presentation, or...?

But we are not domain experts, and we have not created a domain-specific tool.  This itself is a tension I see on the web in general: developers create the best tools for the domain they understand, development.  Developing something like TogetherJS requires some considerable expertise in lots of technical areas (the DOM, browser security models, Javascript code organization, server integration, and so on).  The domain experts are experts in other things.  We want to empower those experts, and empower them to make tools, and not just use the tools that computer experts have made.  We hope TogetherJS can meet them halfway.

So we've created a tool that does a bunch of stuff by default, and doesn't care too much about how you went about building your site or app.  With just a little integration you get lots of functionality.  I think it is relatively hackable.

But we also want to enable really good collaboration, not just okay default collaboration.  This is why we build ways to customize the tool, and we're always open to new ways to do that customization.  We also require integration for the client-side dynamic parts of your application, as you can't seamlessly make everything work.  You *kind of* can make everything work (which I'll talk about below), but we want collaboration experience that is high-fidelity and context-aware.

Some examples where the context depends on the tools: you might want to let two people edit one document, but only one person can save it. You may want to allow two people to draw together, but simultaneously using different tools.  You might want to run a game where you score people separately... or maybe you want to score them together.  You might want a save to fork a document to some personal space, or you might want to keep the two people in sync.  I could go on about the choices an application might encounter for a long time.

We also want something like progressive enhancement: you start out right away with something that works, and then improve upon that.  The tool itself serves as an introduction to the tool.

## Roads Not Taken

Our basic task/intention with TogetherJS has been to enable real-time collaboration, co-browsing, co-presence.  Given that goal there are some two other viable approaches that I see, and that we didn't choose to pursue.  I'd classify each as more modernist than what we've done.

### The Realtime Database

One path is to create a modernist realtime collaborative foundation for your application's data.  In this category is [Firebase](http://firebase.com/), [Meteor](http://www.meteor.com/), the [Google Realtime API](https://developers.google.com/drive/realtime/), or [ShareJS](http://sharejs.org/) With these tools you synchronize your Javascript models across all clients, and the rest of the collaboration flows from that.

Obviously this approach this has a strong appeal, as the area is quite active.  The technique is robust, the tools can make a lot of guarantees about the models and consistency. To the degree you create reasonable deterministic predictable views on your models you can be assured of some consistency in the experience for all participants. Because the tools are low-level you can create a variety of collaboration experiences based on their core functionality.

There are three reasons we didn't want to take this approach:

1. These tools work best with greenfield development.  You have to make all your models aware of these external data and event sources. Some of the greatest benefits come when you rely on these tools for much of your persistence.

2. The tools don't apply very well to traditional websites. Sites that use HTTP requests and responses and dynamically generate HTML don't have browser-accessible models to be synchronized (they have server-side models, but those don't need to be synchronized and synchronizing them doesn't itself provide a realtime experience).

3. Database tools are not UI-aware.  A good collaboration experience doesn't just involve synchronized state, it requires that people *understand* what is happening, and understand when other people are invoking actions.

TogetherJS isn't incompatible with realtime databases.  In fact I think they should be very complementary: if your models are synchronized through a backend database you don't have to synchronize through TogetherJS, removing a lot of the more challenging integration work with Javascript-heavy applications.

### The Screenshare

Traditional screensharing happens at the pixel level, but I'm going to refer to something I'll call DOM Screensharing.  In this model the current/live state of the DOM is transferred from one browser to another.  I'll call the browser that starts the screensharing is the "source" and the browser that receives the DOM is the "viewer".

Examples of this are [Firefly](http://usefirefly.com/) or a now-dormant project of mine, [Browser Mirror](https://github.com/mozilla/browsermirror).  I believe some other customer support tools also use this technique, but in general the technique seems fairly obscure.

In this approach you look at all the elements on the source browser, scrub out any scripts or event handlers, maybe scrub hidden elements (or don't).  Then you serialize this and send it to the viewer.  The page is then recreated at a new URL, visually hard to distinguish from the original page, but it's "dead".  Like with video you send diffs to save effort.  You'll want special handling for form elements.  There are some other corner cases, but it's all relatively doable.  When I first got Browser Mirror working it surprised me how feasible it is, though it's certainly a 90/10 kind of problem.

The benefit of this approach is that It Just Works in a lot of cases. It works behind authentication, works when pages are personalized, and interacts pretty well with dynamic pages (which ultimately display dynamic elements in the browser through the DOM).  It is robust and broadly applicable.  It is modernist while being almost the polar opposite of the realtime database approach.

Because the viewer has a dead version of the application, it's not exactly easy to interact with.  Form fields are easy.  Rich controls though are *really hard*.  You *can* pass events back to the source browser.  In Browser Mirror you could click on anything on the viewer, and that click would be transmitted back to the source browser.  This actually worked in lots of cases, though with a lot of latency.  In some cases it couldn't realistically work -- can you sync mousedown, mousemove, or hover events?  Unfortunately it's also not possible to detect the presence of listeners on the DOM to detect what events are interesting, but even if you could those events are still too low-level.

Also the screensharing technique *because* of its broad applicability is not contextually aware.  Do you want to give the viewer access to the application as though they are the same user as the person using the source browser?  You can allow things like both people being scrolled to a different part of the page, but beyond that parallel work processes across a site or using overlapping tools is not really feasible.

Given these restrictions I was excited to learn from Browser Mirror but in TogetherJS to pursue something with the potential to be of a higher quality of experience.

Still I've considered resurrecting some portion of Browser Mirror within TogetherJS.  Embracing a diversity of techniques only makes the tool more postmodern ;)

## An Additive Approach

This acceptance of postmodern approaches means TogetherJS is being developed using an additive approach.  More stuff.  More configuration. More flags.  More use cases.

The additive approach nearly always produces better results with each addition.  But we all know where else it leads: unwieldy complexity, lack of focus, unreliable combinations.  The approach is perilous. Still we must learn from the past without overlearning from the past. As a project we have and continue to invest time in code organization, and remind ourselves of the dangers.  We're trying our best to engage with the inherent complexity rather than denying or avoiding it.

We'll see where it goes...
