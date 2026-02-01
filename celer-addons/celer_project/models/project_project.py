from odoo import models, fields


class Project(models.Model):
    _inherit = "project.project"

    technology_ids = fields.Many2many("project.technology", string="Technologies used")

    short_description = fields.Text("Hook")

    website_description = fields.Html(
        "Project details",
    )

    client_comment = fields.Text("Client Comment")

    cover_image = fields.Binary("Cover Image (Website)")

    live_url = fields.Char("Link to the live website")

    is_website_visible = fields.Boolean(
        string="Visible on website",
        default=False,
    )

    def action_open_live_url(self):
        self.ensure_one()
        if not self.live_url:
            return False

        return {
            "type": "ir.actions.act_url",
            "url": self.live_url,
            "target": "new",
        }
