# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.payment import reset_payment_acquirer

from . import controllers, models


def uninstall_hook(cr, registry):
    reset_payment_acquirer(cr, registry, 'adyen')
