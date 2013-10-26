Monkeypatching and dead ends
############################
:date: 2008-03-21 17:38
:author: Ian Bicking
:tags: Programming, Python, Ruby

`Bill de hÓra <http://www.dehora.net/journal/2008/03/21/rope />`_ and then `Patrick Logan <http://patricklogan.blogspot.com/2008/03/another-dynamic-tools-topic-are-you.html>`_ picked up on an `old post of mine about monkeypatching <http://blog.ianbicking.org/theres-so-much-more-than-rails.html>`_.  

Patrick's reply:

    I know next to nothing about the specific problems the Ruby and Python folks are encountering with "monkeypatching". However this capability is nothing new for dynamic languages. And it is a frequent desire for me when I program in C-like languages. If you become frustrated using static "utility" methods, for example in Java, that work with "closed" classes (say, String or Object), then you have at least some desire for these "monkeypatches".

    See the thing is this capability *is* a cool feature in many Lisp and most Smalltalk systems. Sorry, dear readers who hate my Smug Lisp Weeniness. But it is true. Not only is it "cool," moreover it is *pragmatic*.

    The truly good implementations of dynamic languages recognize the advantages of these kinds of extensions, and they've supported them with good tools for decades. Learn from it, don't run from it. 

Sharp tools are good.  I would not want monkeypatching removed from Python.  Still, it's best not to leave sharp tools lying around.  It's best not to mix your butter knives with your steak knives.  I don't resent the safety guards on circular saws.

And sorry Lisp Weenies: your experiences are not so novel anymore.  The Python community isn't new to this dynamic typing thing.  We've taken some hits and we've learned from them.  And frankly the problems with runtime patching of methods can't be specific to Python or Ruby.  It only took the Ruby community a couple years to start `catching on <http://avdi.org/devblog/2008/02/23/why-monkeypatching-is-destroying-ruby />`_.  Are you telling me Lisp and Smalltalk programmers still haven't figured this out?  Everything you value about modularity is at risk when you monkeypatch code.  That risk can be worth it, of course!  But do you really need me to explain the benefits of modularity?  What's next, a recap of the problems with GOTO?

One of the things that I think distinguishes Python among the popular dynamically typed languages of the day, is that it's built -- languages and libraries -- on a great deal of concrete experience.  Experience *about developing with Python*.  There was a time when people tended to define Python as a delta from Java or Perl or C.  We don't need to do that anymore.  Sure, closed classes in Java suck.  Python isn't a reaction to Java's suckiness.  That we can do something Java can't doesn't get me excited.  This feature of monkeypatching has to stand up on its own, and while sometimes its use is justified those cases are few and far between.  That's what we've learned: monkeypatching was not dismissed out of hand, it was not dismissed because of anything in Java, it was dismissed because people *used* it without acknowledging it as a hack, and it *sucked*.

Of course the use cases are still there.  Which is why people `are trying new things <http://www.bud.ca/blog/the-great-python-component-swap-meet>`_ to address these problems.  One benefit of experience is that you know some paths are dead ends.  We still haven't figured out The One Right Path (and `we never will <http://blog.ianbicking.org/because-unanswered-problems-are-always-hard.html>`_), and maybe we've only traced out the longest path in a very long dead end in this maze of ideas we are traversing.  Since I doubt the maze has any exit (nirvana?) it's a valid debate about where we are trying to get at all.  That said, I suspect we've out-explored Lisp.  Lisp has been a worthy mentor, an intrepid explorer in his time, but he's old and doesn't get out much and only tells stories of where he's been in the past.  There are still things to be learned there, wisdom to be dug out of that environment, but Lisp and Python are not peers.
