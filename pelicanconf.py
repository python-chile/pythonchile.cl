#!/usr/bin/env python

AUTHOR = "Python Chile"
SITENAME = "Comunidad Chilena de Python"
SITESUBTITLE = "Lugar de encuentro de todas las personas entusiastas de Python a lo largo del país"
DESCRIPTION = (
    "Nuestro objetivo es ser el lugar de encuentro de todos los entusiastas de Python "
    "a lo largo del país, fortaleciendo a los miembros de la comunidad para generar un impacto "
    "positivo en el desarrollo de Python a nivel nacional y mundial."
)
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Santiago"

DEFAULT_LANG = "es"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUELEMENTS = {
    "home": {"title": "Home", "url": "#", "children": None},
    "blog": {"title": "Blog", "url": "#", "children": None},
    "coc": {
        "title": "Código de Conducta",
        "url": "pages/codigo-de-conducta.html",
        "children": None,
    },
    "comunidad": {
        "title": "Comunidad",
        "url": "#",
        "children": {
            "coordinación": {"title": "Coordinadores", "url": "#"},
            "grupos": {"title": "Grupos", "url": "#"},
            "eventos": {"title": "Eventos", "url": "#"},
        },
    },
}

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
REDES = {
    "discord": {"alt": "Discord", "icon": "fa-discord", "url": "https://discord.gg/dTHMfJvauS"},
    "telegram": {"alt": "Telegram", "icon": "fa-telegram", "url": "https://t.me/pythonchile"},
    "slack": {
        "alt": "Slack",
        "icon": "fa-slack",
        "url": "https://join.slack.com/t/python-chile/shared_invite/zt-3hitnkfk-I_CM~2ANuwofgARLZjI42A",
    },
    "facebook": {
        "alt": "Facebook",
        "icon": "fa-facebook-f",
        "url": "https://www.facebook.com/groups/pythonchileprogramadores/",
    },
    "twitter": {
        "alt": "Twitter",
        "icon": "fa-twitter",
        "url": "https://twitter.com/pythonchiledev",
    },
    "github": {"alt": "Github", "icon": "fa-github", "url": "https://github.com/python-chile"},
    "youtube": {
        "alt": "YouTube",
        "icon": "fa-youtube",
        "url": "https://www.youtube.com/c/PythonChile",
    },
    "linkedin": {
        "alt": "LinkedIn",
        "icon": "fa-linkedin",
        "url": "https://www.linkedin.com/groups/4929519/",
    },
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "pycltheme"
