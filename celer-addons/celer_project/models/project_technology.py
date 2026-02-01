from odoo import models, fields


class ProjectTechnology(models.Model):
    _name = "project.technology"
    _description = "Technology / Skill"
    _order = "sequence, name"

    name = fields.Char(string="Name", required=True, translate=True)
    sequence = fields.Integer(default=10)

    image = fields.Image(string="Logo", max_width=192, max_height=192)

    website_url = fields.Char(string="Official website")
    description = fields.Text(string="Description", translate=True)

    category_type = fields.Selection(
        [
            ("language", "Language"),
            ("framework", "Framework"),
            ("database", "Database"),
            ("devops", "DevOps / Infra"),
            ("tool", "Tools"),
            ("other", "Other"),
        ],
        string="Category",
        default="other",
    )

    color = fields.Integer(string="Color")
