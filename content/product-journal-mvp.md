Title: A Product Journal: To MVP Or Not To MVP
Slug: product-journal-mvp
Category: mozilla
Tags: product-journal
Date: 2015-01-27

> I'm going to try to journal the process of a new product that I'm developing in [Mozilla Cloud Services](https://blog.mozilla.org/services/).  My previous post was [*The Tech Demo*](http://www.ianbicking.org/blog/2015/01/product-journal-tech-demo.html), and the first in the series is [*Conception*](http://www.ianbicking.org/blog/2015/01/product-journal-conception.html).

## The Minimal Viable Product

The Minimal Viable Product is a popular product development approach at Mozilla, and judging from Hacker News it is popular everywhere (but that is a wildly inaccurate way to judge common practice).

The idea is that you build the smallest thing that could be useful, and you ship it.  The idea isn't to make a great product, but to make *something* so you can learn in the field.  A couple definitions:

> The Minimum Viable Product (MVP) is a key lean startup concept popularized by Eric Ries. The basic idea is to **maximize validated learning for the least amount of effort**. After all, why waste effort building out a product without first testing if it’s worth it.

"""– from [How I built my Minimum Viable Product](http://practicetrumpstheory.com/how-i-built-my-minimum-viable-product/) (emphasis in original)"""

I like this phrase "validated learning."  Another definition:

> A core component of Lean Startup methodology is the build-measure-learn feedback loop. The first step is figuring out the problem that needs to be solved and then developing a minimum viable product (MVP) to begin the process of learning as quickly as possible. **Once the MVP is established, a startup can work on tuning the engine.** This will involve measurement and learning and must include actionable metrics that can demonstrate cause and effect question.

"""– [Lean Startup Methodology](http://theleanstartup.com/principles) (emphasis added)"""

I don't like this model at all: "once the MVP is established, a startup can work on **tuning the engine**."  You *tune* something that works the way you want it to, but isn't powerful or efficient or fast enough.  You've established almost nothing when you've created an MVP, no aspect of the product is validated, it would be premature to tune. But I see this antipattern happen frequently: get an MVP out quickly, often shutting down critically engaged deliberation in order to Just Get It Shipped, then use that product as the model for further incremental improvements.  Just Get It Shipped is okay, incrementally improving products is okay, but together they are boring and uncreative.

There's another broad discussion to be had another time about how to enable positive and constructive critical engagement around a project. It's not easy, but that's where learning happens, and the **purpose of the MVP is to learn, not to produce**.  In contrast I find myself impressed by the shear willfulness of the [Halflife development process](http://www.gamasutra.com/view/feature/131815/the_cabal_valves_design_process_.php) which apparently involved months of six hour design meetings, four days a week, producing large and detailed design documents.  Maybe I'm impressed because it sounds *so exhausting*, a feat of endurance.  And perhaps it implies that waterfall can work if you invest in it properly.

## Plan plan plan

I have a certain respect for this development pattern that Dijkstra describes:

> **Q:** In practice it often appears that pressures of production reward clever programming over good programming: how are we progressing in making the case that good programming is also cost effective?
>
> **A:** Well, it has been said over and over again that the tremendous cost of programming is caused by the fact that it is done by cheap labor, which makes it very expensive, and secondly that people rush into coding. One of the things people learn in colleges nowadays is to think first; that makes the development more cost effective. I know of at least one software house in France, and there may be more because this story is already a number of years old, where it is a firm rule of the house, that for whatever software they are committed to deliver, coding is not allowed to start before seventy percent of the scheduled time has elapsed. So if after nine months a project team reports to their boss that they want to start coding, he will ask: "Are you sure there is nothing else to do?" If they say yes, they will be told that the product will ship in three months. That company is highly successful.

"""– from [Interview Prof. Dr. Edsger W. Dijkstra, Austin, 04–03–1985](https://www.cs.utexas.edu/users/EWD/misc/vanVlissingenInterview.html)"""

Or, a warning [from a page full of these kind of quotes](http://www.linfo.org/q_programming.html): "Weeks of programming can save you hours of planning."  The planning process Dijkstra describes is intriguing, it says something like: if you spend two weeks making a plan for how you'll complete a project in two weeks then it is an appropriate investment to spend another week of planning to save half a week of programming.  Or, if you spend a month planning for a month of programming, then you haven't invested enough in planning to justify that programming work – to ensure the quality, to plan the order of approach, to understand the pieces that fit together, to ensure the foundation is correct, ensure the staffing is appropriate, and so on.

I believe "Waterfall Design" gets much of its negative connotation from a lack of good design.  A Waterfall process requires the design to be *very very good*.  With Waterfall the design is too important to leave it to the experts, to let the architect arrange technical components, the program manager to arrange schedules, the database architect to design the storage, and so on.  It's anti-collaborative, disengaged.  It relies on intuition and common sense, and those are not powerful enough.  I'll quote Dijkstra again:

> The usual way in which we plan today for tomorrow is in yesterday's vocabulary. We do so, because we try to get away with the concepts we are familiar with and that have acquired their meanings in our past experience. Of course, the words and the concepts don't quite fit because our future differs from our past, but then we stretch them a little bit. Linguists are quite familiar with the phenomenon that the meanings of words evolve over time, but also know that this is a slow and gradual process.
>
> It is the most common way of trying to cope with novelty: by means of metaphors and analogies we try to link the new to the old, the novel to the familiar. Under sufficiently slow and gradual change, it works reasonably well; in the case of a sharp discontinuity, however, the method breaks down: though we may glorify it with the name "common sense", our past experience is no longer relevant, the analogies become too shallow, and the metaphors become more misleading than illuminating. This is the situation that is characteristic for the "radical" novelty.
>
> Coping with radical novelty requires an orthogonal method. One must consider one's own past, the experiences collected, and the habits formed in it as an unfortunate accident of history, and one has to approach the radical novelty with a blank mind, consciously refusing to try to link it with what is already familiar, because the familiar is hopelessly inadequate. One has, with initially a kind of split personality, to come to grips with a radical novelty as a dissociated topic in its own right. Coming to grips with a radical novelty amounts to creating and learning a new foreign language that can not be translated into one's mother tongue. (Any one who has learned quantum mechanics knows what I am talking about.) Needless to say, adjusting to radical novelties is not a very popular activity, for it requires hard work. For the same reason, the radical novelties themselves are unwelcome.

"""– from [EWD 1036, On the cruelty of really teaching computing science](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html)"""

# Research

All this praise of planning implies you know what you are trying to make.  Unlikely!

Coding can be a form of planning.  You can't research how interactions feel without having an actual interaction to look at.  You can't figure out how feasible some techniques are without trying them. Planning without collaborative creativity is dull, planning without research is just documenting someone's intuition.

The danger is that when you are planning with code, it *feels* like execution.  You can [plan to throw one away](http://c2.com/cgi/wiki?PlanToThrowOneAway) to put yourself in the right state of mind, but I think it is better to simply be clear and transparent about *why* you are writing the code you are writing.  Transparent because the danger isn't just that *you* confuse your coding with execution, but that anyone else is likely to confuse the two as well.

So code up a storm to learn, code up something usable so people will use it and then you can learn from that too.

# My own conclusion...

I'm not making an MVP.  I'm not going to make a maximum viable product either – rather, the next step in the project is not to make a viable product.  The next stage is research and learning.  Code is going to be part of that.  Dogfooding will be part of it too, because I believe that's important for learning.  I fear thinking in terms of "MVP" would let us lose sight of the *why* behind this iteration – it is a dangerous abstraction during a period of product definition.

Also, if you've gotten this far, you'll see I'm not creating minimal viable blog posts.  Sorry about that.
