from odoo import SUPERUSER_ID, api


def load_translations(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref("l10n_tw.l10n_tw_chart_template").process_coa_translations()
