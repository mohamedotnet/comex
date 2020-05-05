from django import template

register = template.Library()


@register.filter
def hash(h, key):
    if key not in h:
        return "N/A"
    return h[key]