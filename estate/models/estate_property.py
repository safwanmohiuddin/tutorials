from odoo import models, fields, api


class DemoEstate(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Property Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Number of Bedrooms")
    living_area = fields.Integer(string="Living Area (sq ft)")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Garage")
    garden_area = fields.Integer(string="Garden Area (sq ft)")