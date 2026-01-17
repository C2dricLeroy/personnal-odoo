from odoo import models, fields

class CelerContact(models.Model):
    _name = 'celer.contact'
    _description = 'Contact Form Message'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email', required=True)
    message = fields.Text('Message', required=True)
    create_date = fields.Datetime('Created on', readonly=True)
    company = fields.Char('Company')
    service = fields.Char('Service')
    phone = fields.Char('Phone')