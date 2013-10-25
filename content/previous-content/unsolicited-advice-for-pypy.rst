My Unsolicited Advice For PyPy
##############################
:date: 2011-04-04 09:23
:author: Admin
:tags: Programming, Python

I think the most interesting work in programming languages right now is about the *runtime*, not syntax or even the languages themselves. Which places PyPy in an interesting position, as they have put a great deal of effort into abstracting out the concept of runtime from the language they are implementing (Python).

There are of course other runtime environments available to Python. The main environment has and continues to be CPython -- the runtime developed in parallel with the language, and with continuous incremental feedback and improvement by the Python developer community.  It is the runtime that informs and is informed by the language.  It's also the runtime that is most easy-going about integrating with C libraries, and by extension it is part of the vague but important runtime environment of "Unix".  There's also Jython and IronPython.  I frankly find these completely uninteresting.  They are runtimes controlled by companies, not communities, and the Python implementations are neither natural parts of their runtime environments, nor do the runtimes include many concessions to make themselves natural for Python.

PyPy is somewhere different.  It still has a tremendous challenge because Python was not developed *for* PyPy.  Even small changes to the language seem impossible -- something as seemingly innocuous as making builtins static seems to be stuck in a conservative reluctance to change.  But unlike Jython and IronPython they aren't stuck between a rock and a hard place; they just have to deal with the rock, not the hard place.

So here is my unsolicited advice on what PyPy-the-runtime should consider.  Simple improvements to performance and the runtime are fine, but being incrementally better than CPython only goes so far, and I personally doubt it will ever make a big impact on Python that way.

PyPy should push hard on *concurrency* and *reliability*.  If it is *fast enough* then that's fine; that's done as far as I'm concerned. I say this because I'm a web programmer, and speed is uninteresting to me.  Certainly opinions will differ.  But to me speed (as it's normally defined) is really *really* uninteresting.  When or if I care about speed I'm probably more drawn to Cython.  I *do* care about latency, memory efficiency, scalability/concurrency, resource efficiency, and most of all *worst cases*.  I don't think a JIT addresses any of these (and can even make things worse).  I don't know of benchmarks that measure these parameters either.

I want a runtime with new and novel features; something that isn't just incrementally better than CPython.  This itself might seem controversial, as the only point to such novel features would be for people to implement at least some code intended for *only* PyPy.  But if the features are good enough then I'm okay with this -- and if I'm not drawn to write something that will only work on PyPy, I probably won't be drawn to use PyPy *at all*; natural conservatism and inertia will keep me (and most people) on CPython indefinitely.

What do I want?

* **Microprocesses**.  Stackless and greenlets have given us micro-threads, but it's just not the same.  Which is not entirely a criticism -- it shows that unportable features *are* interesting when they are good features.  But I want the next step, which is processes that don't share state.  (And implicitly I don't just want standard async techniques, which use explicit concurrency and shared state.)

* **Shared objects** across processes with **copy-on-write**; then you can efficiently share objects (like modules!) across concurrent processes without the danger of shared state, but without the overhead of copying *everything* you want to share.  Lack of this is hurting PHP, as you can't have a rich set of libraries and share-nothing without killing your performance.

* I'd rather see a break in compatibility for C extensions to support this new model, than to abandon what could be PyPy's best feature to support CPython's C extension ecosystem.  Being a web programmer I honestly don't need many C modules, so maybe I'm biased.  But if the rest of the system is good enough then the C extensions will come.

* Make sure resource sharing that happens outside of the Python environment is really solid.  C libraries are often going to be unfriendly towards microprocesses; make sure what *is* exposed to the Python environment is solid.  That might even mean a dangerous process mode that can handle ctypes and FFI and where you carefully write Python code that has extra powers, so long as there's a strong wall between that code and "general" code that makes use of those services.

* **Cython** -- it's doing a lot of good stuff, and has a much more conservative but also more predictable path to performance (through things like type annotation).  I think it's worth leaning on.  I also have something of a hunch that it could be a good way to do FFI in a safe manner, as Cython already supports multiple targets (Python 2 and 3) from the same codebase.  Could PyPy be another target?

* **Runtime introspection of the runtime**.  We have great language introspection (probably much to the annoyance of PyPy developers who have to copy this) but currently runtime introspection is poor-to-nonexistant. What processes are running?  How much memory is each using?  Where? Are they holding on to resources?  Are they blocking on some non-Python library?  How much CPU have they been using?  Then I want to be able to kill processes, send them signals, adjust priorities, etc.

And I guess it doesn't have to be "PyPy", but a new backend for PyPy to target; it doesn't have to be the *only* path PyPy pursues.

With a runtime like this PyPy could be an absolutely rocking platform for web development.  Python could be as reliable as, oh... `PHP <http://blog.ianbicking.org/2008/01/12/what-php-deployment-gets-right />`_? Sorry, I probably won't win arguments that way ;)  As good as Erlang! Maybe we could get the benefits of async without the pain of callbacks or Deferreds. And these are features people would *use*.  Right now I'm perceiving a problem where there's lots of people standing on the sidelines cheering you on but not actually *using* PyPy.

So: I wouldn't tell anyone what to do, and if someone tries this out I'll probably only be on the sidelines cheering you on... but I really think this could be awesome.

**Update**: there's some `interesting comments on Hacker News <http://news.ycombinator.com/item?id=2406920>`_ as well.  
