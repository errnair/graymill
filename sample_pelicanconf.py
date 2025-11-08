#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ==============================================================================
# GRAYMILL THEME - CONFIGURATION GUIDE
# ==============================================================================
#
# This is a sample configuration file for the Graymill Pelican theme.
# All theme variables are categorized as REQUIRED or OPTIONAL below.
#
# REQUIRED VARIABLES (must be set):
#   - AUTHOR
#   - SITENAME
#   - SITEURL
#   - DEFAULT_LANG
#
# OPTIONAL VARIABLES (have safe defaults if not set):
#   - FAVICON (no favicon if not set)
#   - AVATAR (no schema.org image if not set)
#   - AUTHOR_DESCRIPTION (empty if not set)
#   - SITEDESCRIPTION (empty if not set)
#   - TWITTER_USERNAME (Twitter meta tags omitted if not set)
#   - SITE_IMAGE (no default Open Graph image if not set)
#   - AUTHOREMAIL (shows AUTHOR name instead if not set)
#   - GOOGLE_ANALYTICS (no analytics if not set)
#   - SPREAD_THE_WORD (defaults to True if not set)
#
# NEW FEATURES IN v2.x:
#   - Multiple authors support (use "Authors:" in article metadata)
#   - Modified date display (use "Modified:" in article metadata)
#   - Draft indicators (use "Status: draft" in article metadata)
#   - Translation links (multilingual articles)
#   - Per-category/tag/author RSS feeds
#   - Enhanced SEO with JSON-LD structured data
#   - Open Graph article-specific properties
#
# ==============================================================================
# BASIC SITE INFORMATION
# ==============================================================================

AUTHOR = 'Your Name'
AUTHOREMAIL = 'your.email@example.com'  # Optional: displays in article footer
SITENAME = 'Your Site Name'
SITEURL = 'http://localhost:8000'  # Change to your domain for production
SITEDESCRIPTION = 'Your site tagline or description'

PATH = 'content'
TIMEZONE = 'America/New_York'  # Change to your timezone
DEFAULT_LANG = 'en'

# ==============================================================================
# THEME CONFIGURATION
# ==============================================================================

THEME = 'graymill'  # or 'path/to/graymill' if using absolute path

# Theme-specific: Default image for social sharing (og:image, twitter:image)
# This image will be used when no article-specific image is set
# Path relative to content directory
SITE_IMAGE = 'images/default-share-image.jpg'  # Recommended size: 1200x630px

# Favicon (path relative to content directory)
FAVICON = 'images/favicon.png'

# Avatar/Profile image for schema.org Person markup
AVATAR = 'images/avatar.jpg'

# Author bio/description for schema.org and meta tags
AUTHOR_DESCRIPTION = 'Brief bio or description about the author'

# ==============================================================================
# SOCIAL MEDIA LINKS
# ==============================================================================

# Social media icons displayed in sidebar
# Available icons: twitter, facebook, github, linkedin, mail, rss
# Note: Google+ removed (service defunct as of April 2019)
SOCIAL = (
    ('twitter', 'https://twitter.com/yourusername'),
    ('github', 'https://github.com/yourusername'),
    ('linkedin', 'https://www.linkedin.com/in/yourusername'),
    ('facebook', 'https://facebook.com/yourusername'),
    ('mail', 'mailto:your.email@example.com'),
)

# Twitter username for twitter:site and twitter:creator meta tags
TWITTER_USERNAME = '@yourusername'

# ==============================================================================
# NAVIGATION & MENU
# ==============================================================================

# Display pages (About, Contact, etc.) in menu
DISPLAY_PAGES_ON_MENU = True

# Display categories in sidebar menu
DISPLAY_CATEGORIES_ON_MENU = True

# Custom menu items (tuples of title and URL)
MENUITEMS = (
    ('Home', '/'),
    ('Archives', '/archives.html'),
)

# ==============================================================================
# CONTENT DISPLAY
# ==============================================================================

# Show article summaries on index page
DISPLAY_SUMMARY = True

