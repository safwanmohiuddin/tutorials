from odoo import fields, models, api

class Course(models.Model):
    _name = "student.course" #name should have . in between, table = school_course
    _description = "The information regarding the course work"
    _rec_name = 'course_name'
    #This is to show the name of the course in the top left corner
    #It is the Field name you want to show
    #if not used, will show table name instead

    course_name = fields.Char(string = "Course Name", required = True)
    #True needs to be capitalized
    #the attributed inside the fields need to be lowercase (string, required)
    course_ID = fields.Char(string = "ID ", required = True)
    credit_hours = fields.Integer(string = "Credit Hours", defaut=3)
    course_active = fields.Boolean(string = "Is Active? ", default = True)
    student = fields.Many2many('student.information', string = "Student")




