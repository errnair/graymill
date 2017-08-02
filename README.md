## Graymin - A minimal Pelican theme.  
  
Graymin is a minimal, responsive theme for the [Pelican](http://blog.getpelican.com/) static site generator. It is based on the [Milligram CSS framework](http://milligram.io/).  

### Demo

See the theme in action at [muchBits](https://muchbits.com)

### Screenshots

*Coming Soon*

### Features

* Responsive (Mobile Friendly Test on [Google](https://search.google.com/test/mobile-friendly?utm_source=mft&utm_medium=redirect&utm_campaign=mft-redirect&id=TT7gCU77TVUWMMbu4pmHsg))
* Syntax highlighting for code blocks
* Google Analytics Support
* Easy to install
* Minimal/No Javascript (JS is only used in case Google Analytics is enabled).

## Installation

* Clone the repository - `git clone https://github.com/rn4ir/graymin.git`
* Create a `THEME` variable in your `pelicanconf.py` file and set its value to the location of ***graymin*** theme, like so:
```python
THEME = 'path/to/graymin'
```

## Custom Variables

The ***Graymin*** theme use the following settings in the `pelicanconf.py`:

### pelicanconf.py

#### Social Icons:
```python
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/username'),
          ('github', 'https://github.com/username'),
          ('twitter', 'https://twitter.com/username'),
          ('facebook', 'https://facebook.com/userid'),
          )
```

#### Pagination:
```python
DEFAULT_PAGINATION = 8
```

#### Home page parameters:

```python
SITEDESCRIPTION = 'snippets, how-tos and other tidbits'
DISPLAY_SUMMARY = True
DISPLAY_PAGES_ON_MENU = True
```

#### Other Settings
```python
FAVICON = 'images/favicon.png'
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
```

#### For local development:
```
SITEURL = 'http://localhost:8000'
```

### publishconf.py

When you are ready to publish your site add the following settings to `publishconf.py` file

```python
SITEURL = 'https://domain-name.tld'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

GOOGLE_ANALYTICS = ""
```

For more information on publishing your site, read the publishing [docs](http://docs.getpelican.com/en/3.6.3/publish.html)
