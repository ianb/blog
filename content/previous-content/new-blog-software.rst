New Blog Software (Previous)
############################
:date: 2007-08-01 12:02
:author: Ian Bicking
:tags: Non-technical

.. -*- mode: rst -*-

I've switched my software over to WordPress.  This was long overdue, as anyone who ever wanted to read anything at all on this site probably knows.  Sometime I should really write an article reflecting on the failures of my previous blog software.  Lets just say that flat files aren't so hot either.

Now that my software doesn't suck, I have lots of posts I have been embarrassed to write because every new post potentially introduced new people to my crappy site.

Hopefully everything is setup correctly, redirects, archives, and the new feed.

My one worry is WordPress comments, which suck a bit.  They shouldn't collect the horrible quantity of spam that the old site has, so that's good, but I hate disconnected streams of comments.  I've tried to modify the theme on this site to be more roomy, with less of the excessive whitespace that has become the norm.  I hope this whitespace kick goes the way of Creating Killer Websites Using Table Based Layout.  I.e., it'll soon look dated and everyone will move on.  So I hope you'll have more than two inches of width to comment in.  Honestly I wonder if I should just ditch WordPress comments and use something else entirely, like some kind of forum software and rig in some way of including the comments in the theme.  I wanted to install `threaded comments <http://meidell.dk/archives/2004/09/04/nested-comments />`_, but the installation process is rather invasive.

For editing I turned TinyMCE off (ugh), and installed `a restructured text plugin <http://goldenspud.com/rotr/index.php/2006/12/15/using-restructuredtext-with-wordpress />`_.   It took a while to figure out, since I have to include ``.. -*- mode: rst -*-`` in the header of each post.  Oh well, a minor inconvenience.  I used `Text Control <http://wordpress.org/extend/plugins/text-control />`_ to enable Markdown in comments, but I had to replace the actual ``markdown.php`` it used, which was broken.
