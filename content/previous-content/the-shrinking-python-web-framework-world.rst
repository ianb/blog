The Shrinking Python Web Framework World
########################################
:date: 2007-08-21 23:25
:author: Ian Bicking
:tags: Programming, Python, Web

When I was writing the summary of `differences between WebOb and other request objects <http://pythonpaste.org/webob/differences.html>`_, to remind myself of web frameworks I might have forgotten I went to the `WebFrameworks page <http://wiki.python.org/moin/WebFrameworks>`_ on the Python wiki.

Looking through that page I'm reminded how many framework options there have been.  And I was further reminded of how few relevant options there are now.  From all this, there have emerged just a few options: Django, Pylons, TurboGears, Zope.  No offense to anyone left out of that list -- I know there's some other actively developed frameworks out there.  But frankly they aren't serious choices; they might be fine internal tools, or interesting experiments, but they are clearly on a different tier (and they all have questionable futures).

And now that `TurboGears 2 will be based on Pylons <http://groups.google.com/group/turbogears/browse_thread/thread/d1d2e416023e7033>`_ the list looks smaller still.

For a long, long time (longer than most of those frameworks have existed) people have complained about the proliferation of web frameworks in Python.  Those of us involved in developing web frameworks in Python haven't been able to respond all that well. Complaining doesn't magically lead to solutions, and you can't just will there to be a single Python web framework.  You can work towards that, but that's what we've been doing... mostly people don't seem to notice.  It's just not an easy thing to work towards; the problem space for a web framework isn't well defined, its end goal is far more vague than most people immediately realize, and it involves *consensus*, which makes everything much harder.  We said the market would decide, which is kind of a cop out (the market decides through the decisions of developers) but that's the best answer we had.

But after all this time, it seems clear that we are getting much closer to that goal.  If you squint *really* hard, you can almost imagine we *are* there.  The *total* list of frameworks only gets longer over time -- that's how open source works -- but the list of *choices* has become quite compact.

How we get to the next level is a little less clear.  We've gotten this way largely through attrition, but that's not going to get us any further.  I'll at least assure people that we are discussing this stuff -- it's slow going, but everyone is interested.  And if anyone actually wants to do some leg work to move this forward, a lot of the work is actually technical, not political, so don't be afraid to jump in.
