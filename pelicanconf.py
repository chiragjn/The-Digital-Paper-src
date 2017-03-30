#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chirag Jain'
SITENAME = u'The Digital Paper'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/perec-mod"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['coming_soon']
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

SOCIAL = (('github', 'https://github.com/chiragjn/'),
		  ('at', 'mailto:jain.chirag925@gmail.com'),
          ('facebook','https://www.facebook.com/chiragjn101'),
          ('twitter', 'http://www.twitter.com/chiragjn101'),
          ('stack-overflow','http://stackoverflow.com/users/3697191/chiragjn'),
          ('linkedin','http://linkedin.com/in/chiragjn'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
TAGLINE="Technology and Thoughts"
STATIC_PATHS = ['images']
# Other Stuff
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = "General"
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 10