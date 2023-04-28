from django import template
register = template.Library()

def conv(str):
    return eval(str)

register.filter("conv", conv)