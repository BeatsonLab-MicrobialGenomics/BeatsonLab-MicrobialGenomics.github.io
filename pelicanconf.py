#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Mitchell Stanton-Cook'
SITENAME = u'Beatson Lab'
SITEURL = ''

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('GitHub', 'https://github.com/organizations/BeatsonLab-MicrobialGenomics'),
        ('SCMB@UQ', 'http://staff.scmb.uq.edu.au/staff/scott-beatson'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = os.path.expanduser("~/3rd-repos/pelican-themes/chunk")
SITESUBTITLE = 'Microbial Genomics Laboratory'
FOOTER_TEXT = '(c) 2013 Beatson Microbial Genomics Laboratory'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

GITHUB_URL = 'http://github.com/BeatsonLab-MicrobialGenomics'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
