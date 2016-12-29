#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcelo Ferselva'
SITENAME = 'REVAUT'
SITETITLE = 'RevAut'
SITESUBTITLE = 'REVolução AUTogestionária'

SITEPATH = '/revaut'
SITEURL = 'http://localhost:8000'

THEME = './flex-theme'
PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

LINKS = (('Wiki', 'http://wikiautogestionaria.com'),)

SOCIAL = (('github', 'https://github.com/marcfers'),
	  ('rss', SITEPATH + '/feeds/all.atom.xml'))

MENUITEMS = (('Arquivos', SITEPATH + '/archives.html'),
	     ('Categorias', SITEPATH + '/categories.html'),
	     ('Etiquetas', SITEPATH + '/tags.html'),)

CC_LICENSE = {
	'name': 'Creative Commons Attribution-NonCommercial-ShareAlike',
	'version': '4.0',
	'slug': 'by-nc-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10
