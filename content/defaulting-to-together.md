Title: Defaulting To Together
Slug: defaulting-to-together
Category: mozilla
Tags: hotdish
Date: 2014-02-17 12:31:00

I've been working on an experiment, [Hotdish](https://github.com/mozilla/hotdish/), for several weeks now with [Aaron Druck](http://www.whatthedruck.com/) and [Gregg Lind](https://twitter.com/gregglind).  I'm really excited about what we're doing, and in particular I'm excited about some of the principles we are bringing to the design.  Hotdish is an experiment in sharing a browser session among a group of peers -- you activate Hotdish on one browser window and everyone in your group sees what you do in that window, and we have tools to interact in the context of that session.

We've started the design with the expectation that Hotdish will be used with a group of people you want to be working with, and we expect that you trust this group of people.  We're not building this as an internet-wide tool, one where people will be trolling each other, or one where some people will be an order of magnitude more noisy than everyone else. So when we take a regular internet collaboration/cooperation idea and rephrase it in the context of Hotdish we think about how we can change default behaviors to make use of that trust.

Instead of using the tool to restrict people from bothering each other, we want to create a tool that **enables powerful new ways for one person to bother another** in the group.  If that's a problem, we expect you to deal with that socially rather than building something into the tool. ([Use your words!](http://www.youtube.com/watch?v=GtrSn8WwCa4))

### Pushing tabs instead of posting links

In Hotdish instead of *asking* someone to go to a link, you *push* a link to everyone.  The normal flow is you copy the URL, you go to your communication medium (instant message, chat room, shared document), you paste the URL, and then you beg everyone to please click it.  Then you ask if everyone is really there yet? Then you make sure everyone knows it wasn't the second-to-last link, but the very last link you pasted.  Just this minute.  Wait, no, not the link that other person pasted in, though I suppose you should all go there too. OK, are we all on the same page now?  Oh wait, I just made a change, can everyone reload?

No: with Hotdish you just push the link, *make* it open for everyone, and once you've done it you'll even get a second confirmation because we show who on a page.  The only problem is right now we open a background tab (because forcing a tab switch is too jarring), but I want to figure out how to push even harder, to let people be more assertive if they choose. Like maybe if you push twice in succession everyone gets a big "Alice really wants you to see: [page]" notification that you can't really ignore, or if you explicitly ignore it then Alice knows you decided to ignore it.

### Presenting and peeking in

Another example where we're being aggressive: in Hotdish you can *present* a page to someone, showing them exactly what you see (including details that might not be the same for them if they went to the same URL).  But you can also *view* someone else's page. When you "view" a page you are viewing the page exactly as the other person sees it (as opposed to simply visiting the same URL as the other person).  It's like the ability to peek over anyone's shoulder.

### Audio/video CB/walkie-talkie mode

We haven't added any voice tools to Hotdish yet.  It didn't seem like the heart of what we were trying to explore -- of course we knew we'd want to enable communication among the group, but we didn't think we'd bring anything new, and so the effort didn't feel like it would bring much.  But then we also hadn't thought about how we might rethinking the ideas in this concept, instead we were just borrowing what seemed like the obvious interface.

After some thought a feature I'd like to try is a talk-at-anyone mode. This is a little like [Sqwiggle](https://www.sqwiggle.com/), where you can talk with anyone without confirmation.  Still I find the Sqwiggle model a little much, where anyone can watch me on their own volition. Maybe it's fine, I might be wrong.  But I'm more open to anyone talking *to* me, and then requiring confirmation before they can listen or watch me. Having someone yell at me spontaneously would probably be annoying, but that's a social problem.

### Sharing a record of your activity

The core feature of Hotdish is that everyone can see any of the pages you open, and see some of your navigational behavior -- like when you go to a new page or change active tabs.  Realistically you would not do everything in your Hotdish window (Hotdish exposes only one browser window to the group -- everything you do in other windows remains personal), but I hope that Hotdish could allow people to do more things in front of their peers.  For instance, from an article [*Making Remote Work Work*](https://source.opennews.org/en-US/learning/making-remote-work-work/):

> It's my earnest belief that some people will have higher expectations for you because you work remotely. It's very easy for them to believe you're in your underwear playing Final Fantasy instead of slogging through the documentation for Django. Not all work has obvious output and when they can't see you at your desk, it's tempting to log those blank hours as time wasted.

One of the hidden parts of work (paid work, school work, or volunteer work) that I want to expose with Hotdish is **research**. Research is slogging through the docs, finding out if some idea you've had *maybe* exists (and perhaps finding out doesn't), it's finding the right term, looking up a date or meeting... it's all these little things we constantly do.  But those things are never the focus of "collaboration".  Research is the stuff you do *before* you can tell anyone what you've learned. It gets seen as a prerequisite to accomplishing real work, instead of a part of what it means to *do* real work.  And yet when asked everyone will defend the value of research: we know we should value this thing, but because we have a hard time seeing it too often we do not.

By putting your work in front of anyone -- even if you aren't trying to share anything with anyone, or have not come to any determination -- I hope we can make research as collaborative as conclusions are.

### Recording history

A feature we are exploring is called the *Activity Log*: a persistent record what happens in the group. Our first foray into this is somewhat comically primitive, we are just pasting the activities into an [Etherpad](http://etherpad.org/) document.  It's primitive but I'm going to have a hard time getting myself to replace it because there's something that just feels really *right* about using an editor.

After my [last post](http://www.ianbicking.org/blog/2014/02/hubot-chat-web-working-in-the-open.html) I got [a comment](https://plus.google.com/+IanBicking/posts/NvnBBQ6eCFe) challenging me to consider the "social implications of showing others one's mistakes".  A fair challenge, and honestly I have *tried* to ignore that for all the reasons I'm talking about here.  But I think in this silly model of recording activities to a text editor there is also a response to this: we keep a record, along with everything else we do, because we want to build a model for a constructive and supportive group to enhance their work together.  But a constructive and supportive group is also based on trust.  One of the ways we demonstrate trust is with things like using an editable document instead of a strict log: we should trust each other to edit history, and edit out history.  We should trust that people use that power well.

In a live environment like Hotdish it's hard to actually make sure no one saw something.  You open a link, it shows up to everyone that moment.  You close it, and maybe we can figure out a way to keep it out of history, or allow you to remove it from history, but we can't remove it from the memories of everyone who saw it.  But this is another kind of politeness: we ask that people respect even our retroactive attempts at privacy.  This is something that Facebook, for instance, works pretty hard at -- they do their best to make deleted content really disappear.  Programmer-designed tools tend to be horrible at this.  I think because the programmer knows you can't *really* delete history, you can't know what has been recorded on other clients, you can't erase people's memory.  They don't put value on politely agreeing to forget.  And so programmer-designed tools almost never let you edit history.  We will not make this mistake.

So that's some of what we're thinking.  Some of these ideas aren't going to work out.  Dogfooding will be essential.  But we can't see how far we can go with putting people together unless we go too far and then pull back.

I'm interested in other ideas for somewhat uncomfortably intimate browser-mediated sharing experiences.  Have any?
