from odoo import http
from odoo.http import request


class ProjectController(http.Controller):

    @http.route("/celer-projects", type="http", auth="public", website=True)
    def list_projects(self):
        projects = (
            request.env["project.project"]
            .sudo()
            .search([("is_website_visible", "=", True)])
        )
        return request.render("celer_website.services", {"projects": projects})
