#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

base = os.path.dirname(os.path.abspath(__file__))
AUTHOR = u'Ian Bicking'
SITENAME = u'Ian Bicking: a blog'
SITEURL = 'http://www.ianbicking.org'
#FEED_DOMAIN = "http://ianbicking.org"
CACHE_CONTENT = True
#ARCHIVES_SAVE_AS = 'test-archive.html'
PATH = os.path.join(base, "content")

import os
if os.environ.get("OVERRIDE_SITEURL"):
    SITEURL = os.environ["OVERRIDE_SITEURL"]

TIMEZONE = 'US/Central'
DATE_FORMATS = {
    "en": "%A, %d %B, %Y",
    }
ARTICLE_EXCLUDES = ["pages", "old", "media", "previous-content"]
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}.html"
PAGE_URL = "{slug.html}"
PAGE_SAVE_AS = "{slug}.html"
DIRECT_TEMPLATES = ('blog/index', 'tags', 'categories', 'archives')
PAGINATED_DIRECT_TEMPLATES = ['blog/index']
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
FEED_MAX_ITEMS = 20
RELATIVE_URLS = False
STATIC_PATHS = ["media"]
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',  # Default
    'extra',  # Default
    #'cite',  # Extra <cite> support
    ]


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

TYPOGRIFY = True

DEFAULT_LANG = u'en-US'

# Blogroll
LINKS = (
    )

USE_FOLDER_AS_CATEGORY = False

# built-texts, cebong
#THEME = '/Users/ianbicking/src/blog.pelican/pelican-themes/built-texts'
THEME = './mystyle/'

# Social widget
SOCIAL = (
    ('Google+', 'https://plus.google.com/+IanBicking/posts'),
    ('@ianbicking', 'https://twitter.com/ianbicking'),
    ('Github', 'https://github.com/ianb'),
    )

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']

PLUGINS = [
    'github_activity',
    'related_posts',
    'assets',
    ]

GITHUB_ACTIVITY_FEED = 'https://github.com/ianb.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10

DISQUS_SITENAME = "ianbicking"
GOOGLE_ANALYTICS = "UA-2442258-1"

MENUITEMS = [
    #("About", "/about.html"),
    ("blog", "/blog/"),
    ("projects", "/projects.html"),
    ]

WEBASSETS = True
DISPLAY_PAGES_ON_MENU = False
GETATTR = getattr

with open(os.path.join(base, "content/old/archive-fragment.html")) as fp:
    EXTRA_ARCHIVE = fp.read()
