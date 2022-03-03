# -*- coding: utf-8 -*-

import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Vincent Davis"  # (translatable)
BLOG_TITLE = "Post Cards"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://postcards.vdavis.net/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://postcards.vdavis.net/"
BLOG_EMAIL = "vincent@vincentdavis.net"
BLOG_DESCRIPTION = "Knox, Chandler, Davis Families"  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en        English
# af        Afrikaans
# ar        Arabic
# az        Azerbaijani
# bg        Bulgarian
# bs        Bosnian
# ca        Catalan
# cs        Czech [ALTERNATIVELY cz]
# da        Danish
# de        German
# el        Greek [NOT gr]
# eo        Esperanto
# es        Spanish
# et        Estonian
# eu        Basque
# fa        Persian
# fi        Finnish
# fr        French
# fur       Friulian
# gl        Galician
# he        Hebrew
# hi        Hindi
# hr        Croatian
# hu        Hungarian
# ia        Interlingua
# id        Indonesian
# it        Italian
# ja        Japanese [NOT jp]
# ko        Korean
# lt        Lithuanian
# mi        Maori
# ml        Malayalam
# mr        Marathi
# nb        Norwegian (Bokmål)
# nl        Dutch
# oc        Occitan
# pa        Punjabi
# pl        Polish
# pt        Portuguese
# pt_br     Portuguese (Brazil)
# ru        Russian
# sk        Slovak
# sl        Slovene
# sq        Albanian
# sr        Serbian (Cyrillic)
# sr_latin  Serbian (Latin)
# sv        Swedish
# te        Telugu
# th        Thai
# tr        Turkish [NOT tr_TR]
# uk        Ukrainian
# ur        Urdu
# vi        Vietnamese
# zh_cn     Chinese (Simplified)
# zh_tw     Chinese (Traditional)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 4 theme,
#          may present issues if the menu is too large.
#          (in Bootstrap, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/archive.html", "Archives"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

# Name of the theme to use.
THEME = "bootblog4"

# A theme color. In default themes, it might be displayed by some browsers as
# the browser UI color (eg. Chrome on Android). Other themes might also use it
# as an accent color (the default ones don’t). Must be a HEX value.
THEME_COLOR = '#5670d4'

# Theme configuration. Fully theme-dependent. (translatable)
# Samples for bootblog4 (enabled) and bootstrap4 (commented) follow.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
#                      navbar_custom_bg (defaults to '')

# Config for bootblog4:
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}
# Config for bootstrap4:
# THEME_CONFIG = {
#     DEFAULT_LANG: {
#         # Use a light navbar with dark text. Defaults to False.
#         'navbar_light': False,
#         # Use a custom navbar color. If unset, 'navbar_light' sets text +
#         # background color. If set, navbar_light controls only background
#         # color. Supported values: bg-dark, bg-light, bg-primary, bg-secondary,
#         # bg-success, bg-danger, bg-warning, bg-info, bg-white, bg-transparent.
#         'navbar_custom_bg': '',
#     }
# }

# POSTS and PAGES contains (wildcard, destination, template) tuples.
# (translatable)
#
# The wildcard is used to generate a list of source files
# (whatever/thing.rst, for example).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.rst and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output/TRANSLATIONS[lang]/destination/pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
# The page might also be placed in /destination/pagename/index.html
# if PRETTY_URLS are enabled.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds, indexes, tag lists and archives and are considered part
# of a blog, while PAGES are just independent HTML pages.
#
# Finally, note that destination can be translated, i.e. you can
# specify a different translation folder per language. Example:
#     PAGES = (
#         ("pages/*.rst", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#         ("pages/*.md", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#     )

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)

PAGES = (
    ("pages/*.rst", "pages", "page.tmpl"),
    ("pages/*.txt", "pages", "page.tmpl"),
    ("pages/*.md", "pages", "page.tmpl"),
    ("pages/*.html", "pages", "page.tmpl"),
)



# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "UTC"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates. (translatable)
# Used by babel.dates, CLDR style: http://cldr.unicode.org/translation/date-time-1/date-time
# You can also use 'full', 'long', 'medium', or 'short'
# DATE_FORMAT = 'yyyy-MM-dd HH:mm'

# Date format used to display post dates, if local dates are used. (translatable)
# Used by Luxon: https://moment.github.io/luxon/docs/manual/formatting
# Example for presets: {'preset': True, 'format': 'DATE_FULL'}
# LUXON_DATE_FORMAT = {
#     DEFAULT_LANG: {'preset': False, 'format': 'yyyy-MM-dd HH:mm'},
# }

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE (without JS)
# 1 = using LUXON_DATE_FORMAT and local user time (JS, using Luxon)
# 2 = using a string like “2 days ago” (JS, using Luxon)
#
# Your theme must support it, Bootstrap already does.
# DATE_FANCINESS = 0

# Customize the locale/region used for a language.
# For example, to use British instead of US English: LOCALES = {'en': 'en_GB'}
# LOCALES = {}

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# The default compiler for `new_post` is the first entry in the POSTS tuple.
#
# 'rest' is reStructuredText
# 'markdown' is Markdown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
    "rest": ['.txt', '.rst'],
    "markdown": ['.md', '.mdown', '.markdown'],
    "html": ['.html', '.htm'],
}

# Enable reST directives that insert the contents of external files such
# as "include" and "raw." This maps directly to the docutils file_insertion_enabled
# config. See: https://docutils.sourceforge.io/docs/user/config.html#file-insertion-enabled
# REST_FILE_INSERTION_ENABLED = True

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Preferred metadata format for new posts
# "Nikola": reST comments, wrapped in a HTML comment if needed (default)
# "YAML": YAML wrapped in "---"
# "TOML": TOML wrapped in "+++"
# "Pelican": Native markdown metadata or reST docinfo fields. Nikola style for other formats.
# METADATA_FORMAT = "Nikola"

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
# NEW_POST_DATE_PATH = False

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.
# NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''

# When linking posts to social media, Nikola provides Open Graph metadata
# which is used to show a nice preview. This includes an image preview
# taken from the post's previewimage metadata field.
# This option lets you use an image to be used if the post doesn't have it.
# The default is None, valid values are URLs or output paths like
# "/images/foo.jpg"
# DEFAULT_PREVIEW_IMAGE = None

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# Note: if your logo is a SVG image, and you set SHOW_BLOG_TITLE = False,
# you should explicitly set a height for #logo in CSS.
# SHOW_BLOG_TITLE = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag RSS_EXTENSION (RSS feed for a tag)
# (translatable)
# TAG_PATH = "categories"

# By default, the list of tags is stored in
#     output / TRANSLATION[lang] / TAG_PATH / index.html
# (see explanation for TAG_PATH). This location can be changed to
#     output / TRANSLATION[lang] / TAGS_INDEX_PATH
# with an arbitrary relative path TAGS_INDEX_PATH.
# (translatable)
# TAGS_INDEX_PATH = "tags.html"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# (translatable)
# TAG_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# (translatable)
# TAG_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ['mathjax']

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# A list of dictionaries specifying tags which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# For example:
#   [
#     {'en': 'private', 'de': 'Privat'},
#     {'en': 'work', 'fr': 'travail', 'de': 'Arbeit'},
#   ]
# TAG_TRANSLATIONS = []

# If set to True, a tag in a language will be treated as a translation
# of the literally same tag in all other languages. Enable this if you
# do not translate tags, for example.
# TAG_TRANSLATIONS_ADD_DEFAULTS = True

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category RSS_EXTENSION (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# By default, the list of categories is stored in
#     output / TRANSLATION[lang] / CATEGORY_PATH / index.html
# (see explanation for CATEGORY_PATH). This location can be changed to
#     output / TRANSLATION[lang] / CATEGORIES_INDEX_PATH
# with an arbitrary relative path CATEGORIES_INDEX_PATH.
# (translatable)
# CATEGORIES_INDEX_PATH = "categories.html"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# (translatable)
# CATEGORY_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# (translatable)
# CATEGORY_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# A list of dictionaries specifying categories which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# See TAG_TRANSLATIONS example above.
# CATEGORY_TRANSLATIONS = []

# If set to True, a category in a language will be treated as a translation
# of the literally same category in all other languages. Enable this if you
# do not translate categories, for example.
# CATEGORY_TRANSLATIONS_ADD_DEFAULTS = True

# If no category is specified in a post, the destination path of the post
# can be used in its place. This replaces the sections feature. Using
# category hierarchies is recommended.
# CATEGORY_DESTPATH_AS_DEFAULT = False

# If True, the prefix will be trimmed from the category name, eg. if the
# POSTS destination is "foo/bar", and the path is "foo/bar/baz/quux",
# the category will be "baz/quux" (or "baz" if only the first directory is considered).
# Note that prefixes coming from translations are always ignored.
# CATEGORY_DESTPATH_TRIM_PREFIX = False

# If True, only the first directory of a path will be used.
# CATEGORY_DESTPATH_FIRST_DIRECTORY_ONLY = True

# Map paths to prettier category names. (translatable)
# CATEGORY_DESTPATH_NAMES = {
#    DEFAULT_LANG: {
#        'webdev': 'Web Development',
#        'webdev/django': 'Web Development/Django',
#        'random': 'Odds and Ends',
#    },
# }

# By default, category indexes will appear in CATEGORY_PATH and use
# CATEGORY_PREFIX. If this is enabled, those settings will be ignored (except
# for the index) and instead, they will follow destination paths (eg. category
# 'foo' might appear in 'posts/foo'). If the category does not come from a
# destpath, first entry in POSTS followed by the category name will be used.
# For this setting, category hierarchies are required and cannot be flattened.
# CATEGORY_PAGES_FOLLOW_DESTPATH = False

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Path to author pages. Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of authors)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts by an author)
# output / TRANSLATION[lang] / AUTHOR_PATH / author RSS_EXTENSION (RSS feed for an author)
# (translatable)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page.
# Author pages and links to them will still be generated.
HIDDEN_AUTHORS = ['Guest']

# Allow multiple, comma-separated authors for a post? (Requires theme support, present in built-in themes)
# MULTIPLE_AUTHORS_PER_POST = False

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
# INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Create previous, up, next navigation links for archives
# CREATE_ARCHIVE_NAVIGATION = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# (translatable)
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Extension for RSS feed files
# RSS_EXTENSION = ".xml"

# RSS filename base (without extension); used for indexes and galleries.
# (translatable)
# RSS_FILENAME_BASE = "rss"

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / RSS_FILENAME_BASE RSS_EXTENSION
# (translatable)
# RSS_PATH = ""

# Final location for the blog main Atom feed is:
# output / TRANSLATION[lang] / ATOM_PATH / ATOM_FILENAME_BASE ATOM_EXTENSION
# (translatable)
# ATOM_PATH = ""

# Atom filename base (without extension); used for indexes.
# (translatable)
ATOM_FILENAME_BASE = "feed"

