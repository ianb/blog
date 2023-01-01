Why toppcloud (Silver Lining) will not be agnostic
##################################################
:date: 2010-02-10 00:41
:author: Ian Bicking
:tags: Programming, Python, Silver Lining, Web

I haven't received a great deal of *specific* feedback on toppcloud (**update**: renamed Silver Lining), only a few people (Ben Bangert, Jorge Vargas) seem to have really dived deeply into it.  But -- and this is not unexpected -- I have already gotten several requests about making it more agnostic with respect to... stuff.  Maybe that it not (at least forever) require Ubuntu.  Or maybe that it should support different process models (e.g., threaded and multiple processes).  Or other versions of Python.

The more I think about it, and the more I work with the tool, the more confident I am that toppcloud should not be agnostic on these issues.  This is not so much about an "opinionated" tool; toppcloud is not actually very opinionated.  It's about a well-understood system.

For instance, Ben noticed a problem recently with `weird import errors <http://code.google.com/p/modwsgi/issues/detail?id=177>`_.  I don't know *quite* why mod_wsgi has this particular problem (when other WSGI servers that I've used haven't), but the fix isn't that hard.  So Ben `committed a fix <http://bitbucket.org/ianb/toppcloud/changeset/27a470352a5e />`_ and the problem went away.

Personally I think this is a bug with mod_wsgi.  Maybe it's also a Python bug.  But it doesn't really matter.  When a bug exists it "belongs" to everyone who encounters it.

toppcloud is not intended to be a transparent system.  When it's working correctly, you should be able to ignore most of the system and concentrate on the relatively simple abstractions given to your application.  So if the configuration reveals this particular bug in Python/mod_wsgi, then the bug is essentially a toppcloud bug, and toppcloud should (and *can*) fix it.

A more flexible system can ignore such problems as being "somewhere else" in the system.  Or, if you don't define these problems as someone else's problem, then a more flexible system is essentially always broken somewhere; there is always some untested combination, some new component, or some old component that might get pushed into the mix.  Fixes for one person's problem may introduce a new problem in someone else's stack.  Some fixes aren't even clear.  toppcloud has Varnish in place, so it's quite clear where a `fix related to Django and Varnish configuration goes <http://bitbucket.org/ianb/toppcloud/changeset/614d5366be67 />`_.  If these were each components developed by different people at different times (like with buildout recipes) then fixing something like this could get complicated.

So I feel very resolved: toppcloud will hardcode everything it possibly can.  Python 2.6 and only 2.6!  (Until 2.7, but then **only 2.7**!).  Only Varnish/Apache/mod_wsgi.  I haven't figured out threads/processes exactly, but once I do, there will be only one way!  And if I get it wrong, then everyone (**everyone**) will have to switch when it is corrected!  Because I'd much rather have a system that is inflexible than one that doesn't work.  With a clear and solid design I think it is feasible to get this to work, and that is no small feat.

Relatedly, `I think I'm going to change the name of toppcloud <https://ianbicking.org/2010/02/09/leaving-topp/comment-page-1/#comment-151194>`_, so ideas are welcome!
