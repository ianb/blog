Silver Lining: More People!
###########################
:date: 2010-04-21 21:20
:author: Ian Bicking
:tags: Python, Silver Lining, Web

OK... so I said before Silver Lining is for collaborators not users. And that's still true... it's not a polished experience where you can confidently ignore the innards of the tool.  But it does stuff, and it works, and you can use it.  So... I encourage some more of you to do so.

Now would be a perfectly good time, for instance, to port an application you use to the system.  Almost all Python applications should be portable.  The requirements are fairly simple:

1. The application needs a WSGI interface.
2. It needs to be Python 2.6 compatible.
3. Any libraries that aren't pure-Python need to be available as deb packages in some form.
4. Any persistence needs to be provided as a `service <http://cloudsilverlining.org/services.html>`_; if the appropriate service isn't already available you may need to write some code.

Also PHP applications should work (though you may encounter more rough edges), with these constraints:

1. No ``.htaccess`` files, so you have to implement any URL rewriting in PHP (e.g., `for WordPress <http://bitbucket.org/ianb/silverlining/src/tip/docs/examples/wordpress/runner.php>`_).
2. Source code is not writable, so self-installers that write files won't work.  (Self-installing plugins might be workable, but that hasn't been worked out yet.)
3. And the same constraints for services.

So... take an application, give it a try, and tell me what you encounter.

Also I'd love to get feedback and ideas from people with more sysadmin background, or who know Ubuntu/Debian tricks.  For instance, I'd like to handle some of the questions packages ask about on installation (right now they are all left as defaults, not always the right answer).  I imagine there's some non-interactive way to handle those questions but I haven't been able to find it.
