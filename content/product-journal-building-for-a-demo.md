Title: A Product Journal: Building for a Demo
Slug: product-journal-building-a-demo
Category: mozilla
Tags: product-journal
Date: 2015-02-18

I've been trying to work through a post on technology choices, as I had it in my mind that we should rewrite substantial portions of the product.  We've just upped the team size to two, adding [Donovan Preston](http://donovanpreston.blogspot.com/), and it's an opportunity to share in some of these decisions. And get rid of code that was desperately expedient.  The server is only [400ish lines](https://github.com/mozilla-services/pageshot/blob/f3df30ccaf64b75426e87325addc6fac373ba220/appengine/pageshotpages/main.py), with some significant copy-and-paste, so we're not losing any big investment.

Now I wonder if part of the [danger of a rewrite](http://www.joelonsoftware.com/articles/fog0000000069.html) isn't the effort, but that it's an excuse to go heads-down and starve your situational awareness.

In other news there has been a [major resignation](http://blog.johnath.com/2015/02/17/home-for-a-rest/) at Mozilla.  I'd read into it largely what Johnathan implies in his post: things seem to be on a good track, so he's comfortable leaving. But the VP of Firefox can't leave without some significant organizational impact.  Now is an important time for me to be situationally aware, and for the product itself to show situational awareness.  The technical underpinnings aren't that relevant at this moment.

So instead, if only for a few days, I want to move back into expedient demoable product mode.  Now is the time to explain the product to other people in Mozilla.

The choices this implies feel weird at times.  What is most important? Security bugs?  Hardly!  It needs to demonstrate some things to different stakeholders:

1. There are some technical parts that require demonstration.  Can we freeze the DOM and produce something usable?  Only an existence proof is really convincing.  Can we do a login system?  Of course!  So I build out the DOM freezing and fix bugs in it, but I'm preparing to build a login system where you type in your email address.  I'm sure you wouldn't lie so we'll just believe you are who you say you are.

2. But I want to get to the interesting questions.  Do we require a login for this system?  If not, what can an anonymous user do?  I don't have an answer, but I want to engage people in the question.  I think one of the best outcomes of a demo is having people think about these questions, offer up solutions and criticisms.  If the demo makes everyone really impressed with how smart I am that is very self-gratifying, but it does not engage people with the product, and I want to build engagement.  To ask a good question I do need to build enough of the context to clarify the question.  I at least need fake logins.

3. I've been getting design/user experience help from [Bram Pitoyo](http://www.brampitoyo.com/) too, and now we have a number of interesting mockups.  More than we can implemented in short order.  I'm trying to figure out how to integrate these mockups into the demo itself -- as simple as "also look at this idea we have".  We should maintain a similar style (colors, basic layout), so that someone can look at a mockup and use all the context that I've introduced from the live demo.

4. So far I've put no effort into onboarding.  A person who picks up the tool may have no idea how it is supposed to be used.  Or maybe they would figure it out: I haven't even thought it through.  Since *I* know how it works, and I'm doing the demo, that's okay.  My in-person narration is the onboarding experience.  But even if I'm trying to explain the product internally, I should recognize I'm cutting myself off from an organic growth of interest.

5. There are other stakeholders I keep forgetting about.  I need to speak to the [Mozilla Mission](https://www.mozilla.org/en-US/about/manifesto/). I think I have a good story to tell there, but it's not the conventional wisdom of what it means to embody the mission.  I see this as a tool of direct outward-facing individual empowerment, not the mediated power of federation, not the opting-out power of privacy, not the committee-mediated and developer driven power of standards.

6. Another stakeholder: people who care about the Firefox brand and marketing our products.  Right now the tool lacks any branding, and it would be inappropriate to deploy this as a branded product right now. But I can *demo* a branded product.  There may also be room to experiment with a [call to action](https://en.wikipedia.org/wiki/Call_to_action_(marketing)), and to start a discussion about what that would mean.  I shouldn't be afraid to do it really badly, because that starts the conversation, and I'd rather attract the people who think deeply about these things than try to solve them myself.

So I'm off now on another iteration of really scrappy coding, along with some strategic fakery.
