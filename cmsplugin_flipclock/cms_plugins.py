# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class FlipClockPlugin(CMSPluginBase):
    render_template = 'cmsplugin_flipclock/flipclock.html'
    allow_children = False
    name = _('FlipClock Plugin')
    module = _('FlipClock')
    model = models.FlipClockPlugin

    fieldsets = (
        (None, {
            'fields': (
                'clock_face',
                ('countdown', 'show_seconds'),
                'date',
                'timezone',
                'numbers',
            )
        }),
        (_('More Options'), {
            'fields': (
                ('auto_play', 'auto_start'),
            ),
            'classes': ('collapse',)
        }),
    )

plugin_pool.register_plugin(FlipClockPlugin)
