Toward a new self-definition for open source
############################################
:date: 2009-09-10 18:09
:author: Ian Bicking
:tags: Licensing, Politics, Programming

    This is roughly the speech I gave as a keynote address at `DjangoCon 2009 <http://www.djangocon.org />`_ in Portland.

I've been programming Python web software for quite a while now.  I considered coming here and talked about WSGI, standards, cross-framework integration, etc., but I decided I wanted to come up here and talk to you as compatriots, as fellow open source programmers.

Over the past year or so I have been thinking a lot about politics.  Not electoral politics per se, or the geopolitical situation, but the question of the meaning of what we are doing.  Maybe it is some sort of programmer midlife crisis: why am I doing what I'm doing, and why does it matter?  And also I have been thinking a lot about open source -- what this thing that we're doing means in the larger context.  Are we just engineers?  Is there some sort of movement?  If so, what is that movement?  Especially as open source has become more popular, the sense of a movement seems to dwindle.  It felt like a movement 10 years ago, but not as much today.  Why should this happen?  Why now, in the midst of success does open source seem less politically relevant than it did 10 years ago?

I'm also speaking somewhat to Django specifically, as I think it is one of the communities with a bit more resistance to the idea of the politics of code.  The Django philosophy is more: the value of this code is the value of what you do with it.  I'm not here to criticize this perspective, but to think about how we can find meaning without relying on the traditional free software ideas.  To see if there's something here that isn't described yet.

I'd like to start with a quick history of free and open source software.  My own start was in highschool where I was taking a class in which we all used Emacs.  This was my first introduction to any real sort of programming environment, to Unix, to a text editor that was anything to talk about.  At the time Emacs would say at startup "to learn more about the GNU project hit Control-H Control-P" -- because of course you need a keyboard shortcut to get to a philosophy statement about an editor.  So one day I hit Control-H Control-P.  I was expecting to see some sort of About Message, or if you remember the software of the times maybe something about Shareware, or even "if you really like this software, consider giving to the Red Cross."  But instead I came upon the GNU Manifesto.

GNU Manifesto
-------------

I'd like to read a couple quotes from the `GNU Manifesto <http://www.gnu.org/gnu/manifesto.html>`_.  There are more `modern descriptions of GNU <http://www.gnu.org/gnu/thegnuproject.html>`_, but this is one of the first documents describing the project and its mission, written by Richard Stallman.  Let me quote the section "Why I Must Write GNU":

    "I consider that the golden rule requires that if I like a program I must share it with other people who like it. Software sellers want to divide the users and conquer them, making each user agree not to share with others. I refuse to break solidarity with other users in this way. [it continues...]

    "So that I can continue to use computers without dishonor, I have decided to put together a sufficient body of free software so that I will be able to get along without any software that is not free."

    [later it goes on...]

    "The fundamental act of friendship among programmers is the sharing of programs; marketing arrangements now typically used essentially forbid programmers to treat others as friends. The purchaser of software must choose between friendship and obeying the law. Naturally, many decide that friendship is more important. But those who believe in law often do not feel at ease with either choice. They become cynical and think that programming is just a way of making money."

When I read this statement I was immediate head-over-heels in love with this concept.  As a teenager, thinking about programming, thinking about the world, having a statement that was so intellectually aggressive was exciting.  It didn't ask: "how wrong is piracy really", or "why are our kids doing this", but it asked "is piracy a moral imperative" -- that's the kind of aggressive question that feels revolutionary and passionate.

Let me go over one of the lines that I think exemplifies this:

    "I consider that the golden rule requires that if I like a program I must share it with other people who like it."

It wasn't saying: what are we not allowed to do, nor did it talk about some kind of societal injustice.  It didn't talk about the meaning of actions or their long-term effects.  Instead it asked: what must we do, not as a society, not in service of some end, but what are we called upon to do as an *individual*, *right now*, in service of the people we call friends.  It didn't allude to any sociological explanation, natural selection, economics; there is just the golden rule, the most basic tenant of moral thought.

Free Software vs. Open Source
-----------------------------

When I first encountered free software, I suppose about 15 years ago, this was during one of the more difficult periods of its evolution.  It was past the initial excitement, the initial optimism that the project would take only a couple years to reach parity with closed-source Unix, it was before it was clear how the project would move forward.  Linux was young and seemed to be largely off the radar of Richard Stallman and other GNU advocates, and they were struggling to fill in final key pieces, things like a kernel, widgets, and they hadn't even thought about entirely new things like browsers.

