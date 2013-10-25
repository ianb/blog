Configuration management: push vs. pull
#######################################
:date: 2010-03-10 19:45
:author: Ian Bicking
:tags: Programming, Silver Lining
:tags: puppet configuration "configuration management"

Since I've been thinking about `deployment <http://blog.ianbicking.org/category/silverlining>`_ I've been thinking a lot more about what "configuration management" means, how it should work, what it should do.

I guess my quick summary of configuration management is that it is *setting up a server correctly*.  "Correct" is an ambiguous term, but given that there are so many to configuration management the solutions are also ambiguous.

`Silver Lining <http://cloudsilverlining.org>`_ includes configuration management of a sort.  It is very simple.  Right now it is simply a bunch of files to rsync over, and one shell script (you can see the `files here <http://bitbucket.org/ianb/silverlining/src/tip/silverlining/server-files/serverroot />`_ and the `script here <http://bitbucket.org/ianb/silverlining/src/tip/silverlining/server-files/update-server-script.sh>`_ -- at least until I move them and those links start 404ing).  Also each "service" (e.g., a database) has a simple setup script.  I'm sure this system will become more complicated over time, but it's **really** simple right now, and I like that.

The other system I've been asked about the most about lately is `Puppet <http://reductivelabs.com/products/puppet />`_.  Puppet is a *real* configuration management system.  The driving forces are very different: I'm just trying to get a system set up that is in all ways *acceptable* for web application deployment.  I want *one* system set up for *one* kind of task; I am completely focused on that end, and I care about means only insofar as I don't want to get distracted by those means.  Puppet is for people who care about the means, not just the ends.  People who want things to work in a particular *way*; I only care that they *work*.

That's the big difference between Puppet and Silver Lining.  The smaller difference (that I want to talk about) is "push" vs. "pull".  `Grig wrote up some notes on two approaches <http://agiletesting.blogspot.com/2010/03/automated-deployment-systems-push-vs.html>`_.  Silver Lining uses a "push" system (though calling it a "system" is kind of overselling what it does) while Puppet is "pull".  Basically Silver Lining runs these commands (from your personal computer)::

    $ rsync -r <silverlining>/server-files/serverroot/ root@server:/
    $ ssh root@server "$(cat <silverlining>/server-files/update-server-script.sh)"

This is what happens when you run ``silver setup-node server``: it pushes a bunch of files over to the server, and runs a shell script.  If you update either of the files or the shell script you run ``silver setup-node`` again to update the server.  This is "push" because everything is initiated by the "master" (in this case, the developer's personal computer).

Puppet uses a pull model.  In this model there is a daemon running on every machine, and these machines call in to the master to see if there's any new instructions for them.  If there are, the daemon applies those instructions to the machine it is running on.

Grig identifies two big advantages to this pull model:

1. When a new server comes up it can get instructions from the master and start doing things.  You can't push instructions to a server that isn't there, and the server itself is most aware of when it is ready to do stuff.

2. If a lot of servers come up, they can all do the setup work on their own, they only have to ask the master what to do.

But... I don't buy either justification.

First: servers don't just *do* things when they start up.  To get this to work you have to create custom images with Puppet installed, and configured to know where the master is, and either the image or the master needs some indication of *what kind* of server you intended to create.  All this is to avoid polling a server to see when it comes online.  Polling a server is lame (and is the best Silver Lining can do right now), but avoiding polling can be done with something a lot simpler than a complete change from push to pull.

Second: there's nothing unscalable about push.  Look at those commands: one ``rsync`` and one ``ssh``.  The first is pretty darn cheap, and the second is cheap on the master and expensive on the remote machine (since it is doing things like installing stuff).  You need to do it on lots of machines?  Then fork a bunch of processes to run those two commands.  This is not complicated stuff.

It is *possible* to write a push system that is hard to scale, if the master is doing lots of work.  But just don't do that.  Upload your setup code to the remote server/slave and *run it there*.  Problem fixed!

What are the advantages of push?

1. Easy to bootstrap.  A bare server can be setup with push, no customization needed.  Any customization is another kind of configuration, and configuration should be automated, and... well, this is why it's a bootstrap problem.

2. Errors are synchronous: if your setup code doesn't work, your push system will get the error back, you don't need some fancy monitor and you don't need to check any logs.  Weird behavior is also synchronous; can't tell why servers are doing something?  Run the commands and watch the output.

3. Development is sensible: if you have a change to your setup scripts, you can try it out from your machine.  You don't need to do anything exceptional, your machine doesn't have to accept connections from the slave, you don't need special instructions to keep the slave from setting itself up as a production machine, there's no daemon that might need modifications... none of that.  You change the code, you run it, it works.

4. It's just so damn simple.  If you don't start thinking about push and pull and other design choices, it simply becomes: do the obvious and easy thing.

In conclusion: push is sensible, pull is needless complexity.
