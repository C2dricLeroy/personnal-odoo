from odoo import http
from odoo.http import request


class CelerWebsite(http.Controller):

    @http.route("/", type="http", auth="public", website=True)
    def home(self):
        return request.render("celer_website.homepage")

    @http.route("/about", type="http", auth="public", website=True)
    def about(self):
        return request.render("celer_website.about")

    @http.route("/contact_celer", type="http", auth="public", website=True)
    def contact(self):
        return request.render("celer_website.celer_contact")

    @http.route(
        "/contact/submit", type="http", auth="public", methods=["POST"], website=True
    )
    def contact_submit(self, **post):
        """
        post = {
            'name': '...',
            'email': '...',
            'message': '...'
        }
        """
        request.env["celer.contact"].sudo().create(
            {
                "name": post.get("name"),
                "email": post.get("email"),
                "message": post.get("message"),
            }
        )
        return request.redirect("/contact?submitted=1")
