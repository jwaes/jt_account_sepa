# -*- coding: utf-8 -*-
{
    'name': "jt_account_sepa",

    'summary': "Account sepa batch transfer grouping disable",

    'description': "Set BtchBookg to false by default",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['account_sepa'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_batch_payment_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
