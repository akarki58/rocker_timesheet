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
from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, Warning
from odoo import tools
from datetime import timedelta, datetime, date, time, timezone
from dateutil.rrule import rrule, DAILY
from odoo.osv import expression
import pytz

import logging

_logger = logging.getLogger(__name__)


class RockerProjectAllocation(models.Model):
    _name = 'rocker.project.allocation'
    # _auto = False
    _description = 'Project Resource Allocation'

    name = fields.Char('Name')
    company_id = fields.Many2one('res.company', "Company", default=lambda self: self.env.company, store=True,
                                 required=True)
    project_id = fields.Many2one('project.project', required=True, string='Project')
    resource_id = fields.Many2one('resource.resource', required=True, string='Allocated Resource')
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
