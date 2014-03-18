Title: How We Use GitHub Issues To Organize a Project
Slug: use-github-issues-to-organize-a-project
Date: 2014-03-18 4:26

On a [couple](https://github.com/mozilla/togetherjs) [projects](https://github.com/mozilla/hotdish) I've used GitHub Issues as the primary technique to organize the project, and I've generally enjoyed it, but it took some playing around to come up with a process. You, reader, may also like this process, so I will describe it for you.

GitHub Issues has a slim set of features:

- Issues, of course
- Issues can be assigned
- Issues belong to zero or one milestone
- Issues can have any number of tags

This isn't a lot to work with, so we had to play around a bit to figure out a good pattern.

## Milestones

We decided there was only a couple things we actually wanted to track:

1. What are we doing right now?
2. What aren't we doing right now?
3. What aren't we sure about?

We have to regularly reevaluate where issues fit into these categories, so we break category 2 into:

2a. Stuff we'll probably do soon

2b. Stuff we probably won't do soon

We tried using labels for this but it was no good.  There's only a small number of queries you can do with labels, foiling any clever ideas.  Instead we have milestones:

**Stuff we are doing right now**: this is the "main" milestone.  We give it a name (like *Alpha 2* or *Strawberry Rhubarb Pie*) and we write down what we are trying to accomplish with the milestone.  We create a new milestone when we are ready for the next iteration.

**Stuff we'll probably do soon**: this is a standing "Next Tasks" milestone.  We never change or rename this milestone.

**Stuff we probably won't do soon**: this is a standing "Blue Sky" milestone.  We refer to these tickets and sometimes look through them, but they are easy to ignore, somewhat intentionally ignored.

**What aren't we sure about?**: issues with no milestone.

We use a permanent "Next Tasks" milestone (as opposed to renaming it to "Alpha 3" or actual-next-iteration milestone) because we don't want to presume or default to including something in the *real* next iteration.  When we're ready to start planning the next iteration we'll create a new milestone, and only deliberately move things into that milestone.

## The Triage Meeting

We use the triage process to organize many of our meetings.  The issues give us our first run at an agenda.

### "Needs Discussion"

We have a label: **needs discussion**.  We start each meeting by querying everything (regardless of milestone) that has that label, and discussing each item.  Once we're done discussing we usually remove the label, but sometimes we couldn't decide whatever we wanted to decide and so we leave the label there, pushing the item to the next meeting.

It's helpful to use "needs discussion" liberally.  It might be for some big things, like we add a ticket "Decide who our target market is" -- that's kind of a big deal, and we might keep adding notes over the course of weeks.  But it might just be a small issue where there seems to be some confusion or an open question.

These are small team meetings, so we aren't trying to use this to close off discussion or restrict the agenda, and anyone can bring up a topic at any time.  But if you want to be sure to talk about something then opening and labeling a ticket is as good a way as anything. Also the issues become our meeting notes (they aren't date-organized meeting notes, but I seldom want date-organized meeting notes).

### Issues without a milestone

GitHub lets you query all issues that have no milestone.  It doesn't let you query issues without a particular label, which made our label-based attempts at organization unproductive.

So next in the meeting we go through each item without a milestone, oldest first.  Sometimes we skim, and if someone says "next tasks?" then usually the answer is "yes".

Outside of a meeting if any of us sees something in Next Tasks or Blue Sky that we should do sooner, that person clears the milestone.  It's often better to clear the milestone than to just assign it to the current iteration, as it brings it in front of the entire team.

An exception is when someone breaks a big issue down into smaller tasks, or creates a dependent bug -- then whoever does that usually assigns the milestone at the same time.

### Starting a new iteration

When we're ready to start a new iteration we first create a new milestone, and agree on our goal.

Sometimes if we're not sure what our goal for the next iteration is we'll create a ticket, "decide on goal for the next iteration" (and mark it needs-discussion of course).

We'll go through the meeting as normal, then look at any open issues in the previous iteration.  It's pretty common that we move these issues to "Next Tasks" instead of the next iteration.  Issues that didn't get fixed often turned out to not be as important as we thought.

We sometimes go through Next Tasks, but it can also take too long to do that together.  Part of me thinks we should slog through anyway, and use that as a chance to clean up Next Tasks -- move stuff to Blue Sky, or close issues we no longer plan to address at all, or check for things that have already been fixed.

But instead one of us will often do an initial triage on Next Tasks, clearing the milestone for anything that might be worth looking at again.  Also it's a chance to close issues and find duplicates.  It's good to err on the side of clearing the milestone.  It's best not to assign a task directly to the next iteration because even talking about a ticket for a moment is useful.

Blue Sky unfortunately is a bit of a dumping ground.  The only way issues emerge is when we search and happen upon something that was put into Blue Sky. Arguably we shouldn't create a bucket for things we don't want to pay attention to.  But the issue list is also an idea collection area, and I like that.  I'd like if we had a process to recover things from Blue Sky.

### Assignments

Sometimes we assign all the tickets in the current iteration.  The primary purpose of assigning all the tickets is to identify the issues that no one is planning to address (and fix that).

