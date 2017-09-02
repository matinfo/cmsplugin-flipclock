# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


CLOCKFACE_CHOICES = [
    ('HourlyCounter', _('Hourly Counter')),
    ('MinuteCounter', _('Minute Counter')),
    ('DailyCounter', _('Daily Counter')),
    ('TwelveHourClock', _('12hr Clock')),
    ('TwentyFourHourClock', _('24hr Clock')),
    ('Counter', _('General Counter')),
]
DEFAULT_CLOCKFACE_CHOICE = CLOCKFACE_CHOICES[0][0]
