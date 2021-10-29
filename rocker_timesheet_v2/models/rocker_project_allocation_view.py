# -*- coding: utf-8 -*-
#############################################################################
#
#    Copyright (C) 2021-Antti Kärki.
#    Author: Antti Kärki.
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class RockerProjectAllocationView(models.Model):
    _name = 'rocker.project.allocation.view'
    _auto = False
    _description = 'Project Allocation View'

    # @api.model
    # def _domain_project_id(self):
    #     domain = [('allow_timesheets', '=', True)]
    #     if not self.user_has_groups('hr_timesheet.group_timesheet_manager'):
    #         # work with Odoo 15 because view has user_id field
    #         return expression.AND([domain,
    #                                ['|', ('project_id.privacy_visibility', '!=', 'followers'), ('project_id.allowed_internal_user_ids', 'in', self.env.user.ids)]
    #                                ])
    #     return domain

    id = fields.Integer('id')
    # name = fields.Char('Name')
    company_id = fields.Many2one('res.company', string='Company')
    project_id = fields.Many2one('project.project', string='Project')
    resource_id = fields.Many2one('resource.resource', string='Resource')
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")

    @api.model
    def init(self):
        _logger.debug('Init: create view')
        # tools.drop_view_if_exists(self.env.cr, self._table)
        # self._cr.execute("""DROP VIEW IF EXISTS rocker_project_allocation_view """)
        self.env.cr.execute("""DROP VIEW IF EXISTS rocker_project_allocation_view """)
        self.env.cr.execute("""
CREATE OR REPLACE VIEW rocker_project_allocation_view as
select cast(ROW_NUMBER ()  OVER () as integer) as id, 
p1.company_id as company_id, 
p1.id as project_id, 
pa1.resource_id as resource_id, 
pa1.start_date as start_date, 
pa1.end_date as end_date
from project_project p1
LEFT OUTER JOIN rocker_project_allocation pa1 ON p1.id = pa1.project_id
                        """)

    @api.model
    def create(self, values):
        _logger.debug('view Create...')
        _logger.debug(values)
        # return vals
        # self.ensure_one()
        self.env['rocker.project.allocation'].create({
            'company_id': values['company_id'],
            'project_id': values['project_id'],
            'resource_id': values['resource_id'],
            'start_date': fields.Datetime.from_string(values['start_date']).date(),
            'end_date': fields.Datetime.from_string(values['end_date']).date(),
        })
        values = self.env['rocker.project.allocation.view'].search([
                ('company_id','=', values['company_id']),
                ('project_id','=', values['project_id']),
                ('resource_id','=', values['resource_id']),
                ('start_date','=', values['start_date']),
                ('end_date','=', values['end_date'])
                ], limit=1)

        return values
        # query where we are and then....
        # if _default_id:
        #     return {
        #         'name': 'Edit User defaults',
        #         'res_model':'rocker.user.defaults',
        #         'view_mode':'form',
        #         'res_id':_default_id,
        #         'type':'ir.actions.act_window',
        #         'view_type':'form',
        #         'view_id':self.env.ref('rocker_timesheet.rocker_user_view_form_simplified').id,
        #         'target':'new',
        #     }