I haven't had a lot of luck using assignments for more than this. Something I *wish* I could do with an assignment is hand a task off to someone -- like sometimes I can only finish half of an issue and I need someone else to finish the work (or vice versa).  But unless that person is carefully watching what is assigned to them this won't accomplish what I want.  So I have to change the assignment *and* leave a comment.  This leads to a lot of out-of-date chatter in the comments.

Generally I am unhappy with the notifications that GitHub provides. Are there third party products that can help here?  Also it's hard to know how someone else's notifications are configured, so I don't know what will trigger a response.  Most people will occasionally catch some updates, leading to a false sense of security.  (It would be great if I saw a list of everyone who was notified when I created or changed an issue.)

We have at times tried to use assignments to "claim" a ticket.  I.e., use it as a declaration of intent to avoid two people working on the same thing.  I did not find this productive, and it was hard to maintain.

In my [Hotdish](https://github.com/mozilla/hotdish) fantasy world I'd know who else in my team had looked at the ticket and when, and I could get a sense of what people were thinking about from that.

### Maintaining the tickets

It's important that tickets have proper titles.  Sometimes I have left bad titles in place and it would cause repeated confusion -- constantly asking myself and other people, what was this ticket about? GitHub has editable titles and you should use them.  Editing the main ticket description for clear mistakes (broken links, s/now/not/, etc) is also useful.

Still issues have a limited lifetime.  When the main description of the issue is no longer what you intend to implement it's time to open a new issue, and close the original with a reference to the new issue. Long comment threads are not useful.  Comments should indicate additions and clarifications, but when a comment changes the goal of the issue it's too easy to skim over.  Also when a debate happens in the comments and is resolved, it's hard to separate the resolution from the debate, and a new ticket fixes that.

Sometimes there's a collection of work that goes together.  We tried two approaches, but neither stuck:

**Create a label for the group of issues:** in this model I might create a `webrtc` label and label a bunch of issues.  This would help me figure out just how much work was left on that area and what bugs I should keep in mind as I look at a particular area of code, and maybe help find bugs or at least be sure I wasn't forgetting about something.

It's easy to think that you should start building a taxonomy of bugs. The default GitHub labels imply something like this (like "bug", "duplicate", "enhancement").  I would sometimes find myself using these just because they are there, but always ask: why did I bother? Then I started deleting these labels to remove the temptation.  I want only actionable labels.

An aside: the labels `duplicate`, `wontfix`, and `invalid` are (a) unnecessary, and (b) socially dangerous.  If something is a duplicate you can close it with the comment "Dup of #123".  Often that's not exactly what happened though, you might say "rendered moot by #123" or "once #123 is fixed this won't be an issue" or something specific. And `wontfix` is the worst, it's like a way of telling someone to fuck off, but that you don't even care enough to actually tell them why they should fuck off.  If it's a team member they won't take offense, but it's easy to fire it at some unwitting member of the public.  Take the time to close the bug with a comment about why you won't fix it. Invalid is like the vague passive aggressive combination of the other two.  Maybe it's because we like to imagine we'll do some kind of reporting on these statuses, but I find myself pretty bored by history.

**Create a master issue**: in this case you create an issue that links to all the sub-issues that need to be tackled.

To do this you can't just use backlinks (the link created whenever one issue references another): all backlinks look the same, and you can't tell if a bug that references the master is a dependency of the master, or depends on the master, or just mentions it in passing.

Instead we list all the bugs in the main description of the master issue, and edit as necessary.  You can use `[ ]` to make the bug list a [checkable list](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments). Unfortunately issue links don't get crossed out when they are closed (but they should, that would be a very helpful improvement).

The master ticket works okay but feels like it requires a lot of manual record keeping, and it's easy for your master issue to get out of sync with the sub-issues.  Also as you add or remove items from the list of dependent bugs you have to edit the main ticket description (anything in the comments would be too easy to lose) and there aren't notifications for those edits.

## The result?

I've only tried this approach with a small dedicated team.  It wouldn't match the less consistent rhythm of an open source project, and I have no idea how it would work with a larger team (maybe okay?)

One attribute is notably and deliberately missing: priorities, severities, and time estimates.  We played with these and I never knew what to *do* with them.  There's no single equation that determines what you should work on, and trying to create such an equation seems pointless -- you probably won't include everything you need to include, and if you do then it's unlikely that all parameters are filled in accurately and so you can't trust the results.

The goals for me, and the team, is to keep things somewhat organized, to remember important things, and to come to a shared understanding of what we're trying to accomplish and how.  Because of that last point some parts of the process deliberately force conversation where a tighter process wouldn't need it.  Specifically I don't want important things expressed through labels because there's no opportunity to discuss labels, they just appear and disappear.  Issue trackers that encourage complex taxonomies of bugs make me worry that the taxonomy will be used to assert things about process that need to be communicated directly and explicitly and via a two-way channel.

GitHub's permissive approach to editing (titles, descriptions, and comments) is reflective of the kind of process I also want to support: everyone should be able to do everything in the service of the project. It's better to give people more power: it's actually *helpful* if people can overreach because it is an opportunity to establish where the limits really are and what purpose those limits have.  Most tools have a strict append-only approach which I do not like (though it does make notifications easier, and notifications are my greatest frustration with GitHub Issues).

From your experience with GitHub issues do you have ideas to add to this?