# Extension for Atom feed files
# ATOM_EXTENSION = ".atom"

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["1886/04/02/from-david-knox-to-jeanette-annie-and-g-r-knox/index.html", "/posts/1886/04/02/from-david-knox-to-jeanette-annie-and-g-r-knox.html"], ["1885/12/06/from-to-jeanette-knox-chandler/index.html", "/posts/1885/12/06/from-to-jeanette-knox-chandler.html"], ["about/index.html", "/pages/about.html"], ["1886/01/26/from-ruth-to-jeanette-knox-chandler/index.html", "/posts/1886/01/26/from-ruth-to-jeanette-knox-chandler.html"], ["1886/02/04/from-will-to-jeanette-knox-chandler/index.html", "/posts/1886/02/04/from-will-to-jeanette-knox-chandler.html"], ["1885/08/31/from-linnie-samuels-to-jeanette-knox-chandler-2/index.html", "/posts/1885/08/31/from-linnie-samuels-to-jeanette-knox-chandler-2.html"], ["1885/12/06/from-izora-h-to-jeanette-knox-chandler/index.html", "/posts/1885/12/06/from-izora-h-to-jeanette-knox-chandler.html"], ["1886/03/04/from-william-knox-to-jeanette-knox-chandler/index.html", "/posts/1886/03/04/from-william-knox-to-jeanette-knox-chandler.html"], ["1885/11/17/from-j-saul-and-elijah-h-chandler-to-unknown-chandler/index.html", "/posts/1885/11/17/from-j-saul-and-elijah-h-chandler-to-unknown-chandler.html"], ["1886/03/22/from-groover-c-hoover-to-jeanette-knox-chandler/index.html", "/posts/1886/03/22/from-groover-c-hoover-to-jeanette-knox-chandler.html"], ["1885/04/10/form-william-thomas-knox-to-anna-roush/index.html", "/posts/1885/04/10/form-william-thomas-knox-to-anna-roush.html"], ["1884/06/01/from-katie-c-to-jeanette-knox-chandler/index.html", "/posts/1884/06/01/from-katie-c-to-jeanette-knox-chandler.html"], ["1885/12/24/from-maggie-knox-to-jeanette-knox-chandler/index.html", "/posts/1885/12/24/from-maggie-knox-to-jeanette-knox-chandler.html"], ["1886/03/11/from-john-knox-to-jeanette-knox-chandler/index.html", "/posts/1886/03/11/from-john-knox-to-jeanette-knox-chandler.html"], ["1886/03/12/from-john-chandler-to-jeanette-knox-chandler/index.html", "/posts/1886/03/12/from-john-chandler-to-jeanette-knox-chandler.html"], ["1885/12/23/from-maggie-knox-to-jeanette-knox-chandler-2/index.html", "/posts/1885/12/23/from-maggie-knox-to-jeanette-knox-chandler-2.html"], ["1884/10/28/from-kate-g-to-jeanette-knox-chandler/index.html", "/posts/1884/10/28/from-kate-g-to-jeanette-knox-chandler.html"], ["1886/03/04/from-knox-to-jeanette-knox-chandler-2/index.html", "/posts/1886/03/04/from-knox-to-jeanette-knox-chandler-2.html"], ["1886/03/23/from-maggie-knox-to-jeanette-knox-chandler-3/index.html", "/posts/1886/03/23/from-maggie-knox-to-jeanette-knox-chandler-3.html"], ["1884/08/10/from-katie-cumoy-to-jeanette-knox-chandler/index.html", "/posts/1884/08/10/from-katie-cumoy-to-jeanette-knox-chandler.html"], ["1886/11/03/from-elijah-h-chandler-to-jeanette-knox/index.html", "/posts/1886/11/03/from-elijah-h-chandler-to-jeanette-knox.html"], ["1886/06/06/from-joe-d-knox-to-jeanette-knox-chandler/index.html", "/posts/1886/06/06/from-joe-d-knox-to-jeanette-knox-chandler.html"], ["1886/10/04/from-linnie-samuels-to-jeanette-chandler-knox/index.html", "/posts/1886/10/04/from-linnie-samuels-to-jeanette-chandler-knox.html"], ["1886/10/13/from-elijah-h-chandler-to-jeanette-knox-chandler-3/index.html", "/posts/1886/10/13/from-elijah-h-chandler-to-jeanette-knox-chandler-3.html"], ["1886/04/08/from-mary-to-jeanette-knox-chandler/index.html", "/posts/1886/04/08/from-mary-to-jeanette-knox-chandler.html"], ["1886/10/20/from-elijah-h-chandler-to-jeanette-knox-chandler-6/index.html", "/posts/1886/10/20/from-elijah-h-chandler-to-jeanette-knox-chandler-6.html"], ["1886/06/08/from-will-to-jeanette-knox-chandler-2/index.html", "/posts/1886/06/08/from-will-to-jeanette-knox-chandler-2.html"], ["1886/10/24/from-elijah-h-dave-and-j-saul-chandler-to-unknown-chandler/index.html", "/posts/1886/10/24/from-elijah-h-dave-and-j-saul-chandler-to-unknown-chandler.html"], ["1886/05/12/from-elijah-h-ad-j-saul-chandler-to-unknown-chandler/index.html", "/posts/1886/05/12/from-elijah-h-ad-j-saul-chandler-to-unknown-chandler.html"], ["1886/08/10/from-linnie-samuels-to-jeanette-knox-chandler-3/index.html", "/posts/1886/08/10/from-linnie-samuels-to-jeanette-knox-chandler-3.html"], ["1886/06/02/from-lizzie-j-to-jeanette-knox-chandler/index.html", "/posts/1886/06/02/from-lizzie-j-to-jeanette-knox-chandler.html"], ["1886/11/03/from-elijah-h-chandler-to-jeanette-knox-chandler-11/index.html", "/posts/1886/11/03/from-elijah-h-chandler-to-jeanette-knox-chandler-11.html"], ["1886/09/25/from-elijah-h-chandler-to-jeanette-knox-chandler-12/index.html", "/posts/1886/09/25/from-elijah-h-chandler-to-jeanette-knox-chandler-12.html"], ["1886/07/02/from-d-knox-to-jeanette-knox-chandler-and-family/index.html", "/posts/1886/07/02/from-d-knox-to-jeanette-knox-chandler-and-family.html"], ["1886/10/18/from-jeanette-knox-chandler-to-elijah-h-chandler-5/index.html", "/posts/1886/10/18/from-jeanette-knox-chandler-to-elijah-h-chandler-5.html"], ["1886/06/15/from-w-l-fulmer-to-jeanette-knox-chandler/index.html", "/posts/1886/06/15/from-w-l-fulmer-to-jeanette-knox-chandler.html"], ["1886/10/21/from-elijah-h-chandler-to-jeanette-knox-chandler-14/index.html", "/posts/1886/10/21/from-elijah-h-chandler-to-jeanette-knox-chandler-14.html"], ["1886/05/21/from-maggie-knox-to-jeanette-knox-chandler-4/index.html", "/posts/1886/05/21/from-maggie-knox-to-jeanette-knox-chandler-4.html"], ["1886/09/02/from-lizzie-to-jeanette-knox-chandler/index.html", "/posts/1886/09/02/from-lizzie-to-jeanette-knox-chandler.html"], ["1886/05/30/from-maggie-knox-to-jeanette-knox-chandler-5/index.html", "/posts/1886/05/30/from-maggie-knox-to-jeanette-knox-chandler-5.html"], ["1887/02/04/to-nettie-from-elijah-h-chandler/index.html", "/posts/1887/02/04/to-nettie-from-elijah-h-chandler.html"], ["1887/07/24/from-elijah-h-chandler-to-jeanette-knox-2/index.html", "/posts/1887/07/24/from-elijah-h-chandler-to-jeanette-knox-2.html"], ["1886/12/29/from-elijah-h-chandler-to-jeanette-knox-chandler/index.html", "/posts/1886/12/29/from-elijah-h-chandler-to-jeanette-knox-chandler.html"], ["1887/06/06/from-elijah-h-chandler-to-jeanette-knox-chandler-2/index.html", "/posts/1887/06/06/from-elijah-h-chandler-to-jeanette-knox-chandler-2.html"], ["1886/11/22/from-linnie-samuels-to-jeanette-knox-chandler/index.html", "/posts/1886/11/22/from-linnie-samuels-to-jeanette-knox-chandler.html"], ["1886/11/09/from-elijah-h-chandler-to-jeanette-knox-chandler-4/index.html", "/posts/1886/11/09/from-elijah-h-chandler-to-jeanette-knox-chandler-4.html"], ["1887/05/24/from-f-m-grimes-to-elijah-h-chandler/index.html", "/posts/1887/05/24/from-f-m-grimes-to-elijah-h-chandler.html"], ["1887/12/21/from-unknown-to-jeanette-knox-chandler/index.html", "/posts/1887/12/21/from-unknown-to-jeanette-knox-chandler.html"], ["1886/12/29/from-elijah-h-chandler-to-jeanette-knox-chandler-5/index.html", "/posts/1886/12/29/from-elijah-h-chandler-to-jeanette-knox-chandler-5.html"], ["1887/01/15/from-elijah-h-chandler-to-jeanette-knox-chandler-8/index.html", "/posts/1887/01/15/from-elijah-h-chandler-to-jeanette-knox-chandler-8.html"], ["1887/02/01/from-jeanette-knox-chandler-to-elijah-h-chandler/index.html", "/posts/1887/02/01/from-jeanette-knox-chandler-to-elijah-h-chandler.html"], ["1887/01/12/from-jeanette-knox-chandler-to-elijah-h-chandler-3/index.html", "/posts/1887/01/12/from-jeanette-knox-chandler-to-elijah-h-chandler-3.html"], ["1887/01/09/from-jeanette-knox-chandler-to-elijah-h-chandler-2/index.html", "/posts/1887/01/09/from-jeanette-knox-chandler-to-elijah-h-chandler-2.html"], ["1886/12/28/from-jeanette-knox-chandler-to-elijah-h-chandler-4/index.html", "/posts/1886/12/28/from-jeanette-knox-chandler-to-elijah-h-chandler-4.html"], ["1886/11/07/from-william-knox-to-jeanette-knox-chandler-2/index.html", "/posts/1886/11/07/from-william-knox-to-jeanette-knox-chandler-2.html"], ["1886/12/04/from-elijah-h-chandler-to-jeanette-knox-chandler-10/index.html", "/posts/1886/12/04/from-elijah-h-chandler-to-jeanette-knox-chandler-10.html"], ["1892/03/06/from-elijah-h-chandler-to-jeanette-knox-chandler-13/index.html", "/posts/1892/03/06/from-elijah-h-chandler-to-jeanette-knox-chandler-13.html"], ["1886/11/11/from-jeanette-knox-chandler-to-elijah-h-chandler-6/index.html", "/posts/1886/11/11/from-jeanette-knox-chandler-to-elijah-h-chandler-6.html"], ["1886/11/11/from-elijah-h-chandler-to-jeanette-knox-chandler-15/index.html", "/posts/1886/11/11/from-elijah-h-chandler-to-jeanette-knox-chandler-15.html"], ["1887/01/19/from-elijah-h-chandler-to-jeanette-knox-chandler-16/index.html", "/posts/1887/01/19/from-elijah-h-chandler-to-jeanette-knox-chandler-16.html"], ["1900/01/01/from-r-to-bess-chandler/index.html", "/posts/1900/01/01/from-r-to-bess-chandler.html"], ["1900/01/01/from-unknown-to-martin-chandler/index.html", "/posts/1900/01/01/from-unknown-to-martin-chandler.html"], ["1900/01/01/from-aunt-sarah-and-uncle-to-bess-and-ruby-chandler/index.html", "/posts/1900/01/01/from-aunt-sarah-and-uncle-to-bess-and-ruby-chandler.html"], ["1900/01/01/from-unknown-to-martin-chandler-2/index.html", "/posts/1900/01/01/from-unknown-to-martin-chandler-2.html"], ["1900/01/01/1077/index.html", "/posts/1900/01/01/1077.html"], ["1900/01/01/from-ruby-chandler-to-margaret-chandler-2/index.html", "/posts/1900/01/01/from-ruby-chandler-to-margaret-chandler-2.html"], ["1900/01/01/from-unknown-to-bess-chandler-10/index.html", "/posts/1900/01/01/from-unknown-to-bess-chandler-10.html"], ["1900/01/01/from-ruby-chandler-to-pearl-ellis/index.html", "/posts/1900/01/01/from-ruby-chandler-to-pearl-ellis.html"], ["1900/01/01/from-maud-g-to-bess-chandler/index.html", "/posts/1900/01/01/from-maud-g-to-bess-chandler.html"], ["1900/01/01/from-johnie-to-lucerne-chandler/index.html", "/posts/1900/01/01/from-johnie-to-lucerne-chandler.html"], ["1900/01/01/from-unknown-to-ruby-chandler-10/index.html", "/posts/1900/01/01/from-unknown-to-ruby-chandler-10.html"], ["1900/01/01/from-doss-bryant-to-grace-chandler/index.html", "/posts/1900/01/01/from-doss-bryant-to-grace-chandler.html"], ["1900/01/01/from-ruby-chandler-to-grace-chandler-2/index.html", "/posts/1900/01/01/from-ruby-chandler-to-grace-chandler-2.html"], ["1900/01/01/from-ruby-chandler-to-jeanette-knox-chandler-3/index.html", "/posts/1900/01/01/from-ruby-chandler-to-jeanette-knox-chandler-3.html"], ["1900/01/01/from-q-to-jas-e-heauner/index.html", "/posts/1900/01/01/from-q-to-jas-e-heauner.html"], ["1900/01/01/from-fern-gray-to-miss-chandler/index.html", "/posts/1900/01/01/from-fern-gray-to-miss-chandler.html"], ["1900/01/01/from-coston-to-grace-chandler/index.html", "/posts/1900/01/01/from-coston-to-grace-chandler.html"], ["1900/01/01/from-bess-chandler-to-elijah-h-chandler-and-family/index.html", "/posts/1900/01/01/from-bess-chandler-to-elijah-h-chandler-and-family.html"], ["1900/01/01/2673/index.html", "/posts/1900/01/01/2673.html"], ["1900/01/01/from-betty-ann-tilley-to-amelia-j-wiggins/index.html", "/posts/1900/01/01/from-betty-ann-tilley-to-amelia-j-wiggins.html"], ["1900/01/01/from-bessie-chandler-to-marie/index.html", "/posts/1900/01/01/from-bessie-chandler-to-marie.html"], ["1900/01/03/from-unknown-to-bess-chandler-2/index.html", "/posts/1900/01/03/from-unknown-to-bess-chandler-2.html"], ["1900/01/01/from-unknown-to-jack-d-krithdey/index.html", "/posts/1900/01/01/from-unknown-to-jack-d-krithdey.html"], ["1900/01/01/from-coston-climmons-to-ruby-chandler/index.html", "/posts/1900/01/01/from-coston-climmons-to-ruby-chandler.html"], ["1900/01/01/from-unknown-to-martin/index.html", "/posts/1900/01/01/from-unknown-to-martin.html"], ["1900/01/01/from-bertha-to-nellie/index.html", "/posts/1900/01/01/from-bertha-to-nellie.html"], ["1900/01/01/from-david-knox-to-annie/index.html", "/posts/1900/01/01/from-david-knox-to-annie.html"], ["1900/01/01/from-pike-county-republican-to-martin-chandler/index.html", "/posts/1900/01/01/from-pike-county-republican-to-martin-chandler.html"], ["1900/01/01/from-unknown-to-bess-chandler-12/index.html", "/posts/1900/01/01/from-unknown-to-bess-chandler-12.html"], ["1900/01/01/from-grace-chandler-to-g-r-roush/index.html", "/posts/1900/01/01/from-grace-chandler-to-g-r-roush.html"], ["1900/01/01/from-chas-to-bess-chandler/index.html", "/posts/1900/01/01/from-chas-to-bess-chandler.html"], ["1900/01/01/from-gus-to-grace-chandler/index.html", "/posts/1900/01/01/from-gus-to-grace-chandler.html"], ["1900/01/01/from-unknown-to-art-f-cole/index.html", "/posts/1900/01/01/from-unknown-to-art-f-cole.html"], ["1900/01/01/from-jesse-to-margaret/index.html", "/posts/1900/01/01/from-jesse-to-margaret.html"], ["1900/01/01/from-ruby-chandler-to-manca/index.html", "/posts/1900/01/01/from-ruby-chandler-to-manca.html"], ["1900/01/01/from-martin-chandler-to-unknown/index.html", "/posts/1900/01/01/from-martin-chandler-to-unknown.html"], ["1900/01/01/from-helma-mead-to-martin-chandler/index.html", "/posts/1900/01/01/from-helma-mead-to-martin-chandler.html"], ["1900/01/05/from-martin-chandler-to-elijah-h-chandler-16/index.html", "/posts/1900/01/05/from-martin-chandler-to-elijah-h-chandler-16.html"], ["1900/01/01/from-betty-and-harold-to-millie/index.html", "/posts/1900/01/01/from-betty-and-harold-to-millie.html"], ["1900/01/01/from-hattie-to-mill/index.html", "/posts/1900/01/01/from-hattie-to-mill.html"], ["1900/05/09/from-eva-resterson-to-bessie-chandler/index.html", "/posts/1900/05/09/from-eva-resterson-to-bessie-chandler.html"], ["1900/06/22/from-unknown-to-bess-chandler-3/index.html", "/posts/1900/06/22/from-unknown-to-bess-chandler-3.html"], ["1900/06/04/from-unknown-to-bess-chandler-4/index.html", "/posts/1900/06/04/from-unknown-to-bess-chandler-4.html"], ["1900/07/07/from-lul-m-to-bess-chandler/index.html", "/posts/1900/07/07/from-lul-m-to-bess-chandler.html"], ["1900/07/31/from-frances-werb-to-ruby-chandler/index.html", "/posts/1900/07/31/from-frances-werb-to-ruby-chandler.html"], ["1900/07/18/from-ruby-chandler-to-lucerne-chandler/index.html", "/posts/1900/07/18/from-ruby-chandler-to-lucerne-chandler.html"], ["1900/07/01/from-martin-w-chandler-to-john-bess-and-all/index.html", "/posts/1900/07/01/from-martin-w-chandler-to-john-bess-and-all.html"], ["1900/06/05/from-grace-chandler-to-ruby-and-all/index.html", "/posts/1900/06/05/from-grace-chandler-to-ruby-and-all.html"], ["1900/04/11/from-martin-chandler-to-elijah-h-chandler-and-family-11/index.html", "/posts/1900/04/11/from-martin-chandler-to-elijah-h-chandler-and-family-11.html"], ["1900/07/22/from-martin-chandler-to-elijah-h-chandler-and-family-17/index.html", "/posts/1900/07/22/from-martin-chandler-to-elijah-h-chandler-and-family-17.html"], ["1900/06/26/from-martin-chandler-to-elijah-h-chandler-and-family-18/index.html", "/posts/1900/06/26/from-martin-chandler-to-elijah-h-chandler-and-family-18.html"], ["1900/01/22/from-martin-chandler-to-grace-chandler/index.html", "/posts/1900/01/22/from-martin-chandler-to-grace-chandler.html"], ["1900/02/28/from-martin-chandler-to-elijah-h-chandler-and-family-22/index.html", "/posts/1900/02/28/from-martin-chandler-to-elijah-h-chandler-and-family-22.html"], ["1900/01/26/from-martin-chandler-to-elijah-h-chandler-and-family-32/index.html", "/posts/1900/01/26/from-martin-chandler-to-elijah-h-chandler-and-family-32.html"], ["1900/01/29/from-martin-chandler-to-elijah-h-chandler-and-family-41/index.html", "/posts/1900/01/29/from-martin-chandler-to-elijah-h-chandler-and-family-41.html"], ["1900/01/08/from-martin-chandler-to-elijah-h-chandler-and-family-42/index.html", "/posts/1900/01/08/from-martin-chandler-to-elijah-h-chandler-and-family-42.html"], ["1900/01/18/from-g-lench-to-bess-chandler/index.html", "/posts/1900/01/18/from-g-lench-to-bess-chandler.html"], ["1900/03/10/from-martin-chandler-to-elijah-h-chandler-and-family-49/index.html", "/posts/1900/03/10/from-martin-chandler-to-elijah-h-chandler-and-family-49.html"], ["1900/04/04/from-martin-chandler-to-elijah-h-chandler-17/index.html", "/posts/1900/04/04/from-martin-chandler-to-elijah-h-chandler-17.html"], ["1900/01/27/from-martin-chandler-to-elijah-h-chandler-and-family-50/index.html", "/posts/1900/01/27/from-martin-chandler-to-elijah-h-chandler-and-family-50.html"], ["1900/10/04/from-ray-to-bess-chandler/index.html", "/posts/1900/10/04/from-ray-to-bess-chandler.html"], ["1900/08/02/from-r-g-to-martin-chandler/index.html", "/posts/1900/08/02/from-r-g-to-martin-chandler.html"], ["1900/08/08/from-unknown-to-ruby-chandler/index.html", "/posts/1900/08/08/from-unknown-to-ruby-chandler.html"], ["1900/11/23/from-unknown-to-martin-chandler-3/index.html", "/posts/1900/11/23/from-unknown-to-martin-chandler-3.html"], ["1900/08/08/from-h-blasdel-to-ruby-chandler/index.html", "/posts/1900/08/08/from-h-blasdel-to-ruby-chandler.html"], ["1900/11/13/from-caston-to-grace-chandler/index.html", "/posts/1900/11/13/from-caston-to-grace-chandler.html"], ["1900/11/21/from-martin-w-chandler-to-pike-county-republican/index.html", "/posts/1900/11/21/from-martin-w-chandler-to-pike-county-republican.html"], ["1900/09/09/from-fred-to-bess-chandler-3/index.html", "/posts/1900/09/09/from-fred-to-bess-chandler-3.html"], ["1900/09/07/from-hetty-w-to-bess-chandler/index.html", "/posts/1900/09/07/from-hetty-w-to-bess-chandler.html"], ["1900/12/27/from-scott-w-lucas-to-bess-chandler/index.html", "/posts/1900/12/27/from-scott-w-lucas-to-bess-chandler.html"], ["1900/12/24/from-fisom-harold-to-bess-chandler/index.html", "/posts/1900/12/24/from-fisom-harold-to-bess-chandler.html"], ["1900/12/24/from-madeline-miller-to-lucerne-chandler/index.html", "/posts/1900/12/24/from-madeline-miller-to-lucerne-chandler.html"], ["1900/09/25/from-annie-to-jeanette-and-all/index.html", "/posts/1900/09/25/from-annie-to-jeanette-and-all.html"], ["1900/08/07/from-elijah-l-fhurst-to-margaret-m-knox/index.html", "/posts/1900/08/07/from-elijah-l-fhurst-to-margaret-m-knox.html"], ["1900/12/29/from-martin-chandler-to-elijah-h-chandler-and-family-13/index.html", "/posts/1900/12/29/from-martin-chandler-to-elijah-h-chandler-and-family-13.html"], ["1900/12/16/from-martin-chandler-to-elijah-h-chandler-6/index.html", "/posts/1900/12/16/from-martin-chandler-to-elijah-h-chandler-6.html"], ["1900/09/03/from-martin-chandler-to-unknown-chandler/index.html", "/posts/1900/09/03/from-martin-chandler-to-unknown-chandler.html"], ["1900/10/18/from-martin-chandler-to-elijah-h-chandler-and-family-46/index.html", "/posts/1900/10/18/from-martin-chandler-to-elijah-h-chandler-and-family-46.html"], ["1900/08/30/from-may-to-margaret-knox/index.html", "/posts/1900/08/30/from-may-to-margaret-knox.html"], ["1900/09/01/2554/index.html", "/posts/1900/09/01/2554.html"], ["1909/01/01/from-q-e-c-to-bess-chandler/index.html", "/posts/1909/01/01/from-q-e-c-to-bess-chandler.html"], ["1908/06/12/from-kiona-to-ruby-chandler/index.html", "/posts/1908/06/12/from-kiona-to-ruby-chandler.html"], ["1907/11/24/from-hazel-b-to-grace-chandler/index.html", "/posts/1907/11/24/from-hazel-b-to-grace-chandler.html"], ["1907/01/01/from-unknown-to-ruby-chandler-2/index.html", "/posts/1907/01/01/from-unknown-to-ruby-chandler-2.html"], ["1908/09/25/from-unknown-to-e-h-chandler/index.html", "/posts/1908/09/25/from-unknown-to-e-h-chandler.html"], ["1908/07/04/from-unknown-to-grace-chandler/index.html", "/posts/1908/07/04/from-unknown-to-grace-chandler.html"], ["1908/07/03/from-margaret-to-ruby-chandler/index.html", "/posts/1908/07/03/from-margaret-to-ruby-chandler.html"], ["1908/08/29/from-unknown-to-grace-chandler-2/index.html", "/posts/1908/08/29/from-unknown-to-grace-chandler-2.html"], ["1908/08/13/from-b-h-to-ruby-chandler/index.html", "/posts/1908/08/13/from-b-h-to-ruby-chandler.html"], ["1908/07/01/from-alice-to-ruby-chandler/index.html", "/posts/1908/07/01/from-alice-to-ruby-chandler.html"], ["1908/07/04/from-bess-chandler-to-ruby-chandler/index.html", "/posts/1908/07/04/from-bess-chandler-to-ruby-chandler.html"], ["1908/04/23/from-j-h-to-vinnie-johnston/index.html", "/posts/1908/04/23/from-j-h-to-vinnie-johnston.html"], ["1908/09/01/from-unknown-to-grace-chandler-3/index.html", "/posts/1908/09/01/from-unknown-to-grace-chandler-3.html"], ["1908/07/27/from-harriet-to-ruby-chandler/index.html", "/posts/1908/07/27/from-harriet-to-ruby-chandler.html"], ["1909/05/03/from-unknown-to-grace-chandler-6/index.html", "/posts/1909/05/03/from-unknown-to-grace-chandler-6.html"], ["1909/04/06/from-jack-to-grace-chandler/index.html", "/posts/1909/04/06/from-jack-to-grace-chandler.html"], ["1909/01/01/from-f-foreman-to-ruby-chandler/index.html", "/posts/1909/01/01/from-f-foreman-to-ruby-chandler.html"], ["1908/10/29/from-grace-chandler-to-bess-chandler-4/index.html", "/posts/1908/10/29/from-grace-chandler-to-bess-chandler-4.html"], ["1908/10/02/from-helen-brown-to-ruby-chandler/index.html", "/posts/1908/10/02/from-helen-brown-to-ruby-chandler.html"], ["1907/02/14/from-vinnie-to-margaret-knox/index.html", "/posts/1907/02/14/from-vinnie-to-margaret-knox.html"], ["1909/05/03/from-unknown-to-grace-chandler-5/index.html", "/posts/1909/05/03/from-unknown-to-grace-chandler-5.html"], ["1909/05/07/from-maudine-to-virginia-johnston/index.html", "/posts/1909/05/07/from-maudine-to-virginia-johnston.html"], ["1909/05/12/from-fred-to-ruby-chandler/index.html", "/posts/1909/05/12/from-fred-to-ruby-chandler.html"], ["1909/09/02/from-ralph-a-h-to-grace-chandler/index.html", "/posts/1909/09/02/from-ralph-a-h-to-grace-chandler.html"], ["1909/10/04/from-g-h-l-to-elijah-h-chandler/index.html", "/posts/1909/10/04/from-g-h-l-to-elijah-h-chandler.html"], ["1909/09/18/from-unknown-to-ruby-chandler-5/index.html", "/posts/1909/09/18/from-unknown-to-ruby-chandler-5.html"], ["1909/10/25/from-grace-chandler-to-bess-chandler-2/index.html", "/posts/1909/10/25/from-grace-chandler-to-bess-chandler-2.html"], ["1909/09/06/from-unknown-to-ruby-chandler-6/index.html", "/posts/1909/09/06/from-unknown-to-ruby-chandler-6.html"], ["1909/09/01/from-grace-chandler-to-jeanette-knox-chandler-2/index.html", "/posts/1909/09/01/from-grace-chandler-to-jeanette-knox-chandler-2.html"], ["1910/04/25/from-g-to-ruby-chandler/index.html", "/posts/1910/04/25/from-g-to-ruby-chandler.html"], ["1910/03/13/from-loyd-to-ruby-chandler/index.html", "/posts/1910/03/13/from-loyd-to-ruby-chandler.html"], ["1910/06/05/from-unknown-to-ruby-d-chandler/index.html", "/posts/1910/06/05/from-unknown-to-ruby-d-chandler.html"], ["1910/02/11/from-g-to-bess-chandler/index.html", "/posts/1910/02/11/from-g-to-bess-chandler.html"], ["1910/01/10/from-ruby-chandler-to-bess-chandler-3/index.html", "/posts/1910/01/10/from-ruby-chandler-to-bess-chandler-3.html"], ["1910/06/14/from-eugene-to-bess-chandler-5/index.html", "/posts/1910/06/14/from-eugene-to-bess-chandler-5.html"], ["1910/06/09/from-gladys-to-bess-chandler/index.html", "/posts/1910/06/09/from-gladys-to-bess-chandler.html"], ["1910/05/10/from-grace-chandler-to-bess-m-chandler/index.html", "/posts/1910/05/10/from-grace-chandler-to-bess-m-chandler.html"], ["1910/04/06/from-g-a-m-to-ruby-chandler/index.html", "/posts/1910/04/06/from-g-a-m-to-ruby-chandler.html"], ["1910/03/22/from-grace-chandler-to-ruby-chandler/index.html", "/posts/1910/03/22/from-grace-chandler-to-ruby-chandler.html"], ["1909/08/21/from-ruby-chandler-to-bess-chandler-5/index.html", "/posts/1909/08/21/from-ruby-chandler-to-bess-chandler-5.html"], ["1910/07/24/from-unknown-to-bess-chandler/index.html", "/posts/1910/07/24/from-unknown-to-bess-chandler.html"], ["1910/06/28/from-unknown-to-ruby-chandler-7/index.html", "/posts/1910/06/28/from-unknown-to-ruby-chandler-7.html"], ["1910/08/01/from-ruby-chandler-to-jeanette-knox-chandler-2/index.html", "/posts/1910/08/01/from-ruby-chandler-to-jeanette-knox-chandler-2.html"], ["1910/06/22/from-eugene-to-bess-chandler-2/index.html", "/posts/1910/06/22/from-eugene-to-bess-chandler-2.html"], ["1910/06/17/from-eugene-to-bess-chandler-3/index.html", "/posts/1910/06/17/from-eugene-to-bess-chandler-3.html"], ["1910/07/13/from-ruby-chandler-to-elijah-h-chandler-2/index.html", "/posts/1910/07/13/from-ruby-chandler-to-elijah-h-chandler-2.html"], ["1910/08/19/from-ida-to-grover-hoover/index.html", "/posts/1910/08/19/from-ida-to-grover-hoover.html"], ["1910/07/17/from-unknown-to-ruby-chandler-9/index.html", "/posts/1910/07/17/from-unknown-to-ruby-chandler-9.html"], ["1910/07/05/from-unknown-to-bess-chandler-8/index.html", "/posts/1910/07/05/from-unknown-to-bess-chandler-8.html"], ["1910/07/11/from-clara-to-grace-chandler/index.html", "/posts/1910/07/11/from-clara-to-grace-chandler.html"], ["1910/07/04/from-eugene-to-bess-chandler-4/index.html", "/posts/1910/07/04/from-eugene-to-bess-chandler-4.html"], ["1910/08/22/from-e-moore-to-grover-hoover/index.html", "/posts/1910/08/22/from-e-moore-to-grover-hoover.html"], ["1910/08/03/from-chas-to-ruby-d-chandler/index.html", "/posts/1910/08/03/from-chas-to-ruby-d-chandler.html"], ["1910/07/20/from-grace-chandler-to-bess-chandler-3/index.html", "/posts/1910/07/20/from-grace-chandler-to-bess-chandler-3.html"], ["1910/07/07/from-lu-to-bess-chandler/index.html", "/posts/1910/07/07/from-lu-to-bess-chandler.html"], ["1910/08/01/from-ruby-chandler-to-bess-chandler-4/index.html", "/posts/1910/08/01/from-ruby-chandler-to-bess-chandler-4.html"], ["1910/08/01/from-m-to-ruby-chandler/index.html", "/posts/1910/08/01/from-m-to-ruby-chandler.html"], ["1910/08/03/from-ruby-chandler-to-lucerne-chandler-2/index.html", "/posts/1910/08/03/from-ruby-chandler-to-lucerne-chandler-2.html"], ["1910/08/01/from-ruby-chandler-to-martin-chandler/index.html", "/posts/1910/08/01/from-ruby-chandler-to-martin-chandler.html"], ["1910/06/27/from-led-to-ruby-chandler/index.html", "/posts/1910/06/27/from-led-to-ruby-chandler.html"], ["1910/09/03/from-eugene-to-bess-chandler/index.html", "/posts/1910/09/03/from-eugene-to-bess-chandler.html"], ["1910/12/21/from-unknown-to-ruby-chandler-8/index.html", "/posts/1910/12/21/from-unknown-to-ruby-chandler-8.html"], ["1910/09/06/from-eugene-to-bess-chandler-6/index.html", "/posts/1910/09/06/from-eugene-to-bess-chandler-6.html"], ["1910/09/07/from-unknown-to-bess-chandler-7/index.html", "/posts/1910/09/07/from-unknown-to-bess-chandler-7.html"], ["1910/12/21/from-a-f-r-to-grace-chandler/index.html", "/posts/1910/12/21/from-a-f-r-to-grace-chandler.html"], ["1910/12/25/from-jon-to-bess-chandler/index.html", "/posts/1910/12/25/from-jon-to-bess-chandler.html"], ["1910/10/17/from-unknown-to-bess-chandler-9/index.html", "/posts/1910/10/17/from-unknown-to-bess-chandler-9.html"], ["1910/12/22/from-arthur-vincent-davis-to-elijah-h-chandler-and-family/index.html", "/posts/1910/12/22/from-arthur-vincent-davis-to-elijah-h-chandler-and-family.html"], ["1910/10/28/from-opal-chandler-to-ruby-chandler/index.html", "/posts/1910/10/28/from-opal-chandler-to-ruby-chandler.html"], ["1910/12/21/from-dick-to-bess-chandler/index.html", "/posts/1910/12/21/from-dick-to-bess-chandler.html"], ["1910/11/21/from-pearl-e-to-ruby-chandler-2/index.html", "/posts/1910/11/21/from-pearl-e-to-ruby-chandler-2.html"], ["1910/09/03/from-pearl-e-to-ruby-chandler-3/index.html", "/posts/1910/09/03/from-pearl-e-to-ruby-chandler-3.html"], ["1910/10/28/from-g-b-to-bess-chandler/index.html", "/posts/1910/10/28/from-g-b-to-bess-chandler.html"], ["1910/12/10/from-maud-to-ruby-chandler/index.html", "/posts/1910/12/10/from-maud-to-ruby-chandler.html"], ["1910/10/20/from-jon-to-grace-chandler/index.html", "/posts/1910/10/20/from-jon-to-grace-chandler.html"], ["1910/09/19/from-russell-bauer-to-grace-chandler/index.html", "/posts/1910/09/19/from-russell-bauer-to-grace-chandler.html"], ["1910/10/20/from-pearl-e-to-ruby-chandler-4/index.html", "/posts/1910/10/20/from-pearl-e-to-ruby-chandler-4.html"], ["1910/09/28/from-opal-chandler-to-ruby-chandler-2/index.html", "/posts/1910/09/28/from-opal-chandler-to-ruby-chandler-2.html"], ["1910/12/27/from-gema-allen-to-ruby-chandler/index.html", "/posts/1910/12/27/from-gema-allen-to-ruby-chandler.html"], ["1910/12/09/from-unknown-to-margaret-chandler-2/index.html", "/posts/1910/12/09/from-unknown-to-margaret-chandler-2.html"], ["1911/04/27/from-unknown-to-bess-chandler-6/index.html", "/posts/1911/04/27/from-unknown-to-bess-chandler-6.html"], ["1911/03/19/from-chas-morgan-to-ruby-chandler/index.html", "/posts/1911/03/19/from-chas-morgan-to-ruby-chandler.html"], ["1911/05/20/from-ruby-chandler-to-elijah-h-chandler/index.html", "/posts/1911/05/20/from-ruby-chandler-to-elijah-h-chandler.html"], ["1911/01/18/from-pearl-to-ruby-chandler/index.html", "/posts/1911/01/18/from-pearl-to-ruby-chandler.html"], ["1911/04/13/from-mrs-w-franklin-to-ruby-chandler/index.html", "/posts/1911/04/13/from-mrs-w-franklin-to-ruby-chandler.html"], ["1911/05/02/from-bess-chandler-to-grace-chandler/index.html", "/posts/1911/05/02/from-bess-chandler-to-grace-chandler.html"], ["1911/01/28/from-clias-to-bess-chandler/index.html", "/posts/1911/01/28/from-clias-to-bess-chandler.html"], ["1911/05/13/from-grace-chandler-to-bess-chandler/index.html", "/posts/1911/05/13/from-grace-chandler-to-bess-chandler.html"], ["1911/05/01/from-ruby-chandler-to-jeanette-knox-chandler/index.html", "/posts/1911/05/01/from-ruby-chandler-to-jeanette-knox-chandler.html"], ["1911/04/15/from-jessie-webster-to-bess-chandler/index.html", "/posts/1911/04/15/from-jessie-webster-to-bess-chandler.html"], ["1911/05/08/from-grace-chandler-to-lucerne-chandler/index.html", "/posts/1911/05/08/from-grace-chandler-to-lucerne-chandler.html"], ["1911/02/13/from-unknown-to-ruby-chandler-3/index.html", "/posts/1911/02/13/from-unknown-to-ruby-chandler-3.html"], ["1911/05/08/from-unknown-to-ruby-chandler-4/index.html", "/posts/1911/05/08/from-unknown-to-ruby-chandler-4.html"], ["1911/01/23/from-l-m-to-ruby-chandler/index.html", "/posts/1911/01/23/from-l-m-to-ruby-chandler.html"], ["1911/05/01/from-grace-chandler-to-elijah-h-chandler/index.html", "/posts/1911/05/01/from-grace-chandler-to-elijah-h-chandler.html"], ["1911/05/16/from-grace-chandler-to-martin-chandler-2/index.html", "/posts/1911/05/16/from-grace-chandler-to-martin-chandler-2.html"], ["1911/02/18/from-martin-chandler-to-elijah-h-chandler-and-family-2/index.html", "/posts/1911/02/18/from-martin-chandler-to-elijah-h-chandler-and-family-2.html"], ["1910/12/28/from-gritnder-to-bess-chandler/index.html", "/posts/1910/12/28/from-gritnder-to-bess-chandler.html"], ["1911/02/02/from-w-d-skinner-to-ticket-agent/index.html", "/posts/1911/02/02/from-w-d-skinner-to-ticket-agent.html"], ["1911/01/23/from-chas-to-grace-chandler/index.html", "/posts/1911/01/23/from-chas-to-grace-chandler.html"], ["1911/05/23/from-s-r-a-to-ruby-chandler/index.html", "/posts/1911/05/23/from-s-r-a-to-ruby-chandler.html"], ["1911/06/26/from-vesne-to-ruby-chandler/index.html", "/posts/1911/06/26/from-vesne-to-ruby-chandler.html"], ["1911/07/24/from-freeda-to-bess-chandler/index.html", "/posts/1911/07/24/from-freeda-to-bess-chandler.html"], ["1911/07/18/from-chas-to-ruby-chandler/index.html", "/posts/1911/07/18/from-chas-to-ruby-chandler.html"], ["1911/07/24/from-freeda-c-to-ruby-chandler/index.html", "/posts/1911/07/24/from-freeda-c-to-ruby-chandler.html"], ["1911/06/01/from-ruby-chandler-to-bess-chandler-2/index.html", "/posts/1911/06/01/from-ruby-chandler-to-bess-chandler-2.html"], ["1911/05/22/from-grace-chandler-to-martin-chandler/index.html", "/posts/1911/05/22/from-grace-chandler-to-martin-chandler.html"], ["1911/07/06/from-lhennay-to-ruby-chandler/index.html", "/posts/1911/07/06/from-lhennay-to-ruby-chandler.html"], ["1911/05/31/from-m-b-hoppler-to-jeanette-knox-chandler/index.html", "/posts/1911/05/31/from-m-b-hoppler-to-jeanette-knox-chandler.html"], ["1911/07/25/from-unknown-to-grace-chandler-4/index.html", "/posts/1911/07/25/from-unknown-to-grace-chandler-4.html"], ["1911/07/04/from-allen-to-ruby-chandler/index.html", "/posts/1911/07/04/from-allen-to-ruby-chandler.html"], ["1911/07/07/from-allen-to-ruby-chandler-2/index.html", "/posts/1911/07/07/from-allen-to-ruby-chandler-2.html"], ["1911/07/05/from-allen-to-ruby-chandler-3/index.html", "/posts/1911/07/05/from-allen-to-ruby-chandler-3.html"], ["1911/07/02/from-bill-to-bess-chandler/index.html", "/posts/1911/07/02/from-bill-to-bess-chandler.html"], ["1911/06/19/from-allen-to-ruby-chandler-4/index.html", "/posts/1911/06/19/from-allen-to-ruby-chandler-4.html"], ["1911/07/23/from-allen-to-ruby-chandler-5/index.html", "/posts/1911/07/23/from-allen-to-ruby-chandler-5.html"], ["1911/06/21/from-florida-to-bess-chandler/index.html", "/posts/1911/06/21/from-florida-to-bess-chandler.html"], ["1911/06/21/from-bill-to-ruby-chandler/index.html", "/posts/1911/06/21/from-bill-to-ruby-chandler.html"], ["1911/06/22/from-allen-to-ruby-chandler-7/index.html", "/posts/1911/06/22/from-allen-to-ruby-chandler-7.html"], ["1911/07/25/from-duffy-to-ruby-chandler/index.html", "/posts/1911/07/25/from-duffy-to-ruby-chandler.html"], ["1911/08/17/from-dollie-to-bess-chandler/index.html", "/posts/1911/08/17/from-dollie-to-bess-chandler.html"], ["1911/08/08/from-unknown-to-bess-chandler-5/index.html", "/posts/1911/08/08/from-unknown-to-bess-chandler-5.html"], ["1911/09/06/from-fred-to-bess-chandler/index.html", "/posts/1911/09/06/from-fred-to-bess-chandler.html"], ["1911/11/02/from-a-v-d-to-elijah-h-chandler/index.html", "/posts/1911/11/02/from-a-v-d-to-elijah-h-chandler.html"], ["1911/08/31/from-ruby-chandler-to-bess-chandler/index.html", "/posts/1911/08/31/from-ruby-chandler-to-bess-chandler.html"], ["1911/08/03/from-vesa-to-ruby-chandler/index.html", "/posts/1911/08/03/from-vesa-to-ruby-chandler.html"], ["1911/10/08/from-lucele-to-bess-chandler/index.html", "/posts/1911/10/08/from-lucele-to-bess-chandler.html"], ["1911/08/07/from-marie-h-to-bess-chandler/index.html", "/posts/1911/08/07/from-marie-h-to-bess-chandler.html"], ["1911/07/31/from-frances-werk-to-bess-chandler/index.html", "/posts/1911/07/31/from-frances-werk-to-bess-chandler.html"], ["1911/12/15/from-ruth-to-bess-chandler/index.html", "/posts/1911/12/15/from-ruth-to-bess-chandler.html"], ["1911/08/26/from-fred-to-bess-chandler-2/index.html", "/posts/1911/08/26/from-fred-to-bess-chandler-2.html"], ["1911/07/26/from-lorene-m-bollin-to-ruby-chandler/index.html", "/posts/1911/07/26/from-lorene-m-bollin-to-ruby-chandler.html"], ["1911/07/25/from-emma-jay-to-ruby-chandler/index.html", "/posts/1911/07/25/from-emma-jay-to-ruby-chandler.html"], ["1911/09/27/from-j-w-s-to-bess-chandler/index.html", "/posts/1911/09/27/from-j-w-s-to-bess-chandler.html"], ["1911/07/25/from-emma-jay-to-bess-chandler/index.html", "/posts/1911/07/25/from-emma-jay-to-bess-chandler.html"], ["1911/09/08/from-ruby-chandler-to-grace-chandler/index.html", "/posts/1911/09/08/from-ruby-chandler-to-grace-chandler.html"], ["1911/12/21/from-hugh-hearner-to-bess-chandler/index.html", "/posts/1911/12/21/from-hugh-hearner-to-bess-chandler.html"], ["1911/08/01/from-allen-to-ruby-chandler-6/index.html", "/posts/1911/08/01/from-allen-to-ruby-chandler-6.html"], ["1911/07/28/from-clias-to-ruby-chandler/index.html", "/posts/1911/07/28/from-clias-to-ruby-chandler.html"], ["1911/07/27/from-ruth-to-grace-chandler/index.html", "/posts/1911/07/27/from-ruth-to-grace-chandler.html"], ["1913/01/01/from-unknown-to-a-v-davis/index.html", "/posts/1913/01/01/from-unknown-to-a-v-davis.html"], ["1912/06/10/from-benson-to-ruby-chandler/index.html", "/posts/1912/06/10/from-benson-to-ruby-chandler.html"], ["1912/07/17/from-unknown-to-margaret-chandler/index.html", "/posts/1912/07/17/from-unknown-to-margaret-chandler.html"], ["1911/12/24/from-lucile-hardin-to-bess-chandler/index.html", "/posts/1911/12/24/from-lucile-hardin-to-bess-chandler.html"], ["1911/12/22/from-pearl-e-to-ruby-chandler/index.html", "/posts/1911/12/22/from-pearl-e-to-ruby-chandler.html"], ["1912/09/10/from-unknown-to-knox-chandler-family/index.html", "/posts/1912/09/10/from-unknown-to-knox-chandler-family.html"], ["1912/07/10/from-grace-chandler-to-elijah-h-chandler-2/index.html", "/posts/1912/07/10/from-grace-chandler-to-elijah-h-chandler-2.html"], ["1912/06/17/from-marie-husmann-to-ruby-chandler-2/index.html", "/posts/1912/06/17/from-marie-husmann-to-ruby-chandler-2.html"], ["1912/08/21/from-leoto-to-bess-chandler/index.html", "/posts/1912/08/21/from-leoto-to-bess-chandler.html"], ["1912/06/10/from-unknown-to-bess-chandler-11/index.html", "/posts/1912/06/10/from-unknown-to-bess-chandler-11.html"], ["1912/07/30/from-grace-chandler-to-jeanette-knox-chandler-3/index.html", "/posts/1912/07/30/from-grace-chandler-to-jeanette-knox-chandler-3.html"], ["1912/07/20/from-grace-chandler-to-lucerne-chandler-2/index.html", "/posts/1912/07/20/from-grace-chandler-to-lucerne-chandler-2.html"], ["1912/08/28/from-h-whittaker-to-bess-chandler/index.html", "/posts/1912/08/28/from-h-whittaker-to-bess-chandler.html"], ["1912/08/18/from-vivien-dawson-to-bess-harleson/index.html", "/posts/1912/08/18/from-vivien-dawson-to-bess-harleson.html"], ["1913/01/22/from-mae-chandler-to-bess-chandler/index.html", "/posts/1913/01/22/from-mae-chandler-to-bess-chandler.html"], ["1912/08/10/from-g-l-w-to-bess-chandler/index.html", "/posts/1912/08/10/from-g-l-w-to-bess-chandler.html"], ["1912/09/04/from-harold-g-to-bess-chandler/index.html", "/posts/1912/09/04/from-harold-g-to-bess-chandler.html"], ["1912/08/17/from-j-t-w-to-bess-chandler/index.html", "/posts/1912/08/17/from-j-t-w-to-bess-chandler.html"], ["1912/10/23/from-ruby-chandler-to-elijah-h-chandler-and-family/index.html", "/posts/1912/10/23/from-ruby-chandler-to-elijah-h-chandler-and-family.html"], ["1912/11/28/from-unknown-to-grace-chandler-7/index.html", "/posts/1912/11/28/from-unknown-to-grace-chandler-7.html"], ["1915/08/10/from-lucille-to-bess-chandler/index.html", "/posts/1915/08/10/from-lucille-to-bess-chandler.html"], ["1913/08/09/from-dan-to-bess-chandler/index.html", "/posts/1913/08/09/from-dan-to-bess-chandler.html"], ["1913/05/18/from-o-f-r-to-grace-chandler/index.html", "/posts/1913/05/18/from-o-f-r-to-grace-chandler.html"], ["1913/06/25/from-marie-husmann-to-ruby-chandler/index.html", "/posts/1913/06/25/from-marie-husmann-to-ruby-chandler.html"], ["1915/01/02/from-ruby-chandler-to-elijah-h-chandler-3/index.html", "/posts/1915/01/02/from-ruby-chandler-to-elijah-h-chandler-3.html"], ["1913/06/19/from-j-m-jones-to-grace-chandler/index.html", "/posts/1913/06/19/from-j-m-jones-to-grace-chandler.html"], ["1916/02/19/from-martin-chandler-to-elijah-h-chandler-and-family-12/index.html", "/posts/1916/02/19/from-martin-chandler-to-elijah-h-chandler-and-family-12.html"], ["1915/12/31/from-martin-chandler-to-elijah-h-chandler-10/index.html", "/posts/1915/12/31/from-martin-chandler-to-elijah-h-chandler-10.html"], ["1916/01/06/from-martin-chandler-to-elijah-h-chandler-and-family-38/index.html", "/posts/1916/01/06/from-martin-chandler-to-elijah-h-chandler-and-family-38.html"], ["1915/12/24/from-martin-chandler-to-elijah-h-chandler-and-family-39/index.html", "/posts/1915/12/24/from-martin-chandler-to-elijah-h-chandler-and-family-39.html"], ["1915/01/05/from-martin-chandler-to-elijah-h-chandler-and-family-43/index.html", "/posts/1915/01/05/from-martin-chandler-to-elijah-h-chandler-and-family-43.html"], ["1916/01/14/from-martin-chandler-to-elijah-h-chandler-13/index.html", "/posts/1916/01/14/from-martin-chandler-to-elijah-h-chandler-13.html"], ["1915/01/06/from-martin-chandler-to-elijah-h-chandler-and-family-44/index.html", "/posts/1915/01/06/from-martin-chandler-to-elijah-h-chandler-and-family-44.html"], ["1915/12/18/from-henry-t-rainey-to-e-h-chandler/index.html", "/posts/1915/12/18/from-henry-t-rainey-to-e-h-chandler.html"], ["1915/12/21/from-martin-chandler-to-elijah-h-chandler-and-family-51/index.html", "/posts/1915/12/21/from-martin-chandler-to-elijah-h-chandler-and-family-51.html"], ["1915/12/25/from-martin-chandler-to-elijah-h-chandler-and-family-52/index.html", "/posts/1915/12/25/from-martin-chandler-to-elijah-h-chandler-and-family-52.html"], ["1916/02/07/from-martin-chandler-to-elijah-h-chandler-and-family-55/index.html", "/posts/1916/02/07/from-martin-chandler-to-elijah-h-chandler-and-family-55.html"], ["1915/12/20/from-martin-chandler-to-elijah-h-chandler-and-family-56/index.html", "/posts/1915/12/20/from-martin-chandler-to-elijah-h-chandler-and-family-56.html"], ["1915/06/21/from-lorin-chandler-to-elijah-h-chandler-and-family/index.html", "/posts/1915/06/21/from-lorin-chandler-to-elijah-h-chandler-and-family.html"], ["1916/06/02/from-martin-chandler-to-elijah-h-chandler-and-family-57/index.html", "/posts/1916/06/02/from-martin-chandler-to-elijah-h-chandler-and-family-57.html"], ["1916/09/19/from-opal-to-jeanette-knox-chandler/index.html", "/posts/1916/09/19/from-opal-to-jeanette-knox-chandler.html"], ["1917/01/17/from-bess-chandler-to-lucerne-chandler/index.html", "/posts/1917/01/17/from-bess-chandler-to-lucerne-chandler.html"], ["1917/01/08/from-grace-chandler-to-chandler-family/index.html", "/posts/1917/01/08/from-grace-chandler-to-chandler-family.html"], ["1917/01/10/from-martin-chandler-to-elijah-h-chandler-and-family/index.html", "/posts/1917/01/10/from-martin-chandler-to-elijah-h-chandler-and-family.html"], ["1916/09/21/from-opal-chandler-to-jeanette-knox-chandler-and-family/index.html", "/posts/1916/09/21/from-opal-chandler-to-jeanette-knox-chandler-and-family.html"], ["1916/09/29/from-jeanette-knox-chandler-to-ruby-d-chandler/index.html", "/posts/1916/09/29/from-jeanette-knox-chandler-to-ruby-d-chandler.html"], ["1916/09/03/from-martin-chandler-to-richard-knox-chandler/index.html", "/posts/1916/09/03/from-martin-chandler-to-richard-knox-chandler.html"], ["1917/05/05/from-martin-chandler-to-elijah-h-chandler-4/index.html", "/posts/1917/05/05/from-martin-chandler-to-elijah-h-chandler-4.html"], ["1916/10/01/from-grace-chandler-to-elijah-h-chandler-and-family/index.html", "/posts/1916/10/01/from-grace-chandler-to-elijah-h-chandler-and-family.html"], ["1916/08/16/from-martin-chandler-to-jeanette-knox-chandler-and-family/index.html", "/posts/1916/08/16/from-martin-chandler-to-jeanette-knox-chandler-and-family.html"], ["1916/09/20/from-martin-chandler-to-elijah-h-chandler-and-family-9/index.html", "/posts/1916/09/20/from-martin-chandler-to-elijah-h-chandler-and-family-9.html"], ["1917/01/09/from-martin-chandler-to-elijah-h-chandler-and-family-14/index.html", "/posts/1917/01/09/from-martin-chandler-to-elijah-h-chandler-and-family-14.html"], ["1916/08/09/from-martin-chandler-to-elijah-h-chandler-and-family-16/index.html", "/posts/1916/08/09/from-martin-chandler-to-elijah-h-chandler-and-family-16.html"], ["1917/05/03/from-martin-chandler-to-elijah-h-chandler-8/index.html", "/posts/1917/05/03/from-martin-chandler-to-elijah-h-chandler-8.html"], ["1917/05/09/from-martin-chandler-to-elijah-h-chandler-and-family-29/index.html", "/posts/1917/05/09/from-martin-chandler-to-elijah-h-chandler-and-family-29.html"], ["1916/09/18/from-martin-chandler-to-elijah-h-chandler-and-family-35/index.html", "/posts/1916/09/18/from-martin-chandler-to-elijah-h-chandler-and-family-35.html"], ["1917/01/02/from-martin-chandler-to-elijah-h-chandler-and-family-36/index.html", "/posts/1917/01/02/from-martin-chandler-to-elijah-h-chandler-and-family-36.html"], ["1916/06/05/from-martin-chandler-to-elijah-h-chandler-and-family-53/index.html", "/posts/1916/06/05/from-martin-chandler-to-elijah-h-chandler-and-family-53.html"], ["1916/11/06/from-bess-chandler-to-jeanette-knox-chandler-and-family/index.html", "/posts/1916/11/06/from-bess-chandler-to-jeanette-knox-chandler-and-family.html"], ["1916/10/27/from-grace-chandler-to-jeanette-knox-chandler-and-family-2/index.html", "/posts/1916/10/27/from-grace-chandler-to-jeanette-knox-chandler-and-family-2.html"], ["1917/10/24/from-unknown-to-martin-chandler-4/index.html", "/posts/1917/10/24/from-unknown-to-martin-chandler-4.html"], ["1917/10/20/from-martin-chandler-to-chandler-family/index.html", "/posts/1917/10/20/from-martin-chandler-to-chandler-family.html"], ["1917/12/11/from-ruby-chandler-to-margaret-chandler/index.html", "/posts/1917/12/11/from-ruby-chandler-to-margaret-chandler.html"], ["1917/12/07/from-bess-chandler-to-elijah-h-chandler/index.html", "/posts/1917/12/07/from-bess-chandler-to-elijah-h-chandler.html"], ["1917/12/13/from-grover-c-hoover-to-jeanette-knox-chandeler/index.html", "/posts/1917/12/13/from-grover-c-hoover-to-jeanette-knox-chandeler.html"], ["1917/06/09/from-margaret-chandler-to-ruby-chandler/index.html", "/posts/1917/06/09/from-margaret-chandler-to-ruby-chandler.html"], ["1917/05/31/from-martin-chandler-to-elijah-h-chandler-and-family-3/index.html", "/posts/1917/05/31/from-martin-chandler-to-elijah-h-chandler-and-family-3.html"], ["1917/12/07/from-martin-chandler-to-elijah-h-chandler-and-family-5/index.html", "/posts/1917/12/07/from-martin-chandler-to-elijah-h-chandler-and-family-5.html"], ["1917/07/11/from-martin-chandler-to-elijah-h-chandler-and-family-8/index.html", "/posts/1917/07/11/from-martin-chandler-to-elijah-h-chandler-and-family-8.html"], ["1917/12/26/from-martin-chandler-to-elijah-h-chandler-and-family-15/index.html", "/posts/1917/12/26/from-martin-chandler-to-elijah-h-chandler-and-family-15.html"], ["1917/12/04/from-martin-chandler-to-elijah-h-chandler-and-family-24/index.html", "/posts/1917/12/04/from-martin-chandler-to-elijah-h-chandler-and-family-24.html"], ["1917/11/16/from-martin-chandler-to-elijah-h-chandler-and-family-26/index.html", "/posts/1917/11/16/from-martin-chandler-to-elijah-h-chandler-and-family-26.html"], ["1917/06/04/from-martin-chandler-to-elijah-h-chandler-and-family-30/index.html", "/posts/1917/06/04/from-martin-chandler-to-elijah-h-chandler-and-family-30.html"], ["1917/10/25/from-martin-chandler-to-elijah-h-chandler-and-family-31/index.html", "/posts/1917/10/25/from-martin-chandler-to-elijah-h-chandler-and-family-31.html"], ["1917/09/28/from-martin-chandler-to-elijah-h-chandler-and-family-37/index.html", "/posts/1917/09/28/from-martin-chandler-to-elijah-h-chandler-and-family-37.html"], ["1917/11/02/from-martin-chandler-to-margaret-chandler/index.html", "/posts/1917/11/02/from-martin-chandler-to-margaret-chandler.html"], ["1917/12/17/from-martin-chandler-to-elijah-h-chandler-11/index.html", "/posts/1917/12/17/from-martin-chandler-to-elijah-h-chandler-11.html"], ["1917/10/08/from-martin-chandler-to-elijah-h-chandler-12/index.html", "/posts/1917/10/08/from-martin-chandler-to-elijah-h-chandler-12.html"], ["1917/08/27/from-martin-chandler-to-elijah-h-chandler-and-family-45/index.html", "/posts/1917/08/27/from-martin-chandler-to-elijah-h-chandler-and-family-45.html"], ["1917/07/03/from-martin-chandler-to-elijah-h-chandler-and-family-47/index.html", "/posts/1917/07/03/from-martin-chandler-to-elijah-h-chandler-and-family-47.html"], ["1917/12/31/from-mother-gowin-to-jeanette-knox-chandler/index.html", "/posts/1917/12/31/from-mother-gowin-to-jeanette-knox-chandler.html"], ["1918/08/03/from-margaret-chandler-to-jeanette-knox-chandler-and-family/index.html", "/posts/1918/08/03/from-margaret-chandler-to-jeanette-knox-chandler-and-family.html"], ["1918/08/03/from-grace-chandler-to-jeanette-knox-chandler-and-family/index.html", "/posts/1918/08/03/from-grace-chandler-to-jeanette-knox-chandler-and-family.html"], ["1918/02/22/from-martin-chandler-to-elijah-h-chandler-and-family-4/index.html", "/posts/1918/02/22/from-martin-chandler-to-elijah-h-chandler-and-family-4.html"], ["1918/08/13/from-martin-chandler-to-elijah-h-chandler-and-family-6/index.html", "/posts/1918/08/13/from-martin-chandler-to-elijah-h-chandler-and-family-6.html"], ["1918/08/18/from-martin-chandler-to-elijah-h-chandler-and-family-10/index.html", "/posts/1918/08/18/from-martin-chandler-to-elijah-h-chandler-and-family-10.html"], ["1918/06/25/from-martin-chandler-to-elijah-h-chandler-and-family-20/index.html", "/posts/1918/06/25/from-martin-chandler-to-elijah-h-chandler-and-family-20.html"], ["1918/03/19/from-martin-chandler-to-elijah-h-chandler-and-family-23/index.html", "/posts/1918/03/19/from-martin-chandler-to-elijah-h-chandler-and-family-23.html"], ["1918/09/01/from-martin-chandler-to-elijah-h-chandler-and-family-25/index.html", "/posts/1918/09/01/from-martin-chandler-to-elijah-h-chandler-and-family-25.html"], ["1918/06/15/from-martin-chandler-to-grace-chandler-and-family/index.html", "/posts/1918/06/15/from-martin-chandler-to-grace-chandler-and-family.html"], ["1918/01/13/from-martin-chandler-to-elijah-h-chandler-and-family-33/index.html", "/posts/1918/01/13/from-martin-chandler-to-elijah-h-chandler-and-family-33.html"], ["1918/05/13/from-martin-chandler-to-elijah-h-chandler-and-family-34/index.html", "/posts/1918/05/13/from-martin-chandler-to-elijah-h-chandler-and-family-34.html"], ["1918/01/20/from-bess-chandler-to-elijah-h-chandler-2/index.html", "/posts/1918/01/20/from-bess-chandler-to-elijah-h-chandler-2.html"], ["1918/04/30/from-martin-chandler-to-elijah-h-chandler-14/index.html", "/posts/1918/04/30/from-martin-chandler-to-elijah-h-chandler-14.html"], ["1918/08/02/from-ruby-chandler-to-elijah-h-chandler-and-family-2/index.html", "/posts/1918/08/02/from-ruby-chandler-to-elijah-h-chandler-and-family-2.html"], ["1918/04/17/from-sam-mullholland-to-jeanette-knox-chandler/index.html", "/posts/1918/04/17/from-sam-mullholland-to-jeanette-knox-chandler.html"], ["1918/06/27/from-martin-chandler-to-elijah-h-chandler-and-family-60/index.html", "/posts/1918/06/27/from-martin-chandler-to-elijah-h-chandler-and-family-60.html"], ["1918/03/16/from-martin-chandler-to-elijah-h-chandler-and-family-62/index.html", "/posts/1918/03/16/from-martin-chandler-to-elijah-h-chandler-and-family-62.html"], ["1918/01/05/from-martin-chandler-to-elijah-h-chandler-and-family-64/index.html", "/posts/1918/01/05/from-martin-chandler-to-elijah-h-chandler-and-family-64.html"], ["1918/05/20/from-martin-chandler-to-elijah-h-chandler-and-family-65/index.html", "/posts/1918/05/20/from-martin-chandler-to-elijah-h-chandler-and-family-65.html"], ["1918/11/08/from-unknown-to-elijah-h-chandler/index.html", "/posts/1918/11/08/from-unknown-to-elijah-h-chandler.html"], ["1919/01/07/from-vinnie-to-jeanette-knox-chandler-and-family/index.html", "/posts/1919/01/07/from-vinnie-to-jeanette-knox-chandler-and-family.html"], ["1918/12/16/from-martin-chandler-to-elijah-h-chandler/index.html", "/posts/1918/12/16/from-martin-chandler-to-elijah-h-chandler.html"], ["1918/12/20/from-martin-chandler-to-elijah-h-chandler-2/index.html", "/posts/1918/12/20/from-martin-chandler-to-elijah-h-chandler-2.html"], ["1919/03/26/from-martin-chandler-to-elijah-h-chandler-and-family-7/index.html", "/posts/1919/03/26/from-martin-chandler-to-elijah-h-chandler-and-family-7.html"], ["1919/03/06/from-martin-chandler-to-elijah-h-chandler-and-family-19/index.html", "/posts/1919/03/06/from-martin-chandler-to-elijah-h-chandler-and-family-19.html"], ["1918/11/02/from-martin-chandler-to-elijah-h-chandler-and-family-27/index.html", "/posts/1918/11/02/from-martin-chandler-to-elijah-h-chandler-and-family-27.html"], ["1918/11/20/from-elijah-h-chandler-to-jeanette-knox-chandler-9/index.html", "/posts/1918/11/20/from-elijah-h-chandler-to-jeanette-knox-chandler-9.html"], ["1918/10/24/from-martin-chandler-to-elijah-h-chandler-and-family-28/index.html", "/posts/1918/10/24/from-martin-chandler-to-elijah-h-chandler-and-family-28.html"], ["1918/10/12/from-martin-chandler-to-elijah-h-chandler-7/index.html", "/posts/1918/10/12/from-martin-chandler-to-elijah-h-chandler-7.html"], ["1919/01/30/from-martin-chandler-to-elijah-h-chandler-9/index.html", "/posts/1919/01/30/from-martin-chandler-to-elijah-h-chandler-9.html"], ["1918/09/29/from-martin-chandler-to-elijah-h-chandler-and-family-40/index.html", "/posts/1918/09/29/from-martin-chandler-to-elijah-h-chandler-and-family-40.html"], ["1919/01/22/from-martin-chandler-to-elijah-h-chandler-and-family-48/index.html", "/posts/1919/01/22/from-martin-chandler-to-elijah-h-chandler-and-family-48.html"], ["1918/12/30/from-martin-chandler-to-elijah-h-chandler-and-family-59/index.html", "/posts/1918/12/30/from-martin-chandler-to-elijah-h-chandler-and-family-59.html"], ["1918/11/04/2696/index.html", "/posts/1918/11/04/2696.html"], ["1918/12/24/from-martin-chandler-to-elijah-h-chandler-20/index.html", "/posts/1918/12/24/from-martin-chandler-to-elijah-h-chandler-20.html"], ["1918/11/07/from-martin-chandler-to-elijah-h-chandler-and-family-61/index.html", "/posts/1918/11/07/from-martin-chandler-to-elijah-h-chandler-and-family-61.html"], ["1919/01/16/from-martin-chandler-to-elijah-h-chandler-and-family-63/index.html", "/posts/1919/01/16/from-martin-chandler-to-elijah-h-chandler-and-family-63.html"], ["1918/11/24/from-esther-harrington-to-jeanette-knox-chandler/index.html", "/posts/1918/11/24/from-esther-harrington-to-jeanette-knox-chandler.html"], ["1919/01/01/from-martin-chandler-to-elijah-h-chandler-and-family-66/index.html", "/posts/1919/01/01/from-martin-chandler-to-elijah-h-chandler-and-family-66.html"], ["1920/03/15/from-ruby-chandler-to-e-h-chandler/index.html", "/posts/1920/03/15/from-ruby-chandler-to-e-h-chandler.html"], ["1921/06/05/from-liam-to-e-h-chandler/index.html", "/posts/1921/06/05/from-liam-to-e-h-chandler.html"], ["1921/06/11/from-opal-to-e-h-chandler/index.html", "/posts/1921/06/11/from-opal-to-e-h-chandler.html"], ["1921/05/28/from-lorie-to-e-h-chandler/index.html", "/posts/1921/05/28/from-lorie-to-e-h-chandler.html"], ["1921/05/30/from-william-thomas-knox-to-jeanette-knox-chandler/index.html", "/posts/1921/05/30/from-william-thomas-knox-to-jeanette-knox-chandler.html"], ["1920/04/20/from-unknown-to-john-w-roush/index.html", "/posts/1920/04/20/from-unknown-to-john-w-roush.html"], ["1920/04/22/from-state-of-illinois-department-of-public-welfare-to-jeanette-knox-chandler/index.html", "/posts/1920/04/22/from-state-of-illinois-department-of-public-welfare-to-jeanette-knox-chandler.html"], ["1920/10/21/from-jacksonville-state-hospital-to-jeanette-knox-chandler/index.html", "/posts/1920/10/21/from-jacksonville-state-hospital-to-jeanette-knox-chandler.html"], ["1920/12/16/from-jacksonville-state-hospital-to-elijah-h-chandler/index.html", "/posts/1920/12/16/from-jacksonville-state-hospital-to-elijah-h-chandler.html"], ["1919/06/06/from-lorin-to-martin-chandler/index.html", "/posts/1919/06/06/from-lorin-to-martin-chandler.html"], ["1919/05/11/from-martin-chandler-to-jeanette-knox-chandler/index.html", "/posts/1919/05/11/from-martin-chandler-to-jeanette-knox-chandler.html"], ["1919/04/07/from-martin-chandler-to-elijah-h-chandler-3/index.html", "/posts/1919/04/07/from-martin-chandler-to-elijah-h-chandler-3.html"], ["1919/04/03/from-martin-chandler-to-lorin-grace-and-audrey/index.html", "/posts/1919/04/03/from-martin-chandler-to-lorin-grace-and-audrey.html"], ["1925/02/07/from-russ-f-souers-to-lucerne-chandler/index.html", "/posts/1925/02/07/from-russ-f-souers-to-lucerne-chandler.html"], ["1922/11/30/from-martin-chandler-to-elijah-h-chandler-5/index.html", "/posts/1922/11/30/from-martin-chandler-to-elijah-h-chandler-5.html"], ["1919/05/03/from-martin-chandler-to-elijah-h-chandler-and-family-21/index.html", "/posts/1919/05/03/from-martin-chandler-to-elijah-h-chandler-and-family-21.html"], ["1919/12/27/from-martin-chandler-to-elijah-h-chandler-15/index.html", "/posts/1919/12/27/from-martin-chandler-to-elijah-h-chandler-15.html"], ["1919/10/28/from-vinnie-to-jeanette-knox-chandler-qaz/index.html", "/posts/1919/10/28/from-vinnie-to-jeanette-knox-chandler-qaz.html"], ["1919/10/02/from-william-thomas-knox-to-jeanette-knox-chandler-2/index.html", "/posts/1919/10/02/from-william-thomas-knox-to-jeanette-knox-chandler-2.html"], ["1920/07/05/from-william-thomas-knox-to-jeanette-knox-chandler-and-family/index.html", "/posts/1920/07/05/from-william-thomas-knox-to-jeanette-knox-chandler-and-family.html"], ["1927/12/21/from-lucile-to-jeanette-knox-chandler/index.html", "/posts/1927/12/21/from-lucile-to-jeanette-knox-chandler.html"], ["1927/11/15/from-craig-and-carmen-ramsay-to-sam-mulholland/index.html", "/posts/1927/11/15/from-craig-and-carmen-ramsay-to-sam-mulholland.html"], ["1929/02/05/from-grace-chandler-to-jeanette-knox-chandler/index.html", "/posts/1929/02/05/from-grace-chandler-to-jeanette-knox-chandler.html"], ["1927/11/21/from-ruby-chandler-mullholland-to-jeanette-knox-chandler-2/index.html", "/posts/1927/11/21/from-ruby-chandler-mullholland-to-jeanette-knox-chandler-2.html"], ["1927/12/23/from-a-c-holloway-to-jeanette-knox-chandler/index.html", "/posts/1927/12/23/from-a-c-holloway-to-jeanette-knox-chandler.html"], ["1930/12/04/from-jerry-to-jeanette-knox-chandler/index.html", "/posts/1930/12/04/from-jerry-to-jeanette-knox-chandler.html"], ["1930/11/06/from-verg-forkmen-to-jeanette-knox-chandler/index.html", "/posts/1930/11/06/from-verg-forkmen-to-jeanette-knox-chandler.html"], ["1927/12/22/from-n-d-mcevers-to-jeanette-knox-chandler/index.html", "/posts/1927/12/22/from-n-d-mcevers-to-jeanette-knox-chandler.html"], ["1929/02/25/from-bess-chandler-roush-to-jeanette-knox-chandler/index.html", "/posts/1929/02/25/from-bess-chandler-roush-to-jeanette-knox-chandler.html"], ["1930/12/22/from-paul-knox-and-family-to-jeanette-knox-chandler/index.html", "/posts/1930/12/22/from-paul-knox-and-family-to-jeanette-knox-chandler.html"], ["1928/06/20/from-springfield-life-insurance-company-to-jeanette-knox-chandler/index.html", "/posts/1928/06/20/from-springfield-life-insurance-company-to-jeanette-knox-chandler.html"], ["1927/12/22/from-paul-knox-and-family-to-jeanette-knox-chandler-2/index.html", "/posts/1927/12/22/from-paul-knox-and-family-to-jeanette-knox-chandler-2.html"], ["1930/12/26/from-ruby-chandler-mullholland-to-jeanette-knox-chandler-3/index.html", "/posts/1930/12/26/from-ruby-chandler-mullholland-to-jeanette-knox-chandler-3.html"], ["1930/08/28/from-grace-chandler-to-jeanette-knox-chandler-4/index.html", "/posts/1930/08/28/from-grace-chandler-to-jeanette-knox-chandler-4.html"], ["1927/11/19/from-hall-of-pleasant-view-lodge-to-jeanette-knox-chandler-and-family/index.html", "/posts/1927/11/19/from-hall-of-pleasant-view-lodge-to-jeanette-knox-chandler-and-family.html"], ["1927/12/25/from-joe-maynard-to-chandler-family/index.html", "/posts/1927/12/25/from-joe-maynard-to-chandler-family.html"], ["1927/11/17/from-rosa-and-fred-to-john-roush/index.html", "/posts/1927/11/17/from-rosa-and-fred-to-john-roush.html"], ["1929/02/19/from-knox-to-jeanette-knox-chandler/index.html", "/posts/1929/02/19/from-knox-to-jeanette-knox-chandler.html"], ["1927/06/02/from-n-j-knox-to-jeanette-knox-chandler/index.html", "/posts/1927/06/02/from-n-j-knox-to-jeanette-knox-chandler.html"], ["1927/01/01/from-anna-chandler-to-jeanette-knox-chandler-2/index.html", "/posts/1927/01/01/from-anna-chandler-to-jeanette-knox-chandler-2.html"], ["1962/07/27/from-rurt-to-ruby-chandler/index.html", "/posts/1962/07/27/from-rurt-to-ruby-chandler.html"], ["1930/12/31/from-ruby-chandler-mullholland-to-jeanette-knox-chandler/index.html", "/posts/1930/12/31/from-ruby-chandler-mullholland-to-jeanette-knox-chandler.html"], ["1932/11/01/from-inez-and-grover-to-jeanette-knox-chandler/index.html", "/posts/1932/11/01/from-inez-and-grover-to-jeanette-knox-chandler.html"], ["2014/07/03/from-elijah-h-chandler-to-jeanette-knox-chandler-7/index.html", "/posts/2014/07/03/from-elijah-h-chandler-to-jeanette-knox-chandler-7.html"], ["2015/01/14/from-martin-chandler-to-elijah-h-chandler-and-family-54/index.html", "/posts/2015/01/14/from-martin-chandler-to-elijah-h-chandler-and-family-54.html"], ["2015/02/21/from-david-knox-to-jeanette-knox-chandler-and-family/index.html", "/posts/2015/02/21/from-david-knox-to-jeanette-knox-chandler-and-family.html"], ["1937/12/06/from-lucy-clarkin-to-amelia-j-wiggins/index.html", "/posts/1937/12/06/from-lucy-clarkin-to-amelia-j-wiggins.html"], ["1935/08/16/from-lucy-clarkin/index.html", "/posts/1935/08/16/from-lucy-clarkin.html"], ["1938/01/18/from-lucy-clarkin-to-amelia-j-wiggins-2/index.html", "/posts/1938/01/18/from-lucy-clarkin-to-amelia-j-wiggins-2.html"], ["1938/05/21/from-lucy-clarkin-to-amelia-j-wiggins-3/index.html", "/posts/1938/05/21/from-lucy-clarkin-to-amelia-j-wiggins-3.html"], ["1941/06/30/from-betty-tilley-to-amelua-j-wiggins/index.html", "/posts/1941/06/30/from-betty-tilley-to-amelua-j-wiggins.html"], ["1936/04/14/from-lucila-to-amelia-j-wiggins/index.html", "/posts/1936/04/14/from-lucila-to-amelia-j-wiggins.html"], ["1938/07/31/from-betty-to-amelia-j-wiggins/index.html", "/posts/1938/07/31/from-betty-to-amelia-j-wiggins.html"], ["1942/02/24/from-betty-to-amelia-j-wiggins-2/index.html", "/posts/1942/02/24/from-betty-to-amelia-j-wiggins-2.html"], ["1937/01/01/from-mattie-caraher-to-amelia-j-wiggins/index.html", "/posts/1937/01/01/from-mattie-caraher-to-amelia-j-wiggins.html"], ["1941/07/04/from-amelia-j-wiggins-to-betty-ann-tilley/index.html", "/posts/1941/07/04/from-amelia-j-wiggins-to-betty-ann-tilley.html"], ["1971/01/31/from-luila-to-unknown/index.html", "/posts/1971/01/31/from-luila-to-unknown.html"]]

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete --delete-after output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete --delete-after output/ joe@my.site:/srv/www/site",
#     ]
# }

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []

