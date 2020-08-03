Title: A Product Journal: Oops We Made A Scraper
Slug: product-journal-oops-a-scraper
Category: mozilla
Tags: product-journal
Date: 2016-08-15

> I'm blogging about the development of a new product in Mozilla, [look here for my other posts in this series](http://www.ianbicking.org/tag/product-journal.html)

A while back we got our [first contributor](https://github.com/ben-en) to [PageShot](https://github.com/mozilla-services/pageshot/), who contributed a feature he wanted for [Outernet](https://outernet.is/) – the ability to use PageShot to create readable and packaged versions of websites for distribution.  Outernet is a neat project: they are building satellite capacity to distribute content anywhere in the world.  But it's purely one-way, so any content you send has to be complete.  And PageShot tries pretty hard to identify and normalize all that content.

Lately I spent a week with the [Activity Stream](https://wiki.mozilla.org/Firefox/Activity_Stream) team, and got to thinking about the development process around recommendations.  I'd like to be able to take my entire history and actually get the content, and see what I can learn from that.

And there's this feature in PageShot to do just that!  You can install the add-on and enable the pref to make the browser into a server:

<figure style="background-color: rgba(240, 240, 240, 0.4); padding: 5px; width: 90%; border: 1px solid #aaa; border-radius: 3px;"><a href="/media/pageshot-server-pref-screenshot.png"><img style="width: 100%; height: auto" src="/media/pageshot-server-pref-screenshot.png" /></a><figcaption style="font-size: 80%; line-height: 1em; text-align: center;"><tt>about:addons</tt> prefs</figcaption></figure>

After that you can get the shot data from a page with a simple command:

```sh
$ url=https://mail.google.com
$ server=http://localhost:10082
$ curl "${server}/data/?url=${url}&allowUnknownAttributes=true&delayAfterLoad=1000" > data.json
```

`allowUnknownAttributes` preserves attributes like `data-*` attributes that you might find useful in your processing.  `delayAfterLoad` gives the milliseconds to wait, usually for the page to "settle".

A fun part of this is that because it's in a regular browser it will automatically pick up your profile and scrape the page *as* you, and you'll literally see a new tab open for a second and then close.  Install an ad blocker or anything else and its changes will also be applied.

The thing you get back will be a big JSON object:

```javascript
{
  "bodyAttrs": ["name", "value"],
  "headAttrs": [], "htmlAttrs": [],
  "head": "html string",
  "body": "html string",
  "resources": {
    "uuid": {
      "url": "..."
    }
  }
}
```

There's other stuff in there too (e.g., [Open Graph properties](http://ogp.me/)), but this is what you need to reconstruct the page itself.  It has a few nice features:

1. The head and body are well formed; they are actually serialized from the DOM, not related to the HTTP response.
2. All embedded resources (mostly images) are identified in the `resources` mapping.  The URLs in the page itself are replaced with those UUIDs, so you can put them back with a simple string substitutions, or you can rewrite the links easily.
3. Actual links (`<a href>`) should all be absolute.
4. It will *try* to tell you if the page is private (though it's just a heuristic).
5. If you want, it'll include a screenshot of the full page as a `data:` URL (use `&thumbnailWidth=px` to choose how wide).
6. CSS will be inlined in a `<style>` tag, perhaps reducing the complexity of the page for you.

Notably scripts and hidden elements will *not* be included (because PageShot was written to share visible content and not to scrape content).

Anyway, fun to realize the tool can address some hidden and unintentional use cases.
