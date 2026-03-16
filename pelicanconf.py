#!/usr/bin/env python

import os
import sys
sys.path.append(".")
from integrantes import INTEGRANTES

AUTHOR = "Python Chile"
SITENAME = "Comunidad Chilena de Python"
SITESUBTITLE = "Lugar de encuentro de todas las personas entusiastas de Python a lo largo de Chile"
DESCRIPTION = (
    "Nuestro objetivo es ser el lugar de encuentro de todos los entusiastas de Python "
    "a lo largo del país, fortaleciendo a los miembros de la comunidad para generar un impacto "
    "positivo en el desarrollo de Python a nivel nacional y mundial."
)

SITEURL = ""
PATH = "content"
TIMEZONE = "America/Santiago"
DEFAULT_LANG = "es"
THEME = os.path.join(os.path.dirname(__file__), "pycltheme")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = { "es": "%d-%m-%Y"}

MENUELEMENTS = {
    "home": {"title": "Home", "url": "index.html", "children": None},
    "blog": {"title": "Blog", "url": "archives.html", "children": None},
    "coc": {
        "title": "Código de Conducta",
        "url": "pages/codigo-de-conducta.html",
        "children": None,
    },
    "Organización": {
        "title": "Organización",
        "children": {
            "corporación": {"title": "Corporación", "url": "pages/corporacion.html"},
            "coordinación": {"title": "Coordinación", "url": "pages/coordinacion.html"},
        }
    },
    "grupos": {"title": "Grupos", "url": "pages/grupos.html"},
    "eventos": {
        "title": "Eventos",
        "url": "pages/eventos.html",
        "children": None,
    },
    "recursos": {
        "title": "Recursos",
        "url": "pages/recursos.html",
        "children": None,
    },
    "videos": {
        "title": "Videos",
        "url": "pages/videos.html",
        "children": None,
    },
}

# Social widget
PLATAFORMAS = {
    "discord": {
        "alt": "Discord",
        "icon": "fa-discord",
        "url": "https://discord.gg/dTHMfJvauS"
    },
    "telegram": {
        "alt": "Telegram",
        "icon": "fa-telegram",
        "url": "https://t.me/pythonchile"
    },
}

REDES = {
    "facebook": {
        "alt": "Facebook",
        "icon": "fa-facebook-f",
        "url": "https://www.facebook.com/groups/pythonchiledev/",
    },
    "twitter": {
        "alt": "Twitter",
        "icon": "fa-x-twitter",
        "url": "https://x.com/pythonchiledev",
    },
    "instagram": {
        "alt": "Instagram",
        "icon": "fa-instagram",
        "url": "https://instagram.com/pythonchiledev",
    },
    "github": {
        "alt": "Github",
        "icon": "fa-github",
        "url": "https://github.com/python-chile"
    },
    "linkedin": {
        "alt": "LinkedIn",
        "icon": "fa-linkedin",
        "url": "https://www.linkedin.com/groups/4929519/",
    },
    "youtube": {
        "alt": "YouTube",
        "icon": "fa-youtube",
        "url": "https://www.youtube.com/c/PythonChile",
    },
    "meetup": {
        "alt": "Meetup",
        "icon": "fa-meetup",
        "url": "https://meetup.com/es/pythonchile",
    },
}

PLUGINS = ["pelican.plugins.image_process"]

IMAGE_PROCESS = {
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 300px, "
            "90vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
