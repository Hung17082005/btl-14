# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# odoo models
# discuss
# mail models
# mixin
# core models (required for mixins)
from . import mail_notification  # keep before as decorated m2m
from . import (
    bus_presence,
    ir_action_act_window,
    ir_actions_server,
    ir_attachment,
    ir_config_parameter,
    ir_http,
    ir_model,
    ir_model_fields,
    ir_translation,
    ir_ui_view,
    mail_activity,
    mail_activity_mixin,
    mail_activity_type,
    mail_alias,
    mail_alias_mixin,
    mail_blacklist,
    mail_channel,
    mail_channel_partner,
    mail_channel_rtc_session,
    mail_composer_mixin,
    mail_followers,
    mail_guest,
    mail_ice_server,
    mail_mail,
    mail_message,
    mail_message_reaction,
    mail_message_subtype,
    mail_render_mixin,
    mail_shortcode,
    mail_template,
    mail_thread,
    mail_thread_blacklist,
    mail_thread_cc,
    mail_tracking_value,
    models,
    res_company,
    res_config_settings,
    res_groups,
    res_partner,
    res_users,
    res_users_settings,
    res_users_settings_volumes,
    update,
)
