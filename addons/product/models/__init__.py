# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# flake8: noqa: F401

# don't try to be a good boy and sort imports alphabetically.
# `product.template` should be initialised before `product.product`
from . import (
    decimal_precision,
    product,
    product_attribute,
    product_pricelist,
    product_template,
    res_company,
    res_config_settings,
    res_currency,
    res_partner,
    uom_uom,
)
