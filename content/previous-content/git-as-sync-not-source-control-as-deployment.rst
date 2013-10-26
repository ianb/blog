Git-as-sync, not source-control-as-deployment
#############################################
:date: 2012-02-14 02:30
:author: Admin
:tags: Programming, Web

I don't like systems that use ``git push`` for deployment (Heroku et al).  Why?  I do a lot of this::

    $ git push deploy
    ... realize I forgot a domain name ...
    $ git commit -m "fix domain name" -a ; git push deploy
    ... realize I didn't do something right with the database setup ...
    $ git commit -m "configure database right" -a ; git push deploy
    ... dammit, I didn't fix it quite right ...
    $ git commit -m "typo" -a ; git push deploy

And then maybe I'd actually like to keep my config out of my source control, or have a build process that I run locally, or any number of things.  I'd like to be able to test deployment, but every deployment is a commit, and I like to commit *tested* work.  I think I could use ``git rebase`` but I lack the discipline to undo my work so I can do it correctly.  This is why I don't do continuous commits.

There's a whole different level of weirdness when you use `GitHub Pages <http://pages.github.com />`_ as you aren't pushing to a deployment-specific remote, you are pushing to a deployment-specific branch.

So I've generally thought: git deployment is wrong.

Then I was talking to some other people at Mozilla and they mentioned that ops was using git for simply moving files around even though the stuff they were deploying was itself in Mercurial.  They had a particular site with a very large number of files, and it was faster to use git than rsync (git has more metadata than rsync; rsync has to look at *everything* everytime you sync).  And that all seemed very reasonable; git is a fine way to sync things.

But I kind of forgot about it all, and just swore to myself as I did too many trivial commits and wrote too many meaningless commit messages.

Still... it isn't so hard to separate these concerns, is it?  So I wrote up a `quite small command <https://github.com/ianb/git-sync/blob/master/git-sync>`_ called `git-sync <https://github.com/ianb/git-sync>`_.  The basic idea: copy the working directory to a new location (minus ``.git/``), commit that, and push the result to your deployment remote.  You can send modified and untracked files, and you can run a build script before committing and push the *result* of the build script, all without sullying your "real" source control.  And you happen to have a nice history of deployments, which is also nice.

I've only used this a little bit, but I've enjoyed when I have used it, and it makes me feel much better/clearer about my actual commits.  It's really short right now, and probably gets some things entirely wrong (e.g., moving over untracked files).  But it works well enough to be improved (*winkwinknudgenudge*).

So check it out: https://github.com/ianb/git-sync
