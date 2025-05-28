from odoo import fields, models

class Guardian(models.Model):
    _name = "student.guardian"
    _description = "Guardian information"

    guardian_name = fields.Char(string = "Guardian Name", required = True)
    guardian_number = fields.Integer(string = "Number ")
    relation = fields.Selection([('father','Father'),
                                 ('mother','Mother'),
                                 ('other','Other')], string = "Relationship", required = True)
    student = fields.One2many('student.information','guardian_id', string = "Child")