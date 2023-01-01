Documents vs. Objects
#####################
:date: 2008-01-15 19:28
:author: Ian Bicking
:tags: Programming, Web

Let's imagine we live in a `late binding <http://en.wikipedia.org/wiki/Name_binding#Binding_time>`_ world, a programming world of messages, what should that look like?  What does it look like in the large?

The Smalltalk notion of this is many, many independent referencable objects.  Objects all the way down.  So you might get something like ``buddies do: [ buddy | buddy sendMessage: myMessage]``.

At runtime this means something like:

* Send the ``buddies`` object (some reference we obtained elsewhere)   the ``do:`` message, with the argument ``[ buddy | buddy   sendMessage: myMessage]``.  Except remember that that ``[...]`` is a   block (aka closure), and it's also an object.  Which only makes   sense, because ``buddies`` doesn't know what ``myMessage`` means.  So all ``buddies`` knows is that it gets an argument.

* The ``buddies`` object receives this ``do:`` message, with an   argument we'll call ``block`` (that ``[...]`` stuff).  By convention   ``do:`` is sent to sequence-like things, and calls its argument   multiple times.  So buddies figures out some items -- maybe it's a   concrete sequence (like an ``Array``) or maybe it looks it up in a   database, or does a call over the net, or whatever.

* Once ``buddies`` gets an item, it calls ``block value: item``.  That   is, it sends a ``value:`` message back to the ``block`` object, with   the argument ``item``.

* The block has just received that ``value:`` message.  The block   wouldn't *have* to be that ``[...]`` syntactic construct, it just   usually is.  So it receives that value, and locally binds the   ``buddy`` variable to the argument and evaluates the inside of that   block.

* Our expression then sends the ``sendMessage:`` message to that   buddy object, with another object as the argument.  That argument   might be a string, but it also might be markup, or a richer object   that itself does all sorts of magical things.  Maybe the buddy   object sends the object over the net to your remote buddy, then the   remote buddy calls ``message displayOn: myScreen``, and the message   object reponds to ``displayOn:`` by sending ``screen showText:   someString withColor: #blue``.  This can go on for a while.

As you can see, there can be a lot of tracing through code in this style.  This has been called `Ravioli code <http://en.wikipedia.org/wiki/Ravioli_code>`_.  Many people lean heavily on concepts like classes and methods to make sense of this kind of code, though if you look through my description you'll notice they don't show up; it is apparently somewhat frustrating for Alan Kay that he first used the term "object-oriented" when he would have preferred this message-oriented concept.  Classes and methods are just implementation details.  Messages and object references are the true fundamental concept.

Doing this in the large means that a lot of these messages go over the network.  It means we can get a handle to an object that lives on another computer.  It *might* result in a system that is very chatty (many systems with transparent RPC do end up being unintentionally chatty).  But it doesn't have to.  You can make this asynchronous to facilitate these kinds of efficiencies.

That said, there is another distinct technique for programming in the large: document oriented programming.  This is what REST is focused on: transmitting state in as complete a form as feasible, with explicit references whenever referring to another resource.

Resources and objects are in many ways similar, but in other ways completely opposite.  An object has behavior but no visible state.  It responds to messages, passing more objects along.  Resources themselves have no behavior.  They are just bare state.  REST and the web *kind of* adds behavior, but strict REST avoids even that.  PUT is not behavior.  PUT is almost like a declaration of fact.  When you PUT to a resource you are claiming that the new state of the resource represents the truth of that resource.  Any behavior that occurs because of that is hidden.  Other resources may change as a result of the PUT, but this is not exposed in any way.  To find out what's changed you simply have to refresh all the state you've acquired -- re-GET the resources.  (POST, except when used simply to create a resource, is more like a verb than a statement of truth; the HTTP model is not pure in this respect.)

For programming on a web scale resources have become the dominant technique.  REST was really an acknowledgement of this idea, not the invention of it.  It's also an advocacy effort that our future work should be built on this past success.  It's been focused very clearly on advocating resources over the object/message-based systems of WS-\*, but the WS-\* design is hardly the first or only object based system of its kind; anything called "RPC" comes from that line of thinking.  But now that WS-\* isn't king of the hill anymore maybe we can more be more thoughtful about how REST relates to other programming techniques.

A way to describe the difference in terms of programming language design is that with resources everything we do is `call by value <http://en.wikipedia.org/wiki/Call_by_value#Call_by_value>`_.  Resources are *values*, and we pass them around in their complete form.  You can pass around a reference value (a URI), but this is like calling a function with a pointer argument.  Object/RPC techniques are `call by reference <http://en.wikipedia.org/wiki/Call_by_value#Call_by_reference>`_ (though at some level there are true "values", things like integers and strings, as things would simply be too chatty otherwise).

One interesting place where objects and resources can overlap is in functional programming.  Thinking in terms of call by value or call by reference, in a functional programming language these are identical.  Because values are not mutable a value and a copy of the value are equivalent.  You can also pass an object between systems by reference, in whole, or some lazy compromise where the object is only incrementally communicated between the processes.

Resources are in a sense immutable regardless of your programming language.  When you retrieve a resource you cannot modify it in place, as the result is no longer representative of what the resource really *is*.  You can put a new resource in a named location (PUT), and you can copy resources (maybe making an internal copy).  Incidentally this is why I think `literal document models are best <https://ianbicking.org/2007/08/02/atom-models />`_.  It would probably be useful to have a native representation of what a "resource" really is in programming languages, though usually this is not done.  A resource should really be a document (content type, some bytes, perhaps a cache of parsed representations) plus the name (URI) and the *time*.  Resources aren't eternal, but given a time and URI there is (in a REST world) a single canonical representation.

Further investigations of functional programming languages would probably be useful here.  I believe strict functional languages have interesting metaphors for handling this kind of information; the eternal immutable sense of what a thing is at a point in time, and a way to reconcile the incomplete knowledge of what a resource is *right now*.  I don't think this is a clear pattern in Erlang, but is in Haskell.

One useful aspect of resources is the ability to spy on the process, to get a snapshot of it, to understand it in a kind of literal way.  This is *view source* in a browser, or just poking around with curl.  You can feel a certain confidence that you can get a real sense of what the truth is using these tools.  In an object-based system you can only poke around with a process of 20 questions, hoping that there isn't some hidden truth that you are unaware of.  For instance, talking to a proxy that is *almost exactly* like the original object, but with some small replacement.  Of course internally a server can be peculiarly coupled as well, with relationships between the resources that aren't explicit or obvious.  But at least the faces it projects are fully formed.

I still haven't fully figured out what distinguishes a document model from an object model, but I think the distinction between the two contains some interesting stuff worth exploring.
