# -*- coding: utf-8 -*-
{
    'name': "Website Landing Page",

    'summary': """
        Remove standard menu and footer from a web page
        allowing landing page to be insulated """,

    'description': """
    """,

    'author': "Alberto Carollo",
    'website': "https://github.com/baba75",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
               'website',
               ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}