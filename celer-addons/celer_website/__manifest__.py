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
        "views/layout.xml",
        "views/pages/homepage.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "celer_website/static/src/css/tailwind.css",
            "celer_website/static/src/css/tailwind.out.css",
        ],
    },
    "installable": True,
    "application": False,
}
