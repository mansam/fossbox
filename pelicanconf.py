#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'FOSS@RIT'
SITENAME = u'foss@rit'
SITEURL = 'http://mansam.github.io/fossbox'
PLUGINS = ["plugins.libravatar"]
PATH = 'content'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
PROFILE_IMG_URL = "http://foss.rit.edu/files/logo.png"

# Github Activity Feed to display
GITHUB_ACTIVITY_FEED = 'https://github.com/fossrit.atom'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/fossrit'),
    ('twitter-square', 'https://twitter.com/fossrit'),
)

AUTHOR_EMAILS = {
	"decause": "decause@gmail.com"
}
DEFAULT_PAGINATION = 10
THEME = "themes/foss"
DISQUS_SITENAME = "fossritedu"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
