# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import SUPERUSER_ID, api

from . import models, wizard


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    ICP = env['ir.config_parameter']
    ICP.set_param('google.pse.id', False)
    ICP.set_param('google.custom_search.key', False)
