# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import SUPERUSER_ID, api

from . import controllers, models, utils, wizards


def reset_payment_acquirer(cr, registry, provider):
    env = api.Environment(cr, SUPERUSER_ID, {})
    acquirers = env['payment.acquirer'].search([('provider', '=', provider)])
    acquirers.write({
        'provider': 'none',
        'state': 'disabled',
    })
