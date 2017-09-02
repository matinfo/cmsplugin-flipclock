# -*- coding: utf-8 -*-
import json
from datetime import date, datetime

from django import template
from django.utils.html import mark_safe
from django.utils.timezone import is_aware, utc

register = template.Library()


@register.filter
def toJSON(value):
    return mark_safe(json.dumps(value))


# This filter doesn't require expects_localtime=True because it deals properly
# with both naive and aware datetimes. Therefore avoid the cost of conversion.
@register.filter
def seconde(value):
    """
    For date and time values show how many seconds, minutes, or hours ago
    compared to current timestamp return representing string.
    """
    if not isinstance(value, date):  # datetime is a subclass of date
        return value

    now = datetime.now(utc if is_aware(value) else None)
    if value > now:
        delta = now - value
        return 3600 * delta.seconds
    else:
        delta = value - now
        return 3600 * delta.seconds

