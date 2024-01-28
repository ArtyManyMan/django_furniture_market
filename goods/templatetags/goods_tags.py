from distutils.command import register
from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag(name="tag_categories")
def tag_categories():
    return Categories.objects.all()