The message that came through from that period is not the message I wish came through.  The message I wish came through was that message from the GNU Manifesto, that spirit of a new sense of duty and ability.  When people talk about Richard Stallman and the Free Software Foundation and the GNU Project, they'll often point to the GNU General Public License as the most important contribution -- the GPL.  I'm sure you all know something about it.  Of course the core concept there is the idea of copyleft.  Not only will the software be open, but it's takes the implied perspective that the principles of freedom are rights -- that unfortunately the world is not wise enough to see that use, distribution, and modification are rights; but the GPL still asserts that these *are* your rights.  When you become one of us, when you participate in the freedoms this license grants you, when you use the GPL, there is encoded in the license a support for this sense of the natural right of free software.  We, GNU, can't encode that for the world, but for the software that we write these rights are inalienable.

But as I said those were difficult times.  There was a great deal of pressure.  People were trying to understand what open source meant. People still struggle with questions: how would an economy function, how would a programmer get a job, if this is as successful as people hoped will we all just be out of jobs?  Other questions were: who will write the software that no one wants to write?  How can I, embedded in a situation where I can't actually use only free software -- remember at this time there was no way to use completely free software -- how can I assert a duty to do something that is not possible?  How can I be useful unless I interface with all these proprietary things?  If I deal with companies which aren't comfortable with open source software, then what?  After all, open source seemed only barely plausible at this time.  It was not an easy argument to make.

And all this was before the term "open source" really took hold as a distinct idea.  That itself is an interesting story.  There was a time during this marketing period when there arose a kind of terminology divide -- free software vs. open source software.  The terminology divide was that the "free" in free software implied you couldn't charge anything, that made people think about price, might even imply cheapness.  Open source directly refers to programming, uses the feel-good term "open", and doesn't sound too revolutionary.  But besides that there was also a substantial philosophical difference about the value of the software itself.

So there was a difference in how things were going to be pitched, but also a difference in what people thought the general value of this project was.  From GNU and Richard Stallman there was the notion that this was right because it was right; it was a moral imperative.  The virtue of what we build is in its freedom; if it is also technically superior then that's great, but it is not how we should judge our success.  We were giving people self-determination: programmer self-determination, user self-determination... on the open source side the argument was that this is a good way to create software.  Programmers working together can do better work.  With many eyes all bugs are shallow.  All working together, we'll work faster, you get the benefit of free contributions from all sorts of people.  People were clamouring to get all these proprietary companies with failing software products to open source their software; miracles will occur!  What you thought was useless will regain value!  You'll reattain relevance!

The open source and free software philosophical divide: on one side practical concerns, on the other moral.  And this is what I want to talk about later: can we find a moral argument for these practical concerns?  

The basic free/open disagreement continues in debates over licenses: the GPL vs. the BSD and other permissive licenses.  If you read the `GPL <http://www.gnu.org/copyleft/gpl.html>`_ it talks a great deal about philosophy; if you read the `BSD license <http://www.opensource.org/licenses/bsd-license.html>`_ it's really just some disclaimers and basic instructions, and the one line: "Redistribution and use in source and binary forms, with or without modification, are permitted."  It doesn't say why you've received this software, or any philosophy about rights and freedoms, or even encourage you to use the same license on your own software.  An engineer's license.

So these two licenses in many ways became a focus and definition of free and open source software.  If you look at the `Open Source Initiative <http://www.opensource.org />`_, which has served to define what "open source" means, it is basically just a `list of approved licenses <http://www.opensource.org/licenses/alphabetical>`_.  If you use one of those licenses, the software is open source, if not then it is closed.

I think this is disappointing, because licenses are just law, and law is not very interesting.  A law tells you what you shouldn't do, it doesn't tell you what you should do.  When both sides are talking about freedom, the licenses just define freedom as the lack of certain restrictions.  Take away those restrictions and voila, you are free... as though we are all just bundles of freedom waiting to be released.

Self-Definitions
----------------

