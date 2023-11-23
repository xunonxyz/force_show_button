# -*- coding: utf-8 -*-
{
    'name': "force_show_button",

    'summary': """
        force show header button for odoo
    """,

    'description': """
        Button template for odoo
    """,

    'author': "crax",
    'website': "https://odoo.openerpnext.com",

    'category': 'Apps/Extra Tools',
    'version': '16.0.0.1',

    'depends': ['base', 'web'],
    'data': [],

    'assets': {
        'web.assets_backend': [
            'force_show_button/static/src/list_button/list_button.xml'
        ]
    }
}
