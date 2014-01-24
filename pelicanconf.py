from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'

SITENAME = u'Leonardo Uieda'
SITESUBTITLE = u'Geophysics, inverse problems, science, and software'
SITEURL = ''

# Language and time
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'

# This goes at the footer of the site
COPYRIGHT_NOTICE = """
<a rel="license"
 href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
><img alt="Creative Commons License" style="border-width:0"
 src="http://i.creativecommons.org/l/by/4.0/88x31.png"
/></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
>Creative Commons Attribution 4.0 International License</a>.
"""

# Where to put generated files
ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

STATIC_PATHS = ['images', 'notebooks']

ARTICLES_FRONT_PAGE = 3
DEFAULT_PAGINATION = 0
DISPLAY_CATEGORIES_ON_MENU = False

# Feeds
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = False

THEME = 'theme/uieda'

# Top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('about', '/about.html'),
    ('github', 'https://github.com/leouieda'),
    ('twitter', 'https://twitter.com/leouieda'),
    ('google+', 'https://plus.google.com/+LeonardoUieda'),
    ('linkedin', 'http://www.linkedin.com/in/uieda'),
    ('figshare', 'http://figshare.com/authors/Leonardo%20Uieda/97471'),
    ('orcid', 'http://orcid.org/0000-0001-6123-9515'),
    ('rss', '/rss.xml'),
]

PLUGIN_PATH = os.path.join(os.environ.get('HOME'), 'src/pelican-plugins')
# Include plugins by jakevdp. See the PR for examples
# (https://github.com/getpelican/pelican-plugins/pull/21)
PLUGINS = ['summary', 'liquid_tags.video', 'liquid_tags.include_code',
           'liquid_tags.notebook']

# This header file is automatically generated by the notebook plugin
# (copied shamelessly from
# https://github.com/jakevdp/PythonicPerambulations/blob/master/pelicanconf.py)
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    with open('_nb_header.html') as f:
        EXTRA_HEADER = f.read().decode('utf-8')



