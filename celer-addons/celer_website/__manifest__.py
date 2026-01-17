{
    "name": "Celer Website",
    "summary": "Celer website",
    "version": "1.0.0",
    "category": "Website",
    "author": "Cédric Leroy",
    "depends": [
        "website",
    ],
    "data": [
        "views/components/header.xml",
        "views/components/footer.xml",
        "views/components/hero.xml",
        "views/components/service_preview.xml",
        "views/components/call_to_action.xml",
        "views/components/development.xml",
        "views/layout.xml",
        "views/pages/homepage.xml",
        "views/pages/about.xml",
        "views/pages/services.xml",
        "views/pages/contact.xml",
        "views/pages/blog.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "celer_website/static/src/css/main.css",
            "celer_website/static/src/css/tailwind.css",
            "celer_website/static/src/css/tailwind.out.css",
        ],
    },
    "installable": True,
    "application": False,
}
