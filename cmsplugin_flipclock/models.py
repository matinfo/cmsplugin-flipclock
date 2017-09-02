# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from timezone_field import TimeZoneField

from .settings import *


class FlipClockPlugin(CMSPlugin):
    """ FlipClock CMS plugin model """
    clock_face = models.CharField(
        _('clockFace'),
        max_length=20,
        choices=CLOCKFACE_CHOICES,
        default=DEFAULT_CLOCKFACE_CHOICE,
        help_text=_('This is the name of the clock that is used to build '
                    'the clock display.')
    )
    auto_play = models.BooleanField(
        _('autoPlay'),
        default=True,
        help_text=_('If selected, the clock will not automatically '
                    'add the play class to start the animation.')
    )
    auto_start = models.BooleanField(
        _('autoStart'),
        default=True,
        help_text=_('If this is set to false, the clock will not auto start.')
    )
    countdown = models.BooleanField(
        _('Countdown'),
        default=False,
        help_text=_('If seleted, the clock will count down instead of up.')
    )
    show_seconds = models.BooleanField(
        _('showSeconds'),
        default=True,
        help_text=_('If selected, the clock will show <i>second</i>. '
                    'Compatible with clockFace Hourly, Minute and Daily counter.')
    )
    date = models.DateTimeField(
        _('date & time'), blank=True, null=True,
        help_text=_('Start or end date depending if <i>countdown</i> set. '
                    'Compatible with clockFace Hourly, Minute and Daily counter.')
    )
    numbers = models.IntegerField(
        _('number'), default=0,
        help_text=_('Compatible with clockFace General counter.')
    )
    timezone = TimeZoneField(
        verbose_name=_('time zone'), blank=True, null=True,
        default='Europe/London',
        help_text=_('If set force the timezone used, otherwise use user timezone.')
    )

    def __str__(self):
        return 'clockFace: {}, autoPlay: {}, autoStart: {}, countDown: {}'.format(
            self.get_clock_face_display(),
            'Yes' if self.auto_play else 'No',
            'Yes' if self.auto_start else 'No',
            'Yes' if self.countdown else 'No')
