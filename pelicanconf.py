#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fatih Sarigoz'
SITENAME = u'Fatih Sarigoz'
SITESUBTITLE = u'Data Science Blog'
SITEURL = ''  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
GITHUB_URL = 'http://github.com/fsarigoz'
TWITTER_USERNAME = '@fatihsarigoz'

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/fatihsarigoz'),
          ('linkedin', 'http://www.linkedin.com/in/fatihsarigoz'),
          ('github', 'https://github.com/fsarigoz'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------
THEME = u'flex'

# Alchemy specific settings
ICONS = (('twitter', 'https://twitter.com/fatihsarigoz'),
          ('linkedin', 'http://www.linkedin.com/in/fatihsarigoz'),
          ('github', 'https://github.com/fsarigoz'),)

PYGMENTS_STYLE = 'default'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Flex specific settings
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),)



