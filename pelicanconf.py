from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'

SITENAME = u"Leonardo Uieda"
SITESUBTITLE = u'Assistant Professor of Geophysics'
SITEKEYWORDS = u'geophysics, earth, earthscience, science, foss, scientific software'
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

STATIC_PATHS = ['images', 'notebooks', 'pdf']

# Blog articles display
ARTICLES_FRONT_PAGE = 3
SUMMARY_MAX_LENGTH = 25
DEFAULT_PAGINATION = 0
DISPLAY_CATEGORIES_ON_MENU = False

# Feeds
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = False

THEME = 'theme/uieda'

# Top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Home', '/'),
    ('About', '/about.html'),
    ('Blog', '/archives.html'),
    ('Research', '/research.html'),
    ('Publications', '/publications.html'),
    ('Talks', '/talks.html'),
    ('Software', '/software.html'),
    ('pinga-lab', 'https://github.com/pinga-lab'),
    ('<i class="fa fa-twitter fa-lg"></i>', 'https://twitter.com/leouieda'),
    ('<i class="fa fa-github fa-lg"></i>', 'https://github.com/leouieda'),
    ('<e class="fa fa-rss fa-lg"></i>', '/rss.xml'),
]

PLUGIN_PATH = '../pelican-plugins'
# Include plugins by jakevdp. See the PR for examples
# (https://github.com/getpelican/pelican-plugins/pull/21)
PLUGINS = ['summary',
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'better_figures_and_images',
           'html_rst_directive',
           'latex',
           ]
RESPONSIVE_IMAGES = False
FIGURE_NUMBERS = True

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



