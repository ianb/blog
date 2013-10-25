Choosing a License
##################
:date: 2008-05-05 17:48
:author: Ian Bicking
:tags: Programming

I thought I'd take some time to talk about licensing.

Licensing is something that `F/OSS <http://en.wikipedia.org/wiki/FOSS>`_ programmers talk about a lot.  There's two major categories of licenses:

* The `GPL <http://en.wikipedia.org/wiki/GNU_General_Public_License>`_, aka Copyleft.  You must distribute source with your application, and users get full rights to the source code, including any additions you may make.

* Permissive licenses, X/MIT, BSD, etc.  These let you do pretty much everything.

There's also the `LGPL <http://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License>`_, which vaguely applies GPL-like terms to the original code, but is not "viral".  LGPL originally meant "Library GPL" but was renamed to "Lesser GPL" because people automatically used it for libraries without considering what the license actually enforced.

How much do these licenses matter?  How should a person choose between these options?

First, the LGPL.  It has specific phrasing that makes some sense for C code, to distinguish between extending the library itself and using the library.  It doesn't make much sense for other runtime environments.  Some people have tried to `clarify its meaning in other environments <http://opensource.franz.com/preamble.html>`_, but I'm not sure if a clarification like that means much.  The ambiguity seems like the worst of all worlds.  People who are afraid of the GPL won't use the software anyway.  People who act in bad faith can satisfy the terms of the license through trickery.  You don't get any practical protection over a permissive license, and you get most of the stigma of the GPL.  The GPL has some success stories, places where source was actually released due to the terms of the license.  I don't know of any similar success stories for the LGPL.  If you don't want to use the GPL, just use a permissive license.

Then the question: GPL or permissive licensing?

For some time I've chosen a permissive license for my code.  But I'm not really advocating that, and every so often I throw out a little GPL code.  Underneath this is something of a disinterest in licensing.  I don't think it means much.  If specifics of your license matters then something has gone wrong.  People are leeching code, and/or the community isn't providing enough benefit to encourage participation.  I don't believe that software has much intrinsic worth, and treating it like property doesn't make that much sense to me.  Licensing treats software as property, which is why I see the relevance of licensing as a kind of disfunction.  But there is the outside chance that it's really just a big project, or that the project is being participated in by rivals.  But nothing I work with is like this, and it's pretty uncommon generally, and anyway those projects all have their licensing pretty much figured out.

The GPL does seem to serve a constructive purpose when rivals have to cooperate in some fashion.  It makes a kind of demilitarized zone where everyone has to work for the collective good.  But even this is a sign that you can't trust the participants.  This is somewhat reasonable, because you can't actually trust large corporations with faceless programmers working on the code.  But even that's a kind of disfunction, because you can at least kind of trust large corporations with programmer employees who have a public face.  The individual programmers are going to be very uncomfortable participating in any kind of Machiavellian conspiracy.  Good open source projects are a coming together of individuals.  Institutions are not effective participants.  There are however scaling issues with individual participation: particularly that only a minority of developers are actually inclined to participate in this way.  An institution can pay someone to work on something they don't care very deeply about, and that person can still do useful work.  But they won't be part of the community.

Outside of this mediation of rivalries I'm not really sure what the GPL provides.  It protects users, because the terms of the GPL ensure that users get code.  It doesn't actually ensure that code is made public, though it does give developer employees leverage to make their work public.  There's some urban legends about the viral aspect of the GPL, but that's really just bullshit.  Code doesn't magically get relicensed just because there's a little GPL in the mix.  The GPL police won't show up at your door and confiscate your computers.  The only people who make those claims are GPL-haters like Microsoft.  Who should you trust: the FSF or Microsoft?  If you answered "Microsoft" then you need to get your head screwed on straight.

Unfortunately there is a stigma about the GPL, and there are competent developers that avoid all GPL software.  I find this frustrating, especially since I don't actually care about licensing, and so this adds a point of contention that I don't really care to pay attention to.  Some people in this situation then become GPL haters, because they feel like it's all GPL's fault.  But the GPL didn't create the licensing situation -- proprietary software started this.  Direct your hate where it belongs.  The GPL ain't it.

If my libraries were GPL I doubt I could leverage that to make other people open source their code.  But I know I would alienate some people, and as a result I choose a permissive license because it's just strategically advantageous.

Applications I think are different strategically.  You don't just swap an application in and out like you might a library.  If you choose to use an application, then often the licensing is a secondary choice.  The licensing ultimately only really applies to extensions.  Libraries also have a different pattern of acceptance.  Stubborn GPL haters can in effect veto a library in many projects (this is because stubborn GPL haters are viral).  But in an application their influence is much smaller.  Developers concerns like architecture and choice of libraries are not what drives an application.  An application is driven by its functionality.  If you have a useful application then licensing tends to be a secondary concern.  The licensing tends to define the community in some sense as well, and as a result there's a kind of opt-in consensus.  And I think the GPL in these cases really does create an environment of collaboration around extensions.  It has a real benefit.

This seems to be true empirically as well.  GPL'd libraries don't tend to get very popular.  People will do `crazy-big projects <http://harmony.apache.org />`_ just because of licensing issues.  GPL'd Applications seem to do quite well, with examples like WordPress, Plone, The Gimp, and even the Linux kernel, which is closer in structure to an application than a library.

I haven't studied the GPL v3 very closely, but it seems useful to me.  Software-as-a-service has the potential to make the GPL irrelevant (especially for the kind of code I write), and could put the GPL in the same category as the LGPL where it retains its stigma without offering any practical advantages.  Version 3 makes the permission/GPL choice seem useful, but so far I've never made any truly conscious choice between version 2 and 3.

If you are thinking about choosing a license, or thinking about choosing software based on the licensing, maybe these thoughts will be helpful in your own thinking.  And please don't GPL-hate in the comments, I'm not interested and if you feel the need then go write your own post.

**Update:** I wrote a second article to expand on some thoughts: `The GPL and Principles <http://blog.ianbicking.org/2008/05/06/the-gpl-and-principles />`_
