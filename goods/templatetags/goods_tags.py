from distutils.command import register
from django import template
from django.utils.http import urlencode
from goods.models import Categories

register = template.Library()

@register.simple_tag(name="tag_categories")
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(name="change_params", takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)