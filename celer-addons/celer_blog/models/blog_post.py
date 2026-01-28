# models/blog_post.py
from odoo import models, fields, api
import math
import re

class BlogPost(models.Model):
    _inherit = "blog.post"

    reading_time = fields.Integer(
        string="Reading time (min)",
        compute="_compute_reading_time",
        store=True
    )

    @api.depends("content")
    def _compute_reading_time(self):
        for post in self:
            if not post.content:
                post.reading_time = 1
                continue

            text = re.sub('<[^<]+?>', '', post.content)
            word_count = len(text.split())
            post.reading_time = max(1, math.ceil(word_count / 200))
