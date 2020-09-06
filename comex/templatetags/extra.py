from django import template
from django.utils.safestring import mark_safe

import json
register = template.Library()


@register.filter
def hash(h, key):
    if key not in h:
        return "N/A"
    return h[key]


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))
