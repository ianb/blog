The Web Server Benchmarking We Need
###################################
:date: 2010-03-16 17:23
:author: Ian Bicking
:tags: Programming, Python, Silver Lining, Web

Another `WSGI web server benchmark <http://nichol.as/benchmark-of-python-web-servers>`_ was published.  It's a decent benchmark, despite some criticisms.  But it benchmarks what everyone benchmarks: serving up a trivial app really really quickly.  This is not very useful to me.  Also, performance is not to me the most important differentiation of servers.

In `Silver Lining <http://cloudsilverlining.org>`_ we're using `mod_wsgi <http://code.google.com/p/modwsgi />`_.  Silver Lining isn't tied to mod_wsgi (applications can't really tell), and we may revisit that decision (mostly because of memory concerns), but it is a deliberate choice.  mod_wsgi is one of the few multiprocess WSGI servers, and it manages its children (the same way Apache manages all its children).  So if a child stops responding, it gets taken out of the pool and killed (brutal efficiency!  Or at least brutal terminology).  Child processes are also recycled, guarding against memory leaks or other peculiarities.  Sometimes these kinds of things are dismissed for covering up bugs, but (a) production is a lousy time to learn about bugs, (b) it's like a third tier of garbage collection, and (c) the bugs you are avoiding are often bugs you can't fix anyway (for instance, if your mysql driver leaks memory, is that the application developer's fault?)

I wish there was competition among servers not to see who can tweak their performance for entirely unrealistic situations, but to see who can implement the most fail-safe server.  We're missing good benchmarks.  Unfortunately benchmarks are a pain in the butt to write and manage.

But I hope someone writes a benchmark like that.  Here's some things I'd like to see benchmarked:

* A "realistic" CPU-bound application.  ``for i in xrange(10000000): pass`` is a reasonable start.

* An application that generates big responses, e.g., ``"x"*100000``.

* An I/O bound application.  E.g., one that reads a big file.

* A simply slow application (``time.sleep(1)``).

* Applications that wedge.  ``while 1: pass`` perhaps?  Or ``lock = threading.Lock(); lock.acquire(); lock.acquire()``.  Wedging in C and wedging in Python are different, so a bunch of different kinds of wedging.

* Applications that segfault.  ctypes is specially designed for this.

* Applications that leak memory like a sieve, e.g., ``global_var.extend(['x']*10000)``.

* Large uploads.

* Slow uploads, like a client that takes 30 seconds to upload 1Mb.

* Also slow downloads.

* In each case it is interesting what happens when something bad happens to just a portion of requests.  E.g., if 1% of requests wedge hard.  A good container will serve the other 99% of requests properly.  A bad container will have its worker pool exhausted and completely stop.

* Mixing and matching these could be interesting.  For instance Dave Beazley `found some bad GIL results mixing I/O and CPU-bound code <http://www.dabeaz.com/blog/2010/02/revisiting-thread-priorities-and-new.html>`_.

* Add ideas in the comments and I'll copy them into this list.

The hardest part of writing this is not the applications (they are simple).  One annoyance is wiring up the applications, but handily Nicholas covers that well in `his benchmark <http://nichol.as/benchmark-of-python-web-servers>`_.  You also have to make sure to clean up, as many servers will not exit cleanly from some of the tests.  Another nuisance is that some of these require funny clients.  These aren't too hard to write, but you can't just use ``ab``.  Then you have to report.

Anyway: I would **love it** if someone did this, and packaged it as repeatable/runnable code/scripts.  I'll help some, but I can't lead.  I'd both really like to see the results, and in my ideal world people writing servers would start using these benchmarks to make their servers more robust.
