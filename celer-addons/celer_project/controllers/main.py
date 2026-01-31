from odoo import http
from odoo.http import request


class ProjectController(http.Controller):

    @http.route("/projects", type="http", auth="public", website=True)
    def list_projects(self):
        projects = request.env["project.project"].search(
            [("website_published", "=", True)]
        )
        return request.render(
            "celer_project.project_list_template", {"projects": projects}
        )

    @http.route(
        '/projects/<model("project.project"):project>',
        type="http",
        auth="public",
        website=True,
    )
    def detail_projects(self, project):
        return request.render(
            "celer_project.project_detail_template", {"project": project}
        )