With licenses we have a negative definition of our community.  Either license you choose, the license feels like a reaction against closed source software.  If you can imagine a world in which there was no copyright, where our platforms were all setup to distribute source code in modifiable forms, where everything was open and everything was free, then none of these licenses would matter.  No one would be compelled to create the GPL in such a world; we wouldn't advocate for copyright just so we can secure people's freedoms.  In that kind of world all this licensing disappears.  And this isn't even so weird a world.  You can pretend there's no copyright now.  Maybe you have to reverse-engineer some stuff.  There's lots of places in the world where no one really gives a damn about copyright.  But those places don't feel open source to me, they don't feel that more free.  We aren't made unfree just by legal restrictions; freedom is something we have to actively grasp.

I don't think what we do is predicated on copyright.  Indeed, many projects are comfortable with an entirely confused copyright ownership.  This causes very few problems.  A focus on licensing makes us into a reaction against proprietary software, where we allow proprietary software and its makers to define what it means to be *us*.

This concerns me because it isn't just about formal definitions and terminology.  When I say *what do I do*, I say I am an open source programmer.  That's not just an attribute, like saying that my hair is brown.  Open source is a way in which I see myself, a way I think about my craft, my profession, and a way I justify the work I put out to the world: that it aligns with these values.  So it's very important to me what these values are.  And it's frustrating to see open source defined in reaction to closed source software, because personally I don't care about closed source software that much.  

I never really cared much about fighting Microsoft, and I certainly don't care now.  I see myself as a builder; this is what always drew me towards programming.  The desire to build new things.  This is our privilege as programmers, that we always have the opportunity to build new things.  If we're asked to do something again and again and again, you always have the power to do it in a more abstract way, to generalize it away, until you can start to ignore the requests and move on to another problem.  This is something unique thing to computer programming.  These are the kind of unique attributes that make us different as a profession and as a craft than just about anything I can think of.

So I'm frustrated.  Here we are stuck in this notion of a license as a self-definition.  I want to find a new self-definition, a new idea of what makes us us.

What Makes Us Us
----------------

So... what makes us us?

I was saying about Django, the community is not particularly enthusiastic about philosophy.  Or maybe I should say, Django's philosophy is: the value of the code is the thing you do with it.  These abstract discussions about architecture, reuse, big plans... instead, Django as a community encourages you to keep your head in the code, think about what you want to do, and then do it.  Don't shave yaks.

But I'm not here to tell you to get philosophical about freedom, or to berate you for a functional definition of value.  I'd like to look at this community for what it is, and ask: what is the value system here?  Maybe it isn't described, but I also don't think it is therefore absent.

So... when I say I identify as an open source programmer, what is it that I am identifying as?  

I don't believe licensing makes something truly open source.  There was this clamour in the past to get companies to open source their products.  This has stopped, because all the software that got open source sucked.  It's just not very interesting to have a closed source program get open sourced.  It doesn't help anyone, because the way closed source software is created in a very different way than open source software.  The result is a software base that just does not engage people in a way to make it a valid piece of software for further development.  At least not unless you have something peculiar going on... an economic force like you had behind Mozilla that could push things forward even in the midst of all the problems that project had.  One might even ask, is Mozilla still suffering from that proprietary background, when something like KHTML or WebKit which came from a truly open source background, and has been a more successful basis for collaboration and new work.

So whatever it is that makes something open source, it's not just licensing.  Given a codebase, we can't necessarily expect that someone going to care about it and love it and make it successful.  A lot of people have described what makes a successful open source codebase; I'd like to talk some about what the communities look like.

------------------------------------------------------------

Open source works as a fairly loose federation of people together.  Everyone involved is involved as an individual.  Companies seldom participate directly in open source.  Companies might use open source, they might sponsor people to work on open source projects, they might ask an employee to act as a liason.  But it's not cool to submit a bug as a company.  You submit it as yourself.  If someone asks a question, you answer as yourself.  You don't join a mailing list under the company's name.  And even when you put a company name on a product, it's hard to relate to the product as a *project* without some sense of authorship, of the underlying individual.

------------------------------------------------------------

There's also very little money being moved about.  There's not a lot of commercial contracts.  You might get software, you might get bug fixes, you might get reputation, but there's seldom any formal way setup to introduce commerce into the community.  How many projects let you pay to escalate a bug?  Even if everyone involved might like that, it's just not there.

------------------------------------------------------------

