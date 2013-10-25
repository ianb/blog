Title: Why Isn't Programming Futuristic
Date: 2013-10-23
Slug: why-isnt-programming-futuristic

If you think someone is asking a rhetorical question, it is usually most interesting to treat it as though it is a legitimate question. Especially if we're talking about something *hard* -- driving down to underlying assumptions through this questioning process is interesting.

Applying this to Bret Victor's talk ["The Future Of Programming"](http://worrydream.com/dbx/) is useful. Why are we living with the programming technology of the 70s, when in the 70s there was so much excitement and expectation that we would create something better?  Bret's talk has an implied challenge: what happened to the future?

I have an affection for the thinking of the 60s and 70s that I also see in Bret's talk.  There was a distinct tone in that decade across thinking in computer science, politics, culture... and even though I usually disagree with the specific ideas, I love the way in which those ideas were discussed and presented.  Optimistic, adventurous, often intimate.  To the degree Bret's talk was a call for that flavor of thought, I heartily agree.  But I wonder that the optimism of this age was in part built on its ambition -- when you imagine things you know you cannot make (at least not *yet*) you avoid confronting the tedium and problems of an actual implementation.  Looking back on the futurism of that time it seems defined more by its overambition than its success.

But it would be unfair to engage so shallowly with just a comparison of the tones of yesteryear and today.  Bret identifies four things that it is implied we should at least *remember*, and perhaps that we should *pursue*.

## procedures -> goals and constraints

When you first read about Prolog, did it excite you?  It certainly excited me.  A whole programming language built on *magic*.

But what then?  It's magical, but you can't make anything from it! Problems are never provided to us in clean forms.  Phrasing problems in solvable terms is more effort than solving them, so instead we use shortcuts that achieve our functional and concrete goals without any high minded "solutions".

I do think it could be argued we need more forms of expression in programming languages.  Regular expressions are pretty great, for all we complain about them.  Why don't languages typically include other kinds of powerful search methods?

When I say "programming language" I'm not referring to special built-in syntax.  Python's regular expressions are better than Javascript's despite the fact Python has no special syntax and Javascript does.  But neither is able to search anything but strings.

We can implement new search techniques through libraries (and such libraries exist), but we can do more.  A programming language is *syntax*, but it is also an *object model*.  If a programming language includes general ways to traverse and interpret object models then we could see much more powerful general goal-oriented libraries.  LINQ is perhaps the best modern example of this.

To get there I think we need a couple things:

#### Safe object traversal

You need to be able to inspect and traverse objects, all objects.  In python for instance you can do `dir(obj)` or `getattr(obj, attr)`, but those are incomplete and unsafe.  Pointing code at an arbitrary object graph and inviting it to inspect things based on this is somewhat dangerous.  Using `obj.__dict__` is actually safer, but incomplete in its own ways.

JSON is compelling in this case because it is highly constrained.  It can't contain methods, all its attributes are concrete and enumerable. It makes something like [JSONSelect](http://jsonselect.org/) reasonable.  But who wants to constrain themselves to large concrete JSON objects?  You don't have derivative properties of objects, polymorphic tests, lazy loading of data, etc.

To traverse objects *safely* and *completely* you need to be able enumerate aspects of the object.  Enumerate its properties, while also being certain there are no side effects to getting data, and identifying methods that can be safely called.

#### Ubiquitous object extensions to support querying

You can accomplish some stuff with traversal, giving you a baseline so that domain-specific portions of the code can be traversed, but there are always cases when you need to customize that traversal.  For instance, any object that supports a "method missing" style override (e.g., `__getattr__` in Python) needs a way to enumerate the actual properties.  And if they are innumerable then *still* you must enumerate something.

There also must be a culture where proper extensions are regularly provided on objects.  Powerful tools are built on powerful paradigms, and *enabling* a paradigm isn't the same thing as actually implementing it across a fully developed programming environment.

#### Code transport

Most things aren't genuinely innumerable.  It's more likely you can't enumerate an object because the source of truth is outside the program.  If you want to access a database of users in your system, you can't load it all into memory and query it from there.