# Use a thumbnail (defined by ".. previewimage:" in the gallery's index) in
# list of galleries for each gallery
GALLERIES_USE_THUMBNAIL = False

# Image to use as thumbnail for those galleries that don't have one
# None: show a grey square
# '/url/to/file': show the image in that url
GALLERIES_DEFAULT_THUMBNAIL = None

# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# If set to True, any ICC profile will be copied when an image is thumbnailed or
# resized.
# PRESERVE_ICC_PROFILES = False

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).
# Panoramas (aspect ratio over 3:1) get 4x larger thumbnails due to scaling issues.

IMAGE_FOLDERS = {'images': 'images'}
IMAGE_THUMBNAIL_SIZE = 400
# IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False
#
# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
# SHOW_INDEX_PAGE_NAVIGATION = False

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
# META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Set to None to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
#
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# If you need to use the literal braces '{' and '}' in your footer text, use
# '{{' and '}}' to escape them (str.format is used)
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, intensedebate, isso, muut, commento, utterances
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = ''
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
## COMMENT_SYSTEM_ID = "nikolademo"

# Create index.html for page folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the PAGE_INDEX
#          will not be generated for that directory.
# PAGE_INDEX = False
# Enable comments on pages (i.e. not posts)?
# COMMENTS_IN_PAGES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
STRIP_INDEXES = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: https://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts (not pages!) by default
# SCHEDULE_ALL = False

