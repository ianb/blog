#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

base = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "Ian Bicking"
SITENAME = "Ian Bicking: a blog"
SITEURL = "https://ianbicking.org"
# FEED_DOMAIN = "https://ianbicking.org"
CACHE_CONTENT = True
# ARCHIVES_SAVE_AS = 'test-archive.html'
PATH = os.path.join(base, "content")

if os.environ.get("OVERRIDE_SITEURL"):
    SITEURL = os.environ["OVERRIDE_SITEURL"]

TIMEZONE = "US/Central"
DATE_FORMATS = {
    "en": "%A, %d %B, %Y",
}
ARTICLE_EXCLUDES = ["pages", "old", "media"]
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
DIRECT_TEMPLATES = ("index", "tag", "category", "archives")
PAGINATED_TEMPLATES = {"index": None, "tag": None, "category": None, "author": None}
INDEX_SAVE_AS = "blog/index.html"
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_MAX_ITEMS = 20
RELATIVE_URLS = False
STATIC_PATHS = ["media"]
COVER_IMAGES_PATH = "media/cover-images"
TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"
WITH_FUTURE_DATES = False
def ARTICLE_ORDER_BY(article):
    return -article.date.timestamp()

def FORMAT_DATE(date):
    d = date.strftime("%A, %B ")
    day = str(date.day)
    if day[-1] == "1":
        day += "st"
    elif day[-1] == "2":
        day += "nd"
    elif day[-1] == "3":
        day += "rd"
    else:
        day += "th"
    d += day + date.strftime(", %Y")
    return d


COMMENTS = {}
for filename in os.listdir(os.path.join(base, "disqusoutput")):
    if not filename.endswith(".html"):
        continue
    content = open(os.path.join(base, "disqusoutput", filename), "r").read()
    article_id = filename.replace(".html", "")
    COMMENTS[article_id] = content

TYPOGRIFY = True

DEFAULT_LANG = "en-US"

# Blogroll
LINKS = ()

USE_FOLDER_AS_CATEGORY = False

# built-texts, cebong
# THEME = '/Users/ianbicking/src/blog.pelican/pelican-themes/built-texts'
THEME = "./mystyle/"

# Social widget
SOCIAL = (
    # ("Mastodon", "https://mastodon.technology/@ianbicking"),
    ("@ianbicking@hachyderm.io", "https://hachyderm.io/@ianbicking"),
    ("Blue Sky", "https://bsky.app/profile/ianbicking.org"),
    ("Threads", "https://www.threads.net/@ibicking"),
    ("Github", "https://github.com/ianb"),
    ("LinkedIn", "https://www.linkedin.com/in/ianbicking/"),
)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["./pelican-plugins"]

PLUGINS = ["github_activity", "related_posts", "assets", "pelican-cover-image"]

GITHUB_ACTIVITY_FEED = "https://github.com/ianb.atom"
GITHUB_ACTIVITY_MAX_ENTRIES = 10

# DISQUS_SITENAME = "ianbicking"
# This is the old ID (pre-2023):
# GOOGLE_ANALYTICS = "UA-2442258-1"
GOOGLE_ANALYTICS = "G-FKT4HDGBE4"

MENUITEMS = [
    # ("About", "/about.html"),
    ("blog", "/blog/"),
    ("projects", "/projects.html"),
]

WEBASSETS = True
DISPLAY_PAGES_ON_MENU = False
GETATTR = getattr

with open(os.path.join(base, "content/old/archive-fragment.html")) as fp:
    EXTRA_ARCHIVE = fp.read()

NEWEST_FIRST_ARCHIVES = True
CACHE_CONTENT = False
