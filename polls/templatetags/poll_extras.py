from __future__ import unicode_literals
import datetime
from django import template
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
from django.utils.translation import ugettext, ungettext_lazy

register = template.Library()
TIMESINCE_CHUNKS = (
    (60 * 60 , ungettext_lazy('%d hora', '%d horas')),
)
@register.filter
def leftbirt(d, now=None):
    # Convert datetime.date to datetime.datetime for comparison.
    if not now:
        now = datetime.date.now()
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(now.year, d.month, d.day)

    delta = d - now
    # ignore microseconds
    since = abs(delta.days * 24 * 60 * 60 + delta.seconds)//3600
    if since<=72:
        for i, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
            count = (since)
        result = avoid_wrapping(name % count)
    else:
        result=False
    return result

@register.filter
def logicalbirt(d, now=None):

    # Convert datetime.date to datetime.datetime for comparison.
    if not now:
        now = datetime.date.now()
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(now.year, d.month, d.day)

    delta = d - now
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since >= 0:
        return True
    else:
        return False