In the past, to the degree I've done anything like this, the transportation of code is extremely ad hoc.  It involves doing things like translating Python to SQL.  To what degree I understand LINQ, I think it also does this, though maybe with the ability to separate in-process from out-of-process portions of a single query.

These limitations came to mind when I was reading a recent [announcement about ZeroVM](http://www.rackspace.com/blog/zerovm-smaller-lighter-faster/) where they talk about "moving the app to the data" instead of the traditional task of moving the data to the app.  And the degree we are dealing with "objects" -- data and methods combined -- we really *can't* move the data to the app, because it's all apps.  The solution alluded to with ZeroVM is that running code can be transported to other environments, that this is reliable and deterministic, that code runs with limited defined interfaces to its environment, and that this is all done efficiently.  Maybe there is a solution there?

#### Combining it all

I struggle somewhat to imagine what all these things could be used for together.  Would my code become much more declarative?  I find declarative frameworks initially exciting but usually ultimately annoying.  Maybe with all the pieces in place it would stop being annoying?  I am skeptical.  I suspect the very idea of a "program" would change in the face of this.  And I'm not sure we want it to change.

## text dump -> spatial representations

Why, after all this time, are we still stuck with ASCII programs?

For one answer: recall Microsoft Word.  Have you ever found yourself "debugging" a Word document?  "Why won't this paragraph align with all the other paragraphs?!?"  There is hidden structure to a Word document.  When composing with Word you do not have access to that hidden structure.  You are only aware of parts of it, and some aspects may only reveal themselves in certain circumstances.  This sort of thing would not do for a program -- it is enough that we must debug what the program *does*, a richer representation of the program means we would have to debug *the expression of the program itself*.

You might counter: we must simply make an unambiguous and transparent spacial representation of a program.  And yes, without that constraint we are doomed.  But then what might we create?  On the large scale we might organize large modules of code using something besides files. And we do see some work like this, IDEs present code in ways that aren't tied to text dumps.  But it's not very interesting, because very little time is spent manipulating large modules of code.  When we rename and move files around it's a relatively small task, and one that requires little debugging -- the paths either work or they don't. There's room for improvement, but nothing revolutionary.

What would be interesting is new representations of code at the more detailed level.  For that level we want clear, compact, composable representations.  But you know what?  We have spent millenia developing a clear, compact, composable representation of human thought.  And it fits in ASCII, and flows from left to write and down the page line by line.

As an aside: why at least do we not allow meaningless stylistic annotations of source code?  Why can't I make code italic or bold? Here we might blame a lowest-common-denominator of tools (which is a topic of its own), but also programmers avoid meaningless annotations. Because there's no actual semantic meaning to bold text, or colored text, it would *imply* some intent without actually enforcing that intent.  We do allow implied intents -- non-significant indentation and whitespace, unneeded parenthesis, and most of all comments -- but it can lead to great hand-wringing, they are each an opportunity to mislead readers.

Still, this is too pessimistic.  What could we do?  I don't think we need to make a strong shift away from ASCII files on disk.  Ultimately anything we do needs to be serialized, and that serialization needs to be debuggable, and ASCII files work fine on both counts.  For serialization we could use XML or something with clear exposed structure, but we don't need to: every programming language can be unambiguously parsed into something, usually an [AST](http://en.wikipedia.org/wiki/Abstract_syntax_tree), which is typically exactly what we'd expect from an XML serialization.

But the interaction between tools and source is crude.  The best we've managed at any scale is color highlighting.

#### Provenance

This is perhaps a personal pet concern of mine, maybe a stretch to connect to this topic, but I see it everywhere.  We need general ways to track artifacts back to their source.

An recent improvement in provenance is the [source map](http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/), where you can compile something to Javascript and the browser debugging tools can trace errors back to their original (pre-compilation) source.  But that's just one example -- for example it doesn't apply to HTML -- and it's only supported by a couple clients.

With more extensive support for provenance you'd have more potential for alternative tools to manipulate source.  With support for provenance of data you could go further yet.

I think the typical vision of a "spatial representation" of source code is very modernist.  It imagines a new, complete, better way of manipulating source.  Then we get annoyed no one has come up with the new, complete, better way... but it doesn't exist, not as a single thing.

#### Better, more accessible ASTs

We're just now starting to see complete ASTs being generated for languages.  Too often comments or other semantically insignificant items were left out, and even producing an AST is something many languages didn't do for much of their history.

So real progress is being made.  We need to be fully ready for the AST to be the true representation of the program.  That is, parsing, changing the AST, and serializing that AST should always be an acceptable step in development.  Sometimes this means better ASTs (like ones that include comments), sometimes this means developers have to suppress their individual preferences.  The good reception I've seen from developers of [gofmt](http://golang.org/cmd/gofmt/) (which normalizes Go syntax, is opinionated, and is widely used) makes me think this is more acceptable than people think.

Of course each langauge usually keeps the AST in memory, and tooling has to be very language-specific.  Maybe hoping for language agnosticism is too much.  But some standard protocol would certainly be nice -- probably tools communicating via sockets with some language-specific parser.  But then to what end?  Each language's AST is distinctive, and should be because that's why we have different languages.  But a generic tool needs a generic AST.

## coding -> direct manipulation of data

On its face this is kind of an odd complaint.  We have lots of direct manipulation of data.  Photoshop is a pretty incredible tool. And there are lots similar tools that allow for the direct manipulation of data.

We need to "code" when we need to handle data in an abstracted way. You can draw *one* picture with direct manipulation, but defining something that can be rendered into a picture in a variety of contexts is more difficult.  (Though even that has been achieved through various modeling tools.)

How can you represent a loop or a variable in non-textual tools?  How do you draw a picture where one line is of length `x`, while another line is of length `x*2`, and another line is of length `5`?  What are the determining constraints that resolve the picture into something concrete for a given value of `x`?

This question is what Bret seems to be struggling with through [Stop Drawing Dead Fish](http://worrydream.com/#!/StopDrawingDeadFish) or [Learnable Programming](http://worrydream.com/LearnableProgramming/). We haven't figured it out, and they didn't have any more of a clue about it in the 70s either.  I wish Bret luck!

It does bring graphical programming languages to mind.  Oddly these languages seem as focused on symbolic manipulation as textual programming languages are.  It seems to me that a graphical programming languages need to more fully embrace the graphics, and embrace a *result* that current programming languages are not well suited to provide.  It shouldn't just be "easier programming".

## sequential -> parallel

Parallel code can be really hard to write, debug, and understand. Sequential code is pretty nice.

If this is an admonition that we should all just do more work to achieve parallelism, then it's not very compelling.  It's a reasonably compromise that we let a computer waste cycles so that developers can write faster and better and more reliably.

As time goes on the benefit of parallelism increases.  But as time goes on the relative value of developer time to processor time also increases, because processing gets cheaper.  The real benefit of parallelism is doing things we couldn't do before. It can feed into greater ubuquity of computing.  The admonitions imply some austere future where we *must* do things in parallel, and that won't come.

But I'm just pontificating.  My only real thought is that while there is an emphasis on declarative programming to enable parallelism, I think we should have an equal emphasis on deterministic programming. These two things are in some ways very similar, but I think "deterministic" is a more expansive idea that can encompass more programming techniques.  You could also say that "deterministic" is the same thing as "functional programming", but that term also has a lot of unnecessary baggage.  We want side effects, because we want code that affects things!  *Deterministic* means we identify all inputs and effects.  Like the data flow analog of strict static typing.

## Conclusion

It is productive to get computers to do the things that computers are good at.  The implication of the talk is that in the past we saw some potential in computers that we've lost.  But equally I think the mismatch between what we envisioned we'd do with computers, and what we are doing with computers, is that back then we *didn't see* all the things computers are good at.

The impact of computers has met or exceeded expectations.  It turns out computers are great for facilitating communication, and they are great at storing information, they can track history, facilitate transactions, and it's hardly necessary for me to enumerate the things we do with them.  And we shouldn't condemn developers for doing what is most impactful with the least effort.  But of course we must all, collectively and individually, determine what the most impactful *next* thing is to do.

We can mine the past for some of that, there's good stuff there.  But we shouldn't get bummed out just because there's more things to think about.  Rather it's exciting to find new things, even in the past.

[Comments on Hacker News](https://news.ycombinator.com/item?id=6601748)
