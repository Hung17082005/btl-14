# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import uuid

from odoo import SUPERUSER_ID, api

from . import controllers, models, utils, wizard


def init_initiating_microsoft_uuid(cr, registry):
    """ Sets the company name as the default value for the initiating
    party name on all existing companies once the module is installed. """
    env = api.Environment(cr, SUPERUSER_ID, {})
    config_parameter = env['ir.config_parameter'].sudo()
    microsoft_guid = config_parameter.get_param('microsoft_calendar.microsoft_guid', False)
    if not microsoft_guid:
        config_parameter.set_param('microsoft_calendar.microsoft_guid', str(uuid.uuid4()))
