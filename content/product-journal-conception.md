Title: A Product Journal: Conception
Slug: product-journal-conception
Category: mozilla
Tags: product-journal
Date: 2015-01-15

> I'm going to try to journal the process of a new product that I'm developing in [Mozilla Cloud Services](https://blog.mozilla.org/services/)

When [Labs closed and I entered management](http://www.ianbicking.org/blog/2014/09/professional-transitions.html) I decided not to do any programming for a while.  I had a lot to learn about management, and that's what I needed to focus on.  Whether I learned what I need to I don't know, but I have been getting [a bit tired](http://www.ianbicking.org/blog/2015/01/being-a-manager-is-lonely.html).

We went through a fairly extensive planning process towards the end of 2014.  I thought it was a good process.  We didn't end up where we started, which is a good sign – often planning processes are just documenting the conventional wisdom and status quo of a group or project, but in a critically engaged process you are open to considering and reconsidering your goals and commitments.

Mozilla is undergoing some stress right now.  We [have a new search deal](https://blog.mozilla.org/press/2014/11/yahoo-and-mozilla-form-strategic-partnership/), which is good, but we've been seeing [declining marketshare](http://www.forbes.com/sites/antonyleather/2014/08/04/google-chrome-browser-market-share-tops-20-leaves-firefox-in-its-dust/) which is bad.  And then when you consider that desktop browsers are themselves a decreasing share of the market it looks worse.

The first planning around this has been to decrease attrition among our existing users.  Longer term much of the focus has been in increasing the quality of our product.  A noble goal of course, but does it lead to growth?  I suspect it can only address attrition, the people who don't use Firefox but could won't have an opportunity to see what we are making.  If you have other growth techniques then focusing on attrition can be sufficient.  Chrome for instance does significant advertising and has deals to side-load Chrome onto people's computers. Mozilla doesn't have the same resources for that kind of growth.

When finished up the planning process I realized, *damn*, all our plans were about product quality.  And I liked our plan!  But something was missing.

This perplexed me for a while, but I didn't really know what to make of it.  Talking with a friend about it he asked *then what do you want to make?* – a seemingly obvious question that no one had asked me, and somehow hearing the question coming at me was important.

Talking through ideas, I reluctantly kept coming back to sharing. It's the most incredibly obvious growth-oriented product area, since every use of a product is a way to implore non-users to switch.  But sharing is so competitive.  When I first started with Mozilla we would obsess over the problem of Facebook and Twitter and silos, and then think about it until we threw our hands up in despair.

But I've had this trick up my sleeve that I pull out for one project after another because I think it's a really good trick: make a static copy of the live DOM.  Mostly you just iterate over the elements, get rid of scripts and stuff, do a few other clever things, use `<base href>` and you are done!  It's like a screenshot, but it's also still a webpage.  I've been trying to do something with this [for a long time](http://pythonhosted.org/Deliverance/).  This time let's use it for sharing...?

So, the first attempt at a concept: freeze the page as though it's a fancy screenshot, upload it somewhere with a URL, maybe add some fun features because now it's disassociated from its original location. The resulting page won't 404, you can save personalized or dynamic content, we could add highlighting or other features.

The big difference with past ideas I've encountered is that here we're not trying to compete with *how* anyone shares things, this is a tool to improve *what* you share.  That's compatible with Facebook and Twitter and SMS and *anything*.

If you think pulling a technology out of your back pocket and building a product around it is like putting the cart in front of the horse, well maybe... but you have to start somewhere.

[The next post in the series is [The Tech Demo](http://www.ianbicking.org/blog/2015/01/product-journal-tech-demo.html)]
