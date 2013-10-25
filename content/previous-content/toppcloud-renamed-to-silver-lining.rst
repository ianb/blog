toppcloud renamed to Silver Lining
##################################
:date: 2010-03-03 20:18
:author: Ian Bicking
:tags: Packaging, Programming, Python, Silver Lining, Web

After some pondering at PyCon, I decided on a new name for toppcloud: **Silver Lining**.  I'll credit a mysterious commenter "david" with the name idea.  The command line is simply ``silver`` -- ``silver update`` has a nice ring to it.

There's a new site: `cloudsilverlining.org <http://cloudsilverlining.org>`_; not notably different than the old site, just a new name.  The product is self-hosting now, using a `simple app <http://bitbucket.org/ianb/silverlining />`_ that runs after every commit to regenerate the docs, and with a small extension to Silver Lining itself (to make it easier to host static files).  Now that it has a real name I also gave it a `real mailing list <http://groups.google.com/group/silverlining-dev>`_.

Silver Lining also has its `first test <http://bitbucket.org/ianb/silverlining/src/tip/tests/functional/runtest.py>`_.  Not an impressive test, but a test.  I'm hoping with a `VM-based libcloud backend <http://mail-archives.apache.org/mod_mbox/incubator-libcloud/201003.mbox/browser>`_ that a full integration test can run in a reasonable amount of time.  *Some* unit tests would be possible, but so far most of the bugs have been interaction bugs so I think integration tests will have to pull most of the weight.  (A continuous integration rig will be very useful; I am not sure if Silver Lining can self-host that, though it'd be nice/clever if it could.)
