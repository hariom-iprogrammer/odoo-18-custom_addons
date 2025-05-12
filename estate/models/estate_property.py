from odoo import models, fields
from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string='Garden Orientation'
    )
    state = fields.Selection([
    ('new', 'New'),
    ('offer_received', 'Offer Received'),
    ('offer_accepted', 'Offer Accepted'),
    ('sold', 'Sold'),
    ('cancelled', 'Cancelled')
], default='new', string='Status')
