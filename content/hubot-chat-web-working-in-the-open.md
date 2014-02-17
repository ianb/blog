Title: Hubot, Chat, The Web, and Working in the Open
Slug: hubot-chat-web-working-in-the-open
Date: 2014-02-14 12:26:00
Category: mozilla
Tags: hotdish

I was listening to a [podcast with some people from GitHub](http://hanselminutes.com/375/on-culture-and-remoteness-at-github-with-paul-betts-and-justin-spahr-summers) and I was struck by [Hubot](http://hubot.github.com/).

My understanding of what they are doing: Hubot is a chat bot -- in this case it hangs out in [Campfire](https://campfirenow.com/) chat rooms, but it could equally be an [IRC bot](http://en.wikipedia.org/wiki/Internet_Relay_Chat_bot).  It started out doing silly things, as bots often do, then started offering up status messages.  Eventually it got a command language where you could actually *do* things, like deploy servers.

As described, as Hubot grew new powers it has given people at GitHub new ways to work together with some interesting features:

1. Everyone else (in your room/group) can see you interacting with Hubot.  This gives people awareness of what each other are doing.

2. There's organic knowledge sharing.  When you watch someone doing stuff, you learn how to do it yourself.  If you ask a question and someone answers the question by doing stuff *in that same channel* then the learning is very concrete and natural.

3. You get a history of stuff that was done.  In GitHub's case they have custom logging and search interfaces for their Campfire channels, so there's a searchable database of everything that happens in chat rooms.

4. What makes search, learnability, and those interactions so useful is that *actions* are intermixed with *discussion*.  It's only modestly interesting that you could search back in history to find commands to Hubot.  It's far more interesting if you can see the context of those commands, the intentions or mistakes that lead to that command.

This setup has come back to mind repeatedly while I've been thinking about the concepts that [Aaron](http://www.whatthedruck.com/) and I have been working through with [TogetherJS](https://togetherjs.com/), my older [Browser Mirror project](https://github.com/mozilla/browsermirror) and now with [Hotdish, our new experiment in browser collaboration](https://github.com/mozilla/hotdish/).

With each of these I've found myself expanding the scope of what we capture and share with the group -- a single person's session (in Browser Mirror), multiple people working in parallel across a site (in TogetherJS), and then multiple people working across a browser session (Hotdish).  One motivation for this expansion is to place these individual web interactions in a social, and purposeful, context.  In the same way your Hubot interactions are surrounded by a conversation, I want to surround web interactions in a person's or group's thought process: to expose some of the *why* behind those actions.

What would it look like if we could get these features of Hubot, but with a workflow that encompasses any web-based tool?  I don't know, but a few thoughts taken from the previous list:

1. Expose your team-related browsing to your team.  Give other people some sense of what you are doing.  **Questions**: should you lead in with an explicit "I am trying to do X"?  Or can a well-connected team infer purpose or query you about your purpose given just a set of actions?  If you use a task management tool -- issue tracker, project management tool, CRM, etc -- is that launching point itself sufficient declaration of intent?

2. Let other people jump in, watching or participating in a session. You might start with an overview of their browsing activity, as it's just too much information to watch it all flow by, as you might be able to do with Hubot.  But then you want to support closer interaction.  It might be a little like being the passenger in a [pair programming](https://bitbucket.org/spooning/) situation, except instead of watching the other person by literally looking over their shoulder, we can let you opt in to watching remotely, and maybe allow for catching up or summarizing segments of the work, instead of requiring the two people to be linked in real time through the entire process.  **Questions**: how do you determine that something is going to be of interest to you?  Do the participants stay in well-defined leading/following roles, or do they switch?

3. Record actions.  Maybe this means "going on the record" sometimes. Ideally you'd be able to go on the record retroactively, like holding a recording locally and allowing you to put that recording in a global record if you decide it is needed.  One can imagine different levels of granularity possible for the recording.  A simple list of URLs you visited.  A recording of DOM states.  Some applications might be able to expose their own internal states that can be reconstructed, like in an automatically versioned resource like Google Docs the internal version numbers would be sufficient to see the context at that moment. **Questions**: how do you figure out what information is actually useful?  Is it possible to save everything and analyze later, or is that too much data (and traffic)?  Can we automatically curate?

4. Push enough communication through the browsing context and collaboration tool that there is a context for the actions.  This helps identify false starts (both to trim them, but also as an opportunity to help with future similar false starts), underlying purposes, bugs in the communication process itself ("I was trying to ask you to do X, but you thought I meant Y"), and give a resource to match future goals and purposes against past work.  **Questions**: does this make voice communication sub-optimal (compared to searchable text chat)?  Do we want to identify subtasks?  Or is it better to flatten everything to the group's purpose -- in some sense all tasks relate to the purpose?

Now you might ask: why web/browser focused instead of application-focused, or a tool that coordinates all these tasks (Google Docs/Apps? Wave?), or communication-tool-focused (like Hubot and Campfire are)?  Mostly because I think that web-based tools encompass *enough* and will consistently encompass more of our work, and because the web makes these things feasible -- it might be a half-assed semantic system, but it's more semantic than anything else. And of course the web is cloudy, which in this case is important because it means a third party (someone watching, or a recording) has a similar perspective to the person doing the action.  Personal computing is challenging because of a huge local state that is hard to identify and communicate to observers.

I think there's an idea here, and one that doesn't require recreating every tool individually to embody these ideas, but instead can happen at the platform level (the platform here being the browser).
