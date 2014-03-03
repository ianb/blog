Title: Collaboration as a Skeuomorphism for Agents
Slug: collaboration-as-a-skeuomorphism-for-agents
Date: 2014-02-21 15:06:00
Category: mozilla
Tags: hotdish

In concept videos and imaginings about the Future Of Computing we often see [Intelligent Agents](https://en.wikipedia.org/wiki/Software_agent#User_agents_.28personal_agents.29): smart computer programs that work on your behalf.

But to be more specific, I'm interested in agents that don't work through formal rules.  An [SMTP daemon](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol#Outgoing_mail_SMTP_server) acts on your behalf routing messages to your intended destination, but they do so in an entirely formal way, one that is "correct" or "incorrect".  And if such agents act with initiative, it is initiative based on formal rules, and those formal rules ultimately lead back to the specific intentions of whoever wrote the rules, the rules defined in terms of unambiguous inputs.

Progress on intelligent agents seems to be thin.  Gmail sorts some stuff for us in a "smart" way.  There are some smart command-based interfaces like Siri, but they are mostly smart frontends for formalized backends, and they lack initiative.  Maybe we get an intelligent alert or two, but it's a tiny minority given all the dumb alerts we get.

One explanation is that we don't have intelligent agents because we haven't figured out intelligence.  But whatever, intelligent is as intelligent does, if this was the only reason then I would expect to see more dumb *attempts* at intelligent agents.

It seems worth approaching this topic with more [mundane attempts](http://johncarlosbaez.wordpress.com/2013/09/29/levels-of-excellence/). But there are reasons we ("we" being "us technologists") don't.

### Intelligent agents will be chronically buggy

If we want agents to do things where it's not clear what to do, then sometimes they are going to do the wrong thing.  It might be a big-scale wrong thing, like they buy airplane tickets and we wanted them to buy concert tickets.  Or a small thing, like we want them to buy airplane tickets and something changed about the interface to buy those tickets and now the agent is just confused.

Intelligent agents will be accepting rules from the people they are working for, from normal people.  Then normal users become programmers in a sense. Maybe it's a hand-holding cute and fuzzy programming language based on natural language, but it is the nature of programming that you will create your own bugs.  Only a minority of bugs are created because you expressed yourself incorrectly, most bugs are because you thought it through incorrectly, and no friendly interface can fix that.

How then do we deal with buggy intelligent agents, while also allowing them to do useful things?

There are two things that come to mind: logging and having the agent check before doing something.  Both are hard in practice.

**Logging**: this lets you figure out who was responsible for a bad action, or the reasoning behind an action.

Programmers do this all the time to understand their programs, but for an intelligent agent the user is also a developer.  When you ask your agent to watch for something, or you ask it to act under certain circumstances, then you've programmed it, and you may have programmed it wrong.  Fixing that doesn't mean looking at stack traces, but there has to be some techniques.

You don't want to have to take users into the mind of the person who programmed the agent.  So how can you log actions so they are understandable?

**Checking**: you'll want your agent to check in with you before doing some things.  Like before actually buying something. Sometimes you'll want the agent to check in even more often, not because you expect the agent to do something impactful, but because it might do something impactful due to a bug.  Or you are just getting to know each other.

Among people this kind of check-in is common, and we have a rich language to describe intentions and to implicitly get support for those intentions.  With computer interactions it's a little less clear: how does an agent talk about what it thinks it *should* do? How do we know what it says it thinks it should do is what it actually plans to do?

### Collaboration

We deal with lots of intelligent agents all the time: each other.  We can give each other instructions, and in this way anyone can program another human.  We report back to each other about what we did.  We can tell each other when we are confused, or unable to complete some operation. We can confirm actions.  Confirmation is almost like functional testing, except often it's the person who receives the instructions who initiates the testing.  And all of this is rooted in *empathy*: understanding what someone else is doing because it's more-or-less how you would do it.

It's in these human-to-human interactions we can find the metaphors that can support computer-based intelligent agents.

But there's a problem: computer-based intelligent agents perform best at computer-mediated tasks.  But we usually work alone when we personally perform computer-mediated tasks.  When we coordinate these tasks with each other we often resort to low-fidelity check-ins, an email or IM.  We don't even have ways to delegate except via the wide categories of permission systems.  If we want to build intelligent agents on the intellectual framework of person-to-person collaboration, we need much better person-to-person collaboration for our computer-based interactions.

(I will admit that I may be projecting this need onto the topic because I'm very interested in person-to-person collaboration.  But then I'm writing this post in the hope I can project the same perspective onto you, the reader.)

My starting point is the kind of collaboration embodied in [TogetherJS](https://togetherjs.com) and some follow-on ideas I'm [experimenting with](https://togetherjs.com/hotdish/). In this model we let people see what each other are "doing" -- how they interact with a website.  This represents a kind of log of activity, and the log is presented as human-like interactions, like a recording.

But I imagine many ways to enter into collaboration: consider a mode for teaching, where one person is trying to tell the other person how to do something.  In this model the helper is giving directed instructions ("click here", "enter this text").  For teaching it's often better to tell than to do.  But this is also an opportunity to check in: if my intelligent agent is instructing me to do some action (perhaps one I don't entirely trust it to do on my behalf) then I'm still confirming every specific action.  At the same time the agent can benefit me by suggesting actions I might not have figured out on my own.

Or imagine a collaboration system where you let someone pull you in part way through their process.  A kind of "hey, come look at this." This is where the diligent intelligent agent can spend its time checking for things, and then bring your attention when it's appropriate.  Many of the same controls we might want for interacting with other people (like a "busy" status) apply well to the agent who also wants to get our attention, but should maybe wait.

Or imagine a "hey, what are you doing, let me see" collaboration mode, where I invite myself to see what you are doing.  Maybe I've set up an intelligent agent to check for some situation.  Anytime you set up *any* kind of detector like this, you'll wonder: is it really still looking?  Is it looking for the right thing?  I think it should have found something, why didn't it?  This is where it would be nice to be able to peek into the agent's actions, to watch it doing its work.

If applications become more collaboration-aware there are further possibilities.  For instance, it would be great if I could participate in a collaboration session in GitHub and edit a file with someone else.  Right now the other person can only "edit" if they also have permission to "save".  As GitHub is now this makes sense, but if collaboration tools were available we'd have a valid use case where only one of the people in the collaboration session could save, while the other person can usefully participate.  There's a kind of cooperative interaction in that model that would be perfect for agents.

We can imagine agents participating already in the collaborative environments we have.  For instance, when a continuous integration system detects a regression on a branch destined for production, it could create its own GitHub pull request to revert the changes that led to a regression.  On Reddit there's a [bot](https://github.com/Deimos/AutoModerator) that I've encountered that allows Subreddits to create fairly subtle rules, like allow image posts only on a certain day, ban short comments, check for certain terms, etc.  But it's not something that blocks submission (it's not part of Reddit itself), instead it uses the same moderator interface that a person does, and it can use this same process to explain to people why their posts were removed, or allow other moderators to intervene when something valid doesn't happen to fit the rules.

### What about APIs?

In everything I've described agents are interacting with interfaces in the same way a human interacts with the interface.  It's like everything is a screen scraper.  The more common technique right now is to use an API: a formal and stabilized interface to some kind of functionality.

I suggest using the interfaces intended for humans, because those are the interfaces humans understand.  When an agent wants to say "I want to submit this post" if you can show the human the filled-in form and show that you want to hit the submit button, you are using what the person is familiar with.  If the agent wants to say "this is what I looked for" you can show the data in the context the person would themselves look to.

APIs usually don't have a staging process like you find in interfaces for humans.  We don't expect humans to act correctly.  So we have a shopping cart and a checkout process, you don't just submit a list of items to a store.  You have a composition screen with preview, or interstitial preview.  Dangerous or destructive operations get a confirmation step -- a confirmation step that could be just as applicable of a warning for an agent as it is for a human.

None of this invalidates the reasons to use an API.  And you can imagine APIs with these intermediate steps built in.  You can imagine an API where each action can also be marked as "stage-only" and then returns a link where a human can confirm the action.  You can imagine an API where each data set returned is also returned with the URL of the equivalent human-readable data set.  You can imagine delegation APIs, where instead of giving a category of access to an agent via OAuth, you can ask for some more selective access. All of that would be great, but I don't think there's any movement towards this kind of API design.  And why would there be? There's no one eager to make use of it.

### That fancy Skeuomorphism term from the title

A [Skeuomorphism](https://en.wikipedia.org/wiki/Skeuomorph#Digital_skeuomorphs) is something built to be reminiscent of an existing tool, not out of any necessity, but because it provides some sense of familiarity.  Our calendar software looks like a physical calendar.  We talk of "folders".  We make our buttons look depressable even though it is all a simulation of a physical control.

This has come to mind when I talk of using the same metaphors for interacting with a computer program that we do for interacting with a human.

When we need a new way for people to work with computers a lot of success has come from finding bridges between our existing practices and a computer-based practice.  The desktop instead of the command line, the use of cards on mobile, the many visual metaphors that we use, the way we phrase emails as letters, etc.  Sometimes these are just scaffolding while people get used to the new systems (maybe [flat design](http://gizmodo.com/what-is-flat-design-508963228) is an example).  And of course you can pick the wrong metaphors (or [go too far](http://www.youtube.com/watch?v=ZegWedG-jk4))

In this case the metaphor isn't using the representation of a physical object in the computer, but using the representation of a fellow human as a stand-in for a program.

The goal is enabling a whole list of *maybe* actions.  Maybe "intelligent" doesn't really mean "knowledgable and smart" but "is not formally verifiable as correct" and "successfully addresses a domain that cannot be fully understood".  You don't need formal AI for these kinds of tasks.  Heuristics don't need to be sophisticated.  But we need interfaces where a computer can make *attempts* without demanding correctness.  And human interaction seems like the perfect model for that.
