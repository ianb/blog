Title: Improving the web with small, composable tools
Date: 2018-02-05
Slug: web-small-composable-tools

[Firefox Screenshots](https://screenshots.firefox.com/) is the first [Test Pilot](https://testpilot.firefox.com/) experiment to graduate into Firefox, and it’s been surprisingly successful. You won’t see many people talking about it: it does what you expect, and it doesn’t cover new ground. Mozilla should do more of this.

# Small, Composable Tools

One of the inspirations for Firefox Screenshots was [user research done in 2015](https://blog.mozilla.org/ux/2015/02/save-share-revisit/). This research involved interviews with a few dozen people about how they save, share, and recall information. I myself had a chance to be part of several house visits in Rochester, NY. We looked over people’s shoulders while they showed us how they worked.

My biggest takeaways from that research:

* There is a wide variety of how people manage their information, with many combinations of different tools and complex workflows
* Everyone is pretty happy with what they are doing
* People only want small, incremental changes
* Screenshots are pretty popular

It was surprising to see how complicated and sometimes clearly suboptimal people’s workflows were, while also understanding that each person was happy with what they did. They were happy because they weren’t looking for something new. At any moment most people are settled ([satisficed](https://www.nngroup.com/articles/satisficing/)) on a process, and they have better things to do than constantly reconsider those choices.

After learning how they worked, we’d sometimes offer up alternatives and get reactions. The alternatives received lots of crickets. If you could add a tool to existing workflows then there might be interest, but there wasn’t interest in replacing tools unless perhaps it was a one-to-one match. People specifically weren’t interested in integrated tools, ones that improved the entire workflow.

And who among us hasn’t been burned by overenthusiasm for a fully integrated tool? It seems great, then it gets tiring just to keep track, annoying to try to get people to sign up so you can collaborate, some number of things don’t fit into the process, you’ve lost track of your old things, it just feels like work.

# Old Philosophies

The [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Origin):

* Write programs that do one thing and do it well.
* Write programs to work together.
* Write programs to handle text streams, because that is a universal interface.

This is still what works well, and still what people want! This is also what the web can provide and apps and silos cannot: open composability.

This isn’t the same as APIs and integrated tools: `find` and `grep` are not integrated, you don’t have to setup OAuth integration between `tail` and `tee`. Things work together because you use them together.

What would the Unix toolset look like on the web? Please speculate! [I've started structuring some of my own ideas into a set of notes](https://docs.google.com/document/d/1NSO_Nl426o5Wuv896qk7vLudbf-z9FQSZf8fDBWPlwk/edit?usp=sharing).

# Stop Being So Clever

At the time of the user research myself and [Donovan](http://donovanpreston.com/) had been working on an experiment in page capture – you could think of it like a personal archive.org. We added screenshotting as an entree into what felt like a more advanced tool.

In the end nothing is left of that original concept, and we just have plain screenshots. It hurt to see that all go. Screenshots are not exciting, and they are not innovative, and there is nothing very new about them. And clearly I needed to get over myself.

And so this is a lesson in humility: things don’t have to be new or novel or exciting to be useful. Screenshots is so un-new, so un-novel, so un-exciting that we aren’t even following along with the competition. Mozilla should spend more time here: behind the curve where the big players stopped caring and the little players have a hard time getting any attention. Behind the curve is where the web was a lot more like how Mozilla wants it to be.

There are lots of useful things back here, things that technophiles have appreciated but the wider population doesn’t know how to use. A pastebin. Site archival. Deep linking. Inline linking at all! Scraping. Clipboard management. Etherpad is still the best lightweight collaborative editor. Little stuff, things that don’t try to take over, things that don’t try to leverage the user for corporate benefit. This stuff is not very hard to make, and is affordable to run. Combine that with a commitment to keep the services competently maintained and openly interoperable, and there’s a lot of value to provide. And that’s what Mozilla is in it for: to be of service.

# Being Part Of The Web

Screenshots was not easy to make. It was not *technically* difficult, but it was not easy.

Mozilla has long been reluctant to host user content. Firefox Sync is pointedly encrypted on the client. Before Screenshots the only unencrypted user content the corporation handled was the add-ons and themes on addons.mozilla.org.

Screenshots did not have to have a server component, and it did not have to allow people to upload or share shots within the tool. I take some pride in the fact that, despite all our cultural and legal attitudes at Mozilla, screenshots.firefox.com is a thing. It required a great deal of stubbornness on my part, and at times a pointed blindness to feedback.

In a small way Screenshots makes Mozilla part of the web, not just a window onto the web. This is a direction I think we should take: `*.firefox.com` links of all kinds should become normal, and you should know that on the other side of the link will be respectful content, it won’t be an avenue for manipulation, and you won’t be a product. Be the change you want to see, right?

> Thanks to Wil Clouser and Jared Hirsch for feedback on this post.
