# -*- coding: utf-8 -*-
{
    "name": "Celer App",
    "version": "19.0.1.0.0",
    "summary": "Custom features for Celer",
    "description": """
Celer App
=========

Custom Odoo module developed for Celer.
""",
    "author": "Celer",
    "website": "https://example.com",
    "category": "Custom",
    "license": "LGPL-3",

    "depends": [
        "base",
        "web",
        "mail",
        "contacts",
        "calendar",
        "auth_signup",
        "sale",
        "project",
        "celer_website",
        "celer_base",
        "celer_data",
    ],
    "data": [
    ],
    "post_init_hook": "post_init_hook",
    "demo": [
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