# Do you want to add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Want to use KaTeX instead of MathJax? While KaTeX may not support every
# feature yet, it's faster and the output looks better.
# USE_KATEX = False

# KaTeX auto-render settings. If you want support for the $.$ syntax (which may
# conflict with running text!), just use this config:
# KATEX_AUTO_RENDER = """
# delimiters: [
#     {left: "$$", right: "$$", display: true},
#     {left: "\\\\[", right: "\\\\]", display: true},
#     {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
#     {left: "$", right: "$", display: false},
#     {left: "\\\\(", right: "\\\\)", display: false}
# ]
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter': {'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# Defaults are markdown.extensions.(fenced_code|codehilite|extra)
# markdown.extensions.meta is required for Markdown metadata.
MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Options to be passed to markdown extensions (See https://python-markdown.github.io/reference/)
# Default is {} (no config at all)
# MARKDOWN_EXTENSION_CONFIGS = {}


# Extra options to pass to the pandoc command, empty by default.
# It can be a list of strings or a dict (keys are file extensions).
# Example for a list of strings (used for all extensions):
# PANDOC_OPTIONS = ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# Example for a dict, where the keys are the extensions in COMPILERS['pandoc']:
# COMPILERS['pandoc'] = ['.rst', '.md', '.txt']
# PANDOC_OPTIONS = {
#     '.rst': ['-t', 'rst'],
#     '.md': ['-t', 'markdown'],
#     '.txt': ['-t', 'markdown-raw_html'],
# }
# Pandoc does not demote headers by default.  To enable this, you can use, for example
# ['--base-header-level=2']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="https://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# FEED_TEASER option. FEED_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# Only include teasers in Atom and RSS feeds. Disabling include the full
# content. Defaults to True.
# FEED_TEASERS = True

# Strip HTML from Atom and RSS feed summaries and content. Defaults to False.
# FEED_PLAIN = False

# Number of posts in Atom and RSS feeds.
# FEED_LENGTH = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="https://duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '.*\/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.rst'
# (Note the '.*\/' in the beginning -- matches source paths relative to conf.py)
# FILE_METADATA_REGEXP = None

# Should titles fetched from file metadata be unslugified (made prettier?)
# FILE_METADATA_UNSLUGIFY_TITLES = True

# If enabled, extract metadata from docinfo fields in reST documents.
# If your text files start with a level 1 heading, it will be treated as the
# document title and will be removed from the text.
# USE_REST_DOCINFO_METADATA = False

# If enabled, hide docinfo fields in reST document output
# HIDE_REST_DOCINFO = False

# Map metadata from other formats to Nikola names.
# Supported formats: yaml, toml, rest_docinfo, markdown_metadata
# METADATA_MAPPING = {}
#
# Example for Pelican compatibility:
# METADATA_MAPPING = {
#     "rest_docinfo": {"summary": "description", "modified": "updated"},
#     "markdown_metadata": {"summary": "description", "modified": "updated"}
# }
# Other examples: https://getnikola.com/handbook.html#mapping-metadata-from-other-formats

# Map metadata between types/values. (Runs after METADATA_MAPPING.)
# Supported formats: nikola, yaml, toml, rest_docinfo, markdown_metadata
# The value on the right should be a dict of callables.
# METADATA_VALUE_MAPPING = {}
# Examples:
# METADATA_VALUE_MAPPING = {
#     "yaml": {"keywords": lambda value: ', '.join(value)},  # yaml: 'keywords' list -> str
#     "nikola": {
#         "widgets": lambda value: value.split(', '),  # nikola: 'widgets' comma-separated string -> list
#         "tags": str.lower  # nikola: force lowercase 'tags' (input would be string)
#      }
# }

# Add any post types here that you want to be displayed without a title.
# If your theme supports it, the titles will not be shown.
# TYPES_TO_HIDE_TITLE = []

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# Bundle JS and CSS into single files to make site loading faster in a HTTP/1.1
# environment but is not recommended for HTTP/2.0 when caching is used.
# Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Special settings to disable only parts of the indexes plugin.
# Use with care.
# DISABLE_INDEXES = False
# DISABLE_MAIN_ATOM_FEED = False
# DISABLE_MAIN_RSS_FEED = False

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Add the absolute paths to directories containing themes to use them.
# For example, the `v7` directory of your clone of the Nikola themes
# repository.
# EXTRA_THEMES_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = False

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
