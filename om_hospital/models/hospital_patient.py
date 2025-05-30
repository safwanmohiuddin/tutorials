from odoo import api, fields, models #keep 2 lines empty after this

class HospitalPatient(models.Model):
    _name = "hospital.patient" #Name should have .
    _description = "Patient Master"

    name = fields.Char(string = "Name", required = True)
    date_of_birth = fields.Date(string = "Date of Birth")
    gender = fields.Selection([('male', 'Male'), ('female','Female'),], string = "Gender")