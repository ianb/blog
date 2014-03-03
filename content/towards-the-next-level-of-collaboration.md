Title: Towards the Next Level of Collaboration
Slug: towards-next-level-of-collaboration
Date: 3014-03-03 12:40:00
Category: mozilla
Tags: hotdish

With [TogetherJS](https://togetherjs.com) we've been trying to make a usable tool for the web we have, and the browsers we have, and the web apps we have.  But we're also accepting a lot of limitations.

For a particular scope the limitations in TogetherJS are reasonable, but my own goals have been more far-reaching.  I am interested in collaboration with as broad a scope as the web itself. ([But no broader than the web because I'm kind of biased.](http://www.ianbicking.org/blog/2014/02/saying-goodbye-to-python.html))
"Collaboration" isn't quite the right term -- it implies a kind of active engagement in creation, but there's more ways to work together than collaboration.  TogetherJS was previously called TowTruck, but we wanted to rename it to something more meaningful.  While brainstorming we kept coming back to names that included some form of "collaboration" but I strongly resisted it because it's such a mush-mouthed term with too much baggage and too many preconceptions.

When we came up with "together" it immediately seemed right. Admittedly the word feels a little cheesy (*it's a web built out of hugs and holding hands!*) but it covers the broad set of activities we want to enable.

With the experience from TogetherJS in mind I want to spend some time thinking about what a less limited tool would look like.  Much of this has become manifest in [Hotdish](https://github.com/mozilla/hotdish), and the notes below have informed its design.

## Degrees of collaboration/interaction

Intense collaboration is cool, but it's not comprehensive.  I don't *want* to always be watching over your shoulder.  What will first come to mind is privacy, but that's not interesting to me. I would rather address privacy by helping you scope your actions, let you interact with your peers or not and act appropriately with that in mind.  I don't want to engage with *my* collaborators all the time because it's boring and unproductive and my eyes glaze over.  I want to engage with other people *appropriately*: with all the intensity called for given the circumstances, but also all the passivity that is also sometimes called for.

I've started to think in terms of categories of collaboration:

### 1. Asynchronous message-based collaboration

This includes email of course, but also issue trackers, planning tools, any notification system. If you [search for "collaboration software"](https://www.google.com/search?q=collaboration+software) this is most of what you find, and much of the innovation is in representing and organizing the messages.

I don't think I have any particularly new ideas in this well-explored area.  That's not to say there aren't lots of important ideas, but the work I want to do is in complementing these tools rather than competing with them.  But I do want to note that they exist on this continuum.

### 2. **Ambient awareness**

This is the awareness of a person's presence and activity. We have a degree of this with Instant Messaging and chat rooms (IRC, Campfire, etc).  But they don't show *what we are actively doing*, just our presence or absence, and in the case of group discussions some of what we're discussing with other people.

Many tools that indicate presence also include status messages which would purport to summarize a person's current state and work.  I've never worked with people who keep those status messages updated.  It's a very explicit approach.  At best it devolves into a record of what you *had been doing*.

A more interesting tool to make people's presence more *present* is [Sqwiggle](https://www.sqwiggle.com/), a kind of always-on video conference.  It's not exactly always-on, there is a low-fidelity video with no audio until you start a conversation with someone and it goes to full video and audio.  This way you know not only if someone is actually sitting at the computer, but also if they are eating lunch, if they have the furrowed brows of careful concentration, or are frustrated or distracted.  Unfortunately most people's faces only show that they are looking at a screen, with the slightly studious but mostly passive facial expressions that we have when looking at screens.

Instant messaging has grown to include an additional the presence indicator: *I am currently typing a response*.  A better fidelity version of this would indicate if I am typing right now, or if I forgot I started typing and switched tabs but left text in the input box, or if I am trying hard to compose my thoughts (typing and deleting), or if I'm pasting something, or if I am about to deliver a soliloquy in the form of a giant message.  (Imagine a typing indicator that gives a sense of the number of words you have typed but not sent.)

I like that instant messaging *detects* your state automatically, using something that you are already engaged with (the text input box).  Sqwiggle has a problem here: because you aren't trying to project any emotions to your computer screen, Sqwiggle catches expressions that don't mean anything.  We can engage with our computers in different ways, there's something there to express, it's just not revealed on our faces.

I'd like to add to the activity indicators we have.  Like the pages (and web apps) you are looking at (or some privacy-aware subset).  I'd like to show *how* you are interacting with those pages.  Are you flopping between tabs?  Are you skimming?  Scrolling through in a way that shows you are studying the page?  Typing?  Clicking controls?

I want to show something like the body language of how you are interacting with the computer.  First I wondered if we could interpret your actions and show them as things like "reading", "composing", "being pissed off with your computer", etc.  But then I thought more about body language.  When I am angry there's no "angry" note that shows up above my head.  A furrowed brow isn't a message, or at least mostly not a message.  Body language is what we read from cues that aren't explicit.  And so we might be able to show *what* a person is doing, and let the person watching figure out *why*.

### 3. Working in **close parallel**

This is where both people (or more than 2 people) are actively working on the same thing, same project, same goal, but aren't directly supporting each other at every moment.

When you've entered into this level of collaboration you've both agreed that you are working together -- you're probably actively talking through tasks, and may regularly be relying on each other ("does what I wrote sound right?" or "did you realize this test is failing" etc).  A good working meeting will be like this.  A bad meeting would probably have been better if you could have stuck to ambient awareness and promoted it to a more intense level of collaboration only as needed.

### 4. **Working directly**

This is where you are both locked on a *single* task.  When I write something and say "does what I wrote sound right?" we have to enter this mode: you have to look at exactly what I'm talking about.  In some sense "close parallel" may mean "prepared to work directly".

I have found that video calls are better than audio-only calls, more than I would have expected.  It's not because the video content is interesting.  But the video makes you work directly, while being slightly uncomfortable so you are encouraged to acknowledge when you should end the call.  In a way you want your senses filled.  Or maybe that's my propensity to distraction.

There's a lot more to video calls than this (like the previously mentioned body language).  But in each feature I suspect there are parallels in collaborative work.  Working directly together should show some of the things that video shows when we are focused on a *conversation*, but can't show when we are focusing on *work*.

### 5. **Demonstrating** to another person

This is common for instruction and teaching, but that shouldn't be the only case we consider.  In Hotdish we have often called it "presenting" and "viewing".  In this mode someone is the driver/presenter, and someone is the passenger/viewer.  When the presenter focuses on something, you want the viewer to be aware of that and follow along.  The presenter also wants to be confident that the viewer is following along.  Maybe we want something like how you might say "uh huh" when someone is talking to you -- if a listener says nothing it will throw off the talker, and these meaningless indications of active listening are important.

Demonstration could just be a combination of direct work and social convention.  Does it need to be specially mediated by tools? I'm not sure.  Do we need a talking stick?  Can I take the talking stick? Are these interactions like a conversation, where sometimes one person enters into a kind of monologue, but the rhythm of the conversation will shift?  If we focus on the demonstration tools we could miss the social interactions we are trying to support.

### Switching modes

Between each of these styles of interaction I think there must be some kind of positive action.  A natural promotion of demotion of your interaction with someone should be mutual.  (A counter example would be the dangling IM conversation, where you are never sure it's over.)

At the same time, the movement between modes also builds your shared context and your relationship with the other person.  You might be proofing an article with another person, and you say: "clearly this paragraph isn't making sense, let me just rewrite it, one minute" -- now you know you are leaving active collaboration, but you also both know you'll be reentering it soon.  You shouldn't have to record that expectation with the tool.

I'm reluctant to put boundaries up between these modes, I'd rather tools simply *inform* people that modes are changing and not *ask* if they can change.  This is part of the principles behind [Defaulting To Together](http://www.ianbicking.org/blog/2014/02/defaulting-to-together.html).

## Ownership

At least in the context of computers we often have strong notions of *ownership*.  Maybe we don't have to -- maybe it's because we have to hand off work explicitly, and maybe we have to hand off work explicitly because we lack fluid ways to interact, cooperate, delegate.

With good tools in hand I see "ownership" being exchanged more regularly:

* I find some documentation, then show it to you, and now it's yours to make use of.

* I am working through a process, get stuck, and need your skills to finish it up.  Now it's yours.  But you might hand it back when you unstick me.

* You are working through something, but are not permitted to complete the operation, you have to hand it over to me for me to complete the last step.

Layered on this we have the normal notions of ownership and control -- the login accounts and permissions of the applications we are using. Whether these are in opposition to cooperation or maybe complementary I have not decided.

## Screensharing vs. Peer-to-Peer

Perhaps a technical aside, but when dealing with real-time collaboration (not asynchronous) there are two distinct approaches.

**Screensharing** means one person (and one computer) is "running" the session -- that one person is logged in, their page or app is "live", everyone else sees what they see.

Screensharing doesn't mean other people can't interact with the screen, but any interaction has to go through the owner's computer. In the case of a web page we can share the DOM (the current visual state of the page) with another person, but we can't share the Javascript handlers and state, cookies, etc., so most interactions have to go back through the original browser.  Any side effects have to make a round trip.  Latency is a problem.

It's hard to figure out exactly what interactivity to implement in a screensharing situation. Doing a view-only interaction is not too hard.  There are a few things you can add after that -- maybe you let someone touch a form control, suggest that you follow a link, send clicks across the wire -- but there's no clear line to stop at. Worse, there's no clear line to *express*.  You can implement certain *mechanisms* (like a click), but these don't always map to what the user thinks they are doing -- something like a drag might involve a mousedown/mousemove/mouseup event, or it might be implemented [directly as dragging](https://developer.mozilla.org/en-US/docs/DragDrop/Drag_and_Drop). Implementing one of those interactions is a lot easier than the other, but the distinction means nothing to the user.

When you implement incomplete interactions you are setting up a situation where a person can do something in the original application that viewers can't do, even though it *looks* like the real live application.  An uncanny valley of collaboration.

I've experimented with DOM-based screen sharing in [Browser Mirror](https://github.com/mozilla/browsermirror), and you can see this approach in a tool like [Surfly](https://surfly.com/). As I write this a minimal version of this is available in Hotdish.

In **peer-to-peer** collaboration both people are viewing their own version of the live page.  Everything works exactly like in the non-collaborative environment.  Both people are logged in as themselves.  This is the model [TogetherJS](https://togetherjs.com) uses, and is also present as a separate mode in Hotdish.

This has a lot of obvious advantages over the problems identified above for screensharing.  The big disadvantage is that hardly anything is collaborative by default in this model.

In the context of the web the building blocks we *do* have are:

* URLs.  Insofar as a URL defines the exact interface you look at, then putting both people at the same URL gives a consistent experience.  This works great for applications that use lots of server-side logic.  Amazon is pretty great, for example, or Wikipedia. It falls down when content is substantially customized for each person, like the Facebook frontpage or a flight search result.

* Event echoing: events aren't based on any internal logic of the program, they are something initiated by the user.  So if the user can do something, a remote user can do something.  Form fields are the best example of this, as there's a clear protocol for doing form changes (change the value, fire a `change` event).

But we *don't* have:

* Consistent event *results*: events aren't state changes, and transferring events about doesn't necessarily lead to a consistent experience. Consider the modest toggle control, where a click on the toggler element shows or hides some other element.  If our hidden states are out of sync (e.g., my toggleable element is hidden, yours is shown), sending the click event between the clients *keeps* them consistently and perfectly out of sync.

* Consistent underlying object models.  In a single-page app of some sort, or a whatever fancy Javascript-driven webapp, a lot of what we see is based on Javascript state and models that are not necessarily consistent across peers.  This is in contrast to old-school server-side apps, where there's a good chance the URL contains enough information to keep everything consistent, and ultimately the "state" is held on a single server or database that both peers are connecting to. But we can't sync the client's object models, as they are not built to support arbitrary modification from the outside.  Apps that use a real-time database work well.

To make this work the application usually has to support peer-to-peer collaboration to some degree.  A [messy approach](http://www.ianbicking.org/blog/2013/10/togetherjs-a-postmodern-tool.html) can help, but can never be enough, not complete enough, not robust enough.

So peer-to-peer collaboration offers potentially more powerful and flexible kinds of collaboration, but only with work on the part of each application.  We can try to make it as [easy as possible](https://hacks.mozilla.org/2013/10/introducing-togetherjs/), and maybe integrate with tools or libraries that support the kinds of higher-level synchronization we would want, but it's never reliably easy.

## Synchronized vs. Coordinated Experiences

Another question: what kind of experiences do we *want* to create?

The most obvious real-time experience is: everything sees the same thing. Everything is fully synchronized.  In the screensharing model this is what you always get and what you *have* to get.

The obvious experience is probably a good starting point, but shouldn't be the end of our thinking.

The trivial example here is the cursor point.  We can both be editing content and viewing each other's edits (close to full sync), but we don't have to be at exactly the same place.  (This is something traditional screensharing has a hard time with, as you are sharing a *screen of pixels* instead of a DOM.)

But other more subtle examples exist.  Maybe only one person has the permission to save a change.  A collaboration-aware application might allow both people to edit, while still only allowing one person to save. (Currently editors will usually be denied to people who don't have permission to save.)

I think there's fruit in playing with the timing of actions.  We don't have to replay remote actions exactly how they occurred.  For example, in a Demonstration context we might detect that when the driver clicks a link the page will change.  To the person doing the click the order of events is: find the link, focus attention on the link, move cursor to the link, click.  To the viewer the order of events is: cursor moves, maybe a short click indicator, and *boom* you are at a new page. There's much less context given to the viewer.  But we don't have to display those events with the original timing for instance we could let the mouse hover over its target for a more extended amount of time on the viewer.

High-level (application-specific) representation of actions could be available.  Instead of trying to express what the other person is doing through every click and scroll and twiddling of a form, you might just say "Bob created a new calendar event".

In the context of something like a bug tracker, you might not want to synchronize the comment field.  Instead you might want to show individual fields for all participants on a page/bug.  Then I can see the other person's in-progress comment, even add to it, but I can also compose my own comment as myself.

This is where the peer-to-peer model has advantages, as it will (by necessity) keep the application in the loop.  It does not demand that collaboration take one form, but it gives the application an environment in which to build a domain-specific form of collaboration.

We can imagine moving from screenshare to peer-to-peer through a series of enhancements.  The first might be: let applications opt-in to peer-to-peer collaboration, or implement a kind of transparent-to-the-application screensharing, and from there tweak. Maybe you indicate some scripts should run on the viewer's side, and some compound UI components can be manipulated.  I can imagine with a component system like [Brick](http://mozilla.github.io/brick/) where you could identify safe ways to run rich components, avoiding latency.

## How do you package all this?

Given tools and interactions, what is the actual context for collaboration?

TogetherJS has a model of a persistent session, and you invite people to that session.  Only for technical reasons the session is bound to a specific domain, but not a specific page.

In Hotdish we've used a group approach: you join a group, and your work clearly happens in the group context or not.

One of the interesting things I've noticed when getting feedback about TogetherJS is that people are most interested in controlling and adding to how the sessions are setup.  While, as an implementor, I find myself drawn to the tooling and specific experiences of collaboration, there's just as much value in allowing new and interesting groupings of people.  Ways to introduce people, ways to start and end collaboration, ways to connect to people by role instead of identity, and so on.

Should this collaboration be a conversation or an environment?  When it is a *conversation* you lead off with the introduction, the "hello" the "so why did you call?" and finish with "talk to you later" -- when it is an *environment* you enter the environment and any coparticipants are just there, you don't preestablish any specific reason to collaborate.

## And in conclusion...

I'm still developing these ideas.  And for each idea the real test is if we can create a useful experience.  For instance, I'm pretty sure there's some ambient information we want to show, but I haven't figured out what.

Experience has shown that simple history (as in an activity stream) seems too noisy.  And is history shown by group or person?

In the past I unintentionally exposed all tab focus and unfocus in TogetherJS, and it felt weird to both expose my own distracted state and my collaborator's distraction.  But part of why it was weird was that in some cases it was simply distraction, but in other cases it was useful multitasking (like researching a question in another tab). Was tab focus too much information or too little?

I am still in the process of figuring out how and where I can explore these questions, build the next thing, and the next thing after that -- the tooling I envision doesn't feel impossibly far away, but still more than one iteration of work yet to be done, maybe many more than one but I can only see to the next peak.

Who else is thinking about these things?  If you are, or you know someone who is, please [get in contact](mailto:ian@ianbicking.org) -- I'm eager to talk specifics with people who have been thinking about it too, but I'm not sure how to find these people.