But I want to get back to individuals.  How things are created is not that someone determines a set of priorities, lays them out, then people work on implementation based on those priorities.  That of course is how things typically work at a company, as an employee.  But open source software and open source projects are created because an individual looks at the world and sees an opportunity to create something they think should exist.  Maybe it resolves a tension they've felt in their work, maybe it allows that person to respond to the priorities from above better, but the decision to implement lies primarily with the implementor.  When someone makes a decision to move a product from simply private code -- regardless of the license -- to being a real open source project, that decision is almost always driven by the programmer.

------------------------------------------------------------

Underneath most open source work there is a passion for the craft itself.  This is what leads to a certain kind of quality that is not the norm in closed source software.  It's not necessarily less bugs or more features, but a pride in the expression itself.  A sense of aesthetic that applies to even the individual lines of software, not just to the functionality produced.  This kind of aesthetic defies scheduling and relies on personal motivation.

As open source programmers we are not first concerned with how a task fits into institutions, how a task can be directed by a hierarchy or an authority, or even how the task can be directed by economics.  The tasks that we take on are motivated by aesthetic, by personal excitement and drive.

------------------------------------------------------------

We are also in a profession where there is little stasis.  If you can create something once, you can create it a thousand times, through iteration or abstraction.  You can constantly make your own effort obsolete.  A good programmer is always trying to work themselves out of a job.

Djangocon didn't exist a couple years ago.  Django didn't exist only a few years ago.  And I don't think there's anyone here who thinks that, having found Django, they've reached some terminal point.  It's hardly even a point to pause.  There's a constant churn, a constant push forward that we're all participating in.

As a result it's demanded of us that we have a tight feedback cycle, that education is not a formal affair but a constant process in our own work.  There's a constant churn, and a professional sense we're kind of like fruit flies.  A generation of knowledge and practice is short enough that the evolution is rapid and visible.  You don't have to be particularly old or even thoughtful to see the changes.  You can look back even on your own work and on communities to see changes over the course of a couple years, to see changes and shifts and a maturing of the work and the community.

------------------------------------------------------------

Another attribute of open source: our communities are ad hoc and temporary.  We do not overvalue these communities and institutions; we regularly migrate, split, recombine, and we constantly rewrite.  There is both an arrogance and a humility to this.  We are arrogant to think This Time Will Be Different.  But we are humble enough to know that last time wasn't different either.  There will always be a next thing, another technique, another vision.

Because of the ad hoc nature of the communities, we don't have long collective plans.  The ad hoc community may be the intersection of different *personal* long range plans, a time when different visions somehow coincide in a similar implementation.  Or perhaps it's just serendipity, or leadership.  But we make each decision anew.  I believe this protects us from being misled by sunk costs.  The idea of a sunk cost is that when you make an investment, you've put in effort, that effort is gone.  Just because you've put in effort doesn't mean you've received value, or that the path of investment remains valid.  But as humans we are highly reluctant to let go of a plan that we've invested in.  We have a hard time recognizing sunk costs.

I believe in our developer community we approach our work with sufficient humility that we can see our work as simply a sunk cost.  Our effort does not entitle us to any particular success, so we can choose new directions with more rationality than an institution.  Though it can also be argued that we are too quick to dismiss past investments; there is a youthfulness even to our oldest members.

------------------------------------------------------------

We do not have hierachies with decision makers above implementors.  Some people have veto power (a BDFL), but no one has *executive* power.  A decision only is valid paired with an implementation.  You cannot decide something based on information you *wish* was true; you cannot decide on something then blame the implementors for getting it wrong.  We are in this sense vertically integrated, decision and implementation are combined.  The result may be success or failure, commitment or abandonment, but the hierarchy is flat and the feedback loop is very tight.  And if an individual feels stymied, there is always another community to join or create.

Though this is only a start, it's these attributes that I would prefer define us, not licenses.

I also would like that this could be a model for how other work should be done.

Why Us?
-------

Why would we, as programmers, be unique or worthy of emulation?  I mentioned before that we constantly work ourselves out of our job.  We also create the tools we use to do the work.  We define the structure of our communities.  We're consistently finding novel ways to use the internet build those communities.  It's not that we as a group are somehow uniquely wise, or some Greatest Generation, but we have become distinctly self-empowered.  There is a uniqueness to us.  It might be a coincidence of history, but it is there.

A question I might then ask: is there a political meaning to this?  This is the form our craft takes, but does that mean anything?  We work with computers, someone else might work with their hands, an artist considers color, a salesperson learns how to put on a good smile.

