# -*- coding: utf-8 -*-
#


{
    'name': 'Rocker Timesheet',
    'summary': 'hr_timesheet supercharged',
    'description': 'Probably most fastes way to report work done',
    'author': 'Antti Kärki',
    'license': 'AGPL-3',
    'version': '14.0.1.0',
    'category': 'Generic Modules/Human Resources',
    'sequence': 23,
    'website': '',
    'depends': ['base', 'project', 'hr_timesheet'],
    'data': [
        'security/rocker_timesheet_security.xml',
        'security/ir.model.access.csv',
        'views/rocker_template.xml',
        'views/rocker_timesheet_views.xml',
        'views/rocker_timesheet_about.xml',
        # 'data/rocker_timesheet_data.xml',
    ],
    # 'demo': [
    #     # 'data/rocker_timesheet_demo.xml',
    # ],
    'qweb': ['static/src/xml/rocker_button.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screenshot.gif'],

}
