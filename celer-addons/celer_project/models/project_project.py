from odoo import models, fields


class Project(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    technology_ids = fields.Many2many("project.technology", string="Technologies used")

    short_description = fields.Text("Hook")

    website_description = fields.Html(
        "Project details",
    )

    website_published = fields.Boolean("Visible on current website")

    client_comment = fields.Text("Client Comment")

    cover_image = fields.Binary("Cover Image (Website)")

    live_url = fields.Char("Link to the live website")

    def action_open_live_url(self):
        self.ensure_one()
        if not self.live_url:
            return False

        return {
            "type": "ir.actions.act_url",
            "url": self.live_url,
            "target": "new",
        }

    def _compute_website_url(self):
        for project in self:
            project.website_url = f"/projects/{self.env['ir.http']._slug(project)}"
