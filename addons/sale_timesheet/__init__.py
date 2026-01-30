# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import SUPERUSER_ID, api

from . import controllers, models, report, wizard


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    env.ref("account.account_analytic_line_rule_billing_user").write({'domain_force': "[(1, '=', 1)]"})
