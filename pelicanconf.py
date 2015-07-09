#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hippo'
SITENAME = u'badrihippo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Thekambattu Pictures', 'http://thekambattupics.tk/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/badrihippo'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'

OUTPUT_PATH = '../master/'

STATIC_PATHS = ['images']

# Theme-specific settings (for pelican-alchemy)

EXTRA_FAVICON = True
PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
SHOW_ARTICLE_AUTHOR = False
GITHUB_ADDRESS = 'https://github.com/badrihippo'
PROFILE_IMAGE = '//i.imgur.com/NOZOY.gif'
SITE_SUBTEXT = 'programming and more'
SO_ADDRESS = 'http://stackoverflow.com/users/1196444/hippo'
