# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': "test project",

    'description': "Test project for tutorial",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'license' : 'OPL-1',
   # 'category': "Uncategorized",
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

