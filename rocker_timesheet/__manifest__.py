# -*- coding: utf-8 -*-
#
#############################################################################
#
#    Copyright (C) 2021-Antti Kärki.
#    Author: Antti Kärki.
#    email: antti.rocker.karki@outlook.com

#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#
# 21-01-2026
#
#############################################################################
#ToDo_

{
    'name': 'Rocker Timesheet',
    'summary': 'hr_timesheet supercharged',
    'description': 'Probably most fastest way to report work done',
    'author': 'Antti Kärki',
    'license': 'OPL-1',
    'price': 10.00,
    'currency': 'EUR',
    'version': '19.0.1.0',
    'category': 'Rocker/Timesheet',
    'sequence': 23,
    'website': '',
    'depends': ['base', 'project', 'hr_timesheet', 'hr_holidays'],
    'data': [
        'security/rocker_timesheet_security.xml',
        'security/ir.model.access.csv',
        'views/rocker_timesheet_views.xml',
        'views/rocker_timesheet_about.xml',
        'views/rocker_holidays.xml',
        'views/rocker_leave_type.xml',
        'report/rocker_timesheet_report_view.xml',
        'views/rocker_timesheet_menu.xml',

    ],
   'assets': {
        'web.assets_backend': [
           'rocker_timesheet/static/src/views/calendar/*.xml',
            'rocker_timesheet/static/src/views/calendar/*.js',
            'rocker_timesheet/static/src/views/list/*.xml',
            'rocker_timesheet/static/src/views/list/*.js',
            'rocker_timesheet/static/src/views/calendar/*.scss',
            'rocker_timesheet/static/src/css/*.scss',

        ]
   },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screenshot.gif'],

}
