Title: A Product Journal: CSS Object Model
Slug: product-journal-css-object-model
Category: mozilla
Tags: product-journal
Date: 2015-12-29

> I'm blogging about the development of a new product in Mozilla, [look here for my other posts in this series](http://www.ianbicking.org/tag/product-journal.html)

And now for something entirely technical!

We've had a contributor from [Outernet](https://outernet.is/) exploring ways of using PageShot for capturing pages for distribution on their network.  Outernet satellite-based content distribution network.  It's a neat idea, but one challenge is that it's *very* one-way – anyone (given the equipment) can listen in to what the satellites broadcast, but that's it (at least for the most interesting use cases).  Lots of modern websites aren't setup well for that, so acquiring content can be tricky.

Given that interest I started thinking more about inlining resources.  We've been hotlinking to resources simply out of laziness.  Some things are easy to handle, but CSS is a bit more annoying because of the indirection of `@import` and yet more relatively URLs.  Until I started poking around I had no idea that there is a [CSS Object Model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model)!

Given this there is now experimental support for inlining all CSS rules into the captured page in PageShot.  The support is still incomplete, and my understanding of everything you can do with CSS is still incomplete.  But the code isn't very hard.  One fun thing is that we can test each CSS rule against the page and see if it is needed.  Doing this typically allows 80% of rules to be omitted.

Some highlights of what I've learned so far:

There's two interesting objects: [CSSStylesheet](https://developer.mozilla.org/en-US/docs/Web/API/CSSStylesheet) (which inherits from [Stylesheet](https://developer.mozilla.org/en-US/docs/Web/API/Stylesheet)) and [CSSRule](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule).  

`document.styleSheets`: a list of all stylesheets, both remote (`<link>`), inline, and imported (`@import`) stylesheets.

`styleSheet.href`: the URL of the stylesheet (`null` if it was inline).

`styleSheet.cssRules`: a list of all the rules in the stylesheet.  

`cssRule.type`: there's [several types of rules](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule#Type_constants).  I've chosen to ignore everything but `STYLE_RULE` and `MEDIA_RULE` out of laziness.

`cssRule.cssRules`: [media rules](https://developer.mozilla.org/en-US/docs/Web/CSS/@media) (like `@media (max-width: 600px) {.nav {display: none}}`) contain sub-rules (`.nav {display: none}` in this case).

`cssRule.parentRule`: points back to a media rule if there is one.

`cssRule.parentStyleSheet`: points back to the parent stylesheet.  There are probably ways of nesting media rules and stylesheets (that can have `media` attributes) in ways to create compound media rules that I haven't accounted for.

`cssRule.cssText`: the text of the rule.  This includes both selectors and style, or media queries and all the sub-rules.  I just split on `{` to separate the selector or query.  I *assume* these are representations of the parsed CSS, and so normalized, but I haven't explored that in detail.

There's all sorts of ways to create trees of media restrictions and other complexities that I know I haven't taken account of, but things Mostly Work Anyway.

Here's an example that makes use of this to create a single inline stylesheet for a page containing only necessary rules (using ES6):

```javascript
let allRules = [];

// CSS rules, some of which may be media queries, form a kind of tree; this gets
// this puts all the style rules in a flat list
function addRules(sheet) {
  for (let rule of sheet.cssRules) {
    if (rule.type == rule.MEDIA_RULE) {
      addRules(rule);
    } else if (rule.type == rule.STYLE_RULE) {
      allRules.push(rule);
    }
  }
}

// Then we traverse all the stylesheets and grab rules from each:
for (let styleSheet of document.styleSheets) {
  if (styleSheet.media.length && styleSheet.media.indexOf("*") == -1 && styleSheet.media.indexOf("screen") == -1) {
    // This is a stylesheet for some media besides screen
    continue;
  }
  addRules(styleSheet);
}

// Then we collect the rules up again, clustered by media queries (with
// rulesByMedia[""] for no media query)
let rulesByMedia = {};

for (let rule of allRules) {
  let selector = rule.split("{")[0].trim();
  if (! document.querySelector(selector)) {
    // Skip selectors that don't match anything
    continue;
  }
  let mediaType = "";
  if (rule.parentRule && rule.parentRule.type == rule.MEDIA_RULE) {
    mediaType = rule.parentRule.cssText.split("{")[0].trim();
  }
  rulesByMedia[mediaType] = rulesByMedia[mediaType] || [];
  rulesByMedia.push(rule);
}

// Now we can create a new clean stylesheet:
let lines = [];
for (let mediaType in rulesByMedia) {
  if (mediaType) {
    lines.push(mediaType + " {");
  }
  for (let rule of rulesByMedia[mediaType]) {
    let padding = mediaType ? "  " : "";
    lines.push(padding + rule.cssText);
  }
  if (mediaType) {
    lines.push("}");
  }
}

let style = "<style>" + lines.join("\n") + "</style>";
```

Obviously there could be rules that apply to DOM elements that aren't present *right now* but could be created.  And I'm sure it's omitting fonts and animations.  But it's fun to hack around with.

It might be fun to use this hooked up to [mutation observers](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) during your testing and find orphaned rules.