I haven't quite figured this out yet, but I think there's something in this.  Over the years I've found myself looking at politics in a increasingly technocratic lens; more so than as a liberal, conservative, or radical.  That is, instead of looking at the world and seeing what's wrong about it, and explaining it in terms of a class struggle, a cultural conflict, in terms of advocacy or invented enemies or allies, I see a system that just works how it works.  It's more like gears than like a war.  The gears turn and sometimes we don't like what results, but it's not malice.

But I also don't think we are slaves to the technical functioning of the system.  None of us are inevitably caught up in some statistical outcome of markets, or condemned by money in politics or advertising.  At any time we can say Here Is What I Believe, and it is as powerful as any of those other things; we're too quick to look at the people who aren't asserting a belief, who aren't asserting their own potential for self-empowerment and direction, and we ignore everyone who is aware and concerned and attempting self-determination.  We are at danger of ignoring the great potential around us.

It is in this sense that I wonder not just how we can spread the idea of freedom through licensing, which has inspired the free culture movement, but also how we can spread this idea and practice of individual action, of combining decision and implementation, and of constant ad hoc collaboration.

I'm not just thinking of politics directly, but of professional lives as well.  Right now we're talking about healthcare.  It's a very political issue, and yet healthcare is ultimately a profession, a job, an action.  How we work on that, collaboratively or not, is as political as any aspect of the system.

One anecdote that made me think about this, is a task I had that involved putting authentication in front of a mailing list.  The mailing list happened to be for wound, ostomy, and continence nurses, and in the process of the job I read a bunch of their emails from the archives.  As wound nurses they spent a lot of time asking about specific questions -- maybe a wound that wouldn't heal, they kept draining the puss and it discharge kept reappearing, and did anyone have ideas of the next technique to try?  

Reading a few of these I could tell this was a profession where you needed a strong stomach.  But the whole interaction, the way they described problems, the way people came back with answers, it felt very familiar to me.  It was the same kind of discussions I could imagine having about Linux administration or debugging.  And the goals were similar.  No one was making money, there wasn't really reputation on the line, it was just people who wanted to help their patients and who wanted to help each other.  

So that mailing list was great, but it's unfortunately not that common.  And if nurses were open to that kind of collaboration, doctors don't seem nearly as ready.  And there's a lot of professions where there's not even that thoughtfulness.  I believe in any profession there's the ability to do it well or not; there's nothing so rote or well understood that there's no room for improvement.  It doesn't have to be fancy technology, it can just be a technique, a way of managing work; all things worth doing have some way of improving, by bringing in this same sense of collaboration and individual action and thoughtfulness, all things can be implemented better than they are now.  What I'm describing isn't a fancy new website for professionals, but about people look at their own work differently; the technology is not the hard part.

The Political
-------------

Changing how people look at their work I think is political.  It involves individual empowerment.  It can mean economic change.  I also think it deemphasizes competition.  When I think about Pylons, or Django, or TurboGears, or WSGI, there's competition, but it's also collegial.  There's not really that much of a sense of survival.  We aren't carving out territories, we're just finding paths to some unknown end.  If something else wins out, well, we're all just along for the ride.  In the end it is inevitable that something else other than what *any* of us are working on will win out over what any of us are doing.  Just like everyone eventually loses their job at least to death or retirement.  There's no permanency.  But if we can be individually more productive, it doesn't have to mean we've put someone else out.  It *could* mean we all, all of society, all of humanity, just do *more*.  Why do we have to set ourselves against the Chinese, or Europe against the U.S.?  Why do we have to set ourselves one economy against another?  

Or consider government itself: we're obsessed with our elected officials, but of course government is far larger than just the elected officials.  The U.S. Federal Government alone has 1.8 million employees.  We constantly threaten to institute accountability, meaning that we'll poke and prod government workers from the outside and expect better outcomes.  That we expect anything to come of this is absurd, but somehow accountability has become an easy alternative to constructive suggestions for improvement.  

But why shouldn't we expect that government workers *want* to do better?  I believe in fact those people doing the work are especially well equiped to figure out *how* to do better.  But it's not automatic.  They aren't empowered in a system that is so exceptionally hierarchical.  Lately we've seen lots of efforts to ask the public how to do government work better, but we've seen nothing asking *government* how to do government work better.

These are the kinds of things I'd like to see us all think about more: open source has done incredible things, has inspired new ideas, about more than just software and engineering, but I think we have yet more things to give.

Thank you for your time.