# Number of articles per page
DEFAULT_PAGINATION = 8

# Show social sharing buttons on article pages
# Set to False to hide "spread the word" section
SPREAD_THE_WORD = True  # Default: True if not set

# ==============================================================================
# RSS/ATOM FEEDS
# ==============================================================================

# Feed generation (set to None/False for local development)
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Per-category feeds (NEW: automatically linked in category pages)
CATEGORY_FEED_ATOM = 'feeds/{slug}.category.atom.xml'

# Per-tag feeds (NEW: automatically linked in tag pages)
TAG_FEED_ATOM = 'feeds/{slug}.tag.atom.xml'

# Per-author feeds (NEW: automatically linked in author pages)
AUTHOR_FEED_ATOM = 'feeds/{slug}.author.atom.xml'
AUTHOR_FEED_RSS = None

# Translation feeds (usually not needed)
TRANSLATION_FEED_ATOM = None

# For local development, disable all feeds
# FEED_ALL_ATOM = None
# FEED_ALL_RSS = None
# CATEGORY_FEED_ATOM = None
# TAG_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None

# ==============================================================================
# ANALYTICS
# ==============================================================================

# Google Analytics 4 Measurement ID
# Format: G-XXXXXXXXXX (NOT the old UA-XXXXXXXXX format)
# Leave empty or comment out to disable analytics
GOOGLE_ANALYTICS = ''  # Example: 'G-ABC123XYZ'

# ==============================================================================
# STATIC FILES
# ==============================================================================

# Paths to copy from content to output (relative to content directory)
STATIC_PATHS = [
    'images',
    'extras',
    # 'pdfs',  # Uncomment if you have PDFs
]

# Map extra files to specific output paths
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

# ==============================================================================
# URLS
# ==============================================================================

# Article URL structure
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# Page URL structure
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Category, tag, author URLs
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

# ==============================================================================
# PLUGINS (Optional)
# ==============================================================================

# Uncomment and configure if using plugins
# PLUGIN_PATHS = ['path/to/pelican-plugins']
# PLUGINS = []

# ==============================================================================
# ADVANCED OPTIONS
# ==============================================================================

# Uncomment for development to see more verbose output
# DEBUG = True
# LOG_FILTER = []

# Article metadata
DEFAULT_METADATA = {
    'status': 'draft',  # Articles are drafts by default
}

# Links widget (blogroll)
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
)

# ==============================================================================
# ARTICLE METADATA GUIDE
# ==============================================================================
#
# The theme supports the following article metadata fields:
#
# BASIC METADATA:
# ---------------
# Title: My Article Title
# Date: 2025-01-01 12:00
# Category: Technology
# Tags: python, pelican, web
# Slug: my-article-slug
# Authors: John Doe, Jane Smith    # NEW: Multiple authors support
# Modified: 2025-01-15 14:30       # NEW: Show last updated date
# Status: draft                    # NEW: Draft indicator (published by default)
#
# SOCIAL SHARING:
# ---------------
# Image: images/my-article-image.jpg    # Custom og:image (1200x630px recommended)
# Summary: Custom article summary here  # Override auto-generated summary
#
# TRANSLATIONS:
# -------------
# Lang: en
# Translation: yes
# Slug: my-article-slug-en  # Keep same slug for all translations
#
# EXAMPLE ARTICLE METADATA:
# -------------------------
# Title: Introduction to Pelican Static Sites
# Date: 2025-01-01 10:00
# Modified: 2025-01-15 14:30
# Authors: John Doe, Jane Smith
# Category: Web Development
# Tags: pelican, python, static-sites, tutorial
# Image: images/pelican-intro.jpg
# Summary: Learn how to build fast, secure static websites with Pelican
# Status: published
#
# NOTES:
# ------
# - If no Image is specified, SITE_IMAGE will be used as fallback
# - Single author uses "Author:", multiple use "Authors:" (comma-separated)
# - Modified date is optional, only shows if article was updated
# - Draft articles show a warning banner and have noindex meta tag
# - Translations link automatically if Lang and Slug match across articles
