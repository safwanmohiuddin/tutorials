# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.information'
    _description = 'Student Information Details '

    name = fields.Char(string ="Full Name", required = True)
    student_id = fields.Integer(string = "ID Number", required = True )
    age = fields.Integer(string = "Age")
    date_of_birth = fields.Date(string = "Date of Birth")
    guardian_id = fields.Many2one('student.guardian', string = 'Guardian')
    course_id = fields.Many2many('student.course', string = 'Courses enrolled')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

