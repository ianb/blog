Thoughts About the Erlang Runtime
#################################
:date: 2008-06-09 18:03
:author: Ian Bicking
:tags: Erlang, Programming, Python

I should preface this entire post by noting that I haven't used Erlang, just read about it, and I handle most concurrency using Python threads, a model for which I have no great affection (or hate).  But I was reading `two <http://patricklogan.blogspot.com/2008/05/toward-finer-tuning-of-definitions-of.html>`_ `posts <http://patricklogan.blogspot.com/2008/05/this-is-part-two-of-my-response-to-ted.html>`_ by Patrick Logan on Erlang and it got me thinking again.

From my reading and what I've heard from other people, Erlang the language-and-syntax seems quite crufty.  Erlang is not the Complete Package, the language that will make you leave your wife, the language that will have you walking into telephone polls because it's just so *hot* that you can't take your eyes off it.  Erlang is not that language.  People seem to get excited about two things in Erlang: the concurrency model and pattern matching.  I'm not quite sure why people are excited about pattern matching.  `Pattern matching isn't particularly hard to implement <http://svn.colorstudy.com/home/ianb/recipes/patmatch.py>`_, though maybe it interacts with other aspects of the system in a way I don't understand.  I remain skeptical that it's anything special.

Then there is the concurrency model (and its associated message passing), and this *does* strike me as special.  You can `kind of <http://candygram.sourceforge.net />`_ implement that model in Python, but with none of the concrete benefits.

These are the useful features I see in the concurrency model:

1. Erlang processes are share-nothing.

2. The processes are light weight.  You can start lots of processes, and they start quickly and can die off quickly without any great overhead.  They aren't OS-level processes.  These are sometimes called green processes or microprocesses.  There are many implementations of micro\ *threads* in Python, but you lose the benefits of share-nothing.

3. The runtime makes light weight processes feasible as well.  The OS overhead of a Python process is actually just a small part of the total overhead when spawning a process.  Loading and initializing the runtime libraries of a Python program of even modest complexity is problematic.  I'm not sure exactly how Erlang does this, but I suspect it's because libraries can be safely shared because Erlang is a functional language.  (`PHP is also like this <https://ianbicking.org/2008/01/12/what-php-deployment-gets-right />`_, with most of the library written in a sharable C library.)

1 and 2 can be handled with the right VM.  This isn't a particularly *common* VM design, but it's certainly doable.  3 is tricky, and effects the language design.

I don't think it effects the language design as greatly as to require a functional language.  It requires that sharable code itself be a functional (i.e., immutable) subset of the language.  What the code *does* doesn't have to be functional, only what the code *is*.

To explain this, functions in most languages are immutable.  Python functions aren't actually immutable, but they are close enough that hardly anyone would notice if you made them immutable (right now you can overwrite their name, compiled code, and some other stuff -- but almost no one actually does this).  The function may have side effects, but as long as the function *object* is immutable then it can be shared safely among processes.

You can extend this to the module as a whole.  This means you couldn't `monkeypatch <http://en.wikipedia.org/wiki/Monkey_patch>`_ objects in the module, and module-level assignments would effectively be constants.  Any module-level objects would have to be immutable.  Things like classes, which are also a kind of module-level object, would also have to be immutable -- meaning things like class variables would be immutable.  It could still be possible to do module-level code if there was a way of freezing the module after its instantiation (this would be important for Python, as even decorators are a kind of code run at import time).  Adding a general concept of "freezing" to the language might be the most general and expedient way to make modules sharable.

The other half of the concurrency model in Erlang is message passing.  Erlang processes send messages around like other systems send methods.  It would be possible to use exactly Erlang's system, as it's not Erlang-specific and has been ported to many languages.  Though I'd be somewhat more inclined to use `bencode <http://en.wikipedia.org/wiki/Bencode>`_ as it has some cleverness in its design.  Or perhaps JSON, just because.  Regardless of the format you are always passing around *data*, which I think is important.  Systems that pass around "objects" become complex, mostly because you just **cannot** pass objects around and so those systems are just complex facades built around data exchange.

Lately I've become fond of thinking of objects as views over a more fundamental data structure (`WebOb <http://pythonpaste.org/webob />`_ is strictly based on this pattern).  Methods are details of the implementation, but only the data can mean something to someone else.  At least this is the worldview you start to internalize when you think about REST a lot.  (My post `Documents vs. Objects <https://ianbicking.org/2008/01/15/documents-vs-objects />`_ is also about this.)

Arguable a plain-data-with-views world is just the `dynamic-weak-typed <https://ianbicking.org/because-unanswered-problems-are-always-hard.html>`_ anti-pattern.  That anti-pattern is one where you get all the disadvantages of dynamic typing, and all the disadvantages of static typing, all in one ugly bundle.  Erlang's records remind me of this anti-pattern.  Instead of dictionaries everything is a tuple, and getting a record is just syntactic sugar mapping record names to indexes -- all in the context of a dynamically typed language where you could mistype a value and get strange output as a result.

The strong-static typing solution to the type problem involves complicated contracts, aka "service descriptions", the stuff of WS-\*, CORBA IDL, etc.  The strong-dynamic typing solution is that every object have an explicit type.  This is fine for things we all agree on: lists, dictionaries, bytes, numbers.  Sadly even a basic thing like unicode strings cause problems, as do dates, but at least those have straight-forward solutions (you add more basic types to the message format).  More complex types, like a domain object (e.g., a user record) are difficult.  Are they all just dictionaries?  Dictionaries plus special metadata?  XML namespaces address this problem in some ways, but are also the point at which XML starts to just piss people off and make them want to use JSON.  And for good reason, because XML namespaces force you to define entities and responsible parties very early on, possibly long before you know what you are actually trying to do.  Besides XML, are there other systems that aren't just naive/unextendable (bencode, JSON) and are still basically dynamically typed?

This is the kind of thing I would really love to see `PyPy <http://codespeak.net/pypy />`_ experiment with.
