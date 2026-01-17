from odoo import http
from odoo.http import request


class CelerWebsite(http.Controller):

    @http.route("/", type="http", auth="public", website=True)
    def home(self):
        return request.render("celer_website.homepage")

    @http.route("/about", type="http", auth="public", website=True)
    def about(self):
        return request.render("celer_website.about")

    @http.route("/services", type="http", auth="public", website=True)
    def services(self):
        return request.render("celer_website.services")

    @http.route("/contact", type="http", auth="public", website=True)
    def contact(self):
        return request.render("celer_website.contact")

    @http.route("/blog", type="http", auth="public", website=True)
    def blog(self):
        return request.render("celer_website.blog")

