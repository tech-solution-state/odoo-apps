# -*- encoding: utf-8 -*-
{
    'name': "Serial Number on List View",
    'summary': 'Displaying Serial Number on List View.',
    'description': """By installing this module, user can see serial number in every list view. numbering list, sequential number in list, row number in list, numberring tree, sequential number in tree, row number in tree, auto numbering in tree/list""",
    'version': '14.0.0.1',
    'category': 'Other',
    'license': 'LGPL-3',
    'author': 'Tech Solution State',
    'website': 'https://techsolutionstate.com',
    'maintainer': 'Tech Solution State',
    "depends": ['web'],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [],
    "images": ["static/description/numbering_list_tss-banner.png"],
    'installable': True,
    'application': True,
    'auto_install': False,
}
