from django import template
from mainapp.models import *

register = template.Library()

@register.filter
def product(request):
    return Product.objects.all()

@register.filter
def service(request):
    return Project.objects.all()

@register.filter
def range_filter(value):
    return value[0:200] + "...."

@register.filter
def range_filter_lite(value):
    return value[0:60] + "...."

@register.filter
def range_filter_blog(value):
    return value[0:130] + "...."