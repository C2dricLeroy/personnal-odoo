from odoo import http
from odoo.http import request


class CelerWebsite(http.Controller):

    @http.route("/", type="http", auth="public", website=True)
    def home(self):
        return request.render("celer_website.homepage")
