# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Updating mako environement in order to be able to use slug
try:
    from odoo.addons.http_routing.models.ir_http import slug
    from odoo.tools.rendering_tools import template_env_globals

    template_env_globals.update({
        'slug': slug
    })
except ImportError:
    pass

from . import controllers, models, wizard
