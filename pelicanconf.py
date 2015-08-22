#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'peeomid'
SITENAME = 'Thoughts'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Saigon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sahaja Yoga', 'http://www.sahajayoga.org/'),
        ('Blog', '/blog'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/luantn'),
          ('github', 'https://github.com/peeomid'),
          ('google', 'https://plus.google.com/+LuanNguyenPeeomid'),
          ('rss', 'http://blog.peeomid.com/feeds/all.atom.xml'))


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Flex'
#THEME = 'themes/twenty-pelican-html5up'


#Theme config
SITETITLE = u'@peeomid'
SITESUBTITLE = 'Sahaja Yogi<br>Product Tech Lead <a href="http://rainmaker-labs.com">@rainmakerlabssg</a>'
#SITELOGO = ''
SITEDESCRIPTION = '@peeomid thoughts - Product Tech Lead @rainmakerlabs'
ROBOTS = u'index, follow'
#DISQUS_SITENAME
#GOOGLE_ANALYTICS
#GOOGLE_TAG_MANAGER

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),)

DEFAULT_CATEGORY = 'nonsense'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

# we need to change the main index page now though...
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAGS_URL = 'blog/tag/'
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

PLUGINS=['extended_sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}