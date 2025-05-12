from odoo import fields,models,api,

class CustomModel(models,model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')