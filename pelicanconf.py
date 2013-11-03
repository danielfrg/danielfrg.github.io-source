# -*- coding: utf-8 -*- #

# SITEURL = ''
SITEURL = 'http://danielfrg.github.io'
AUTHOR = 'Daniel Rodriguez'
SITENAME = 'Daniel Rodriguez'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'
MARKUP = ('md', 'ipynb')
DEFAULT_DATE_FORMAT = '%d.%m.%Y'

PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'

THEME = "themes/middle/"
STATIC_PATHS = ["images"]

SITEMAP = {
    'format': 'xml'
}

PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'ipythonnb']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# paths inside `content`
STATIC_PATHS = ['images', 'favicon.ico', '404.html', 'robots.html']

# Theme settings
HOMEPAGE_INTRO = "This blog is written by Daniel Rodriguez. He writes about coding, python, data science and his projects"

TWITTER_USERNAME = "danielfrg"
GITHUB_USERNAME = "danielfrg"
EMAIL_ADDRESS = "df.rodriguez143@gmail.com"
SHOW_FEED = True

GOOGLE_ANALYTICS = 'UA-35523657-2'
DISQUS_USERNAME = 'danielfrg'
