# templatetags/to_point.py
from django.template import Library
from django import template
from django.template.defaulttags import cycle as cycle_original

register = Library()

#register = template.Library()

@register.filter
def to_point(value):
    return value.replace(",",".")

@register.tag
def cycle(*args, **kwargs):
    return cycle_original(*args, **kwargs)