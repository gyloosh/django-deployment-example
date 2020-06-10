from django import template

register = template.Library()



@register.filter(name='cut')
def cut(value, arg):
    """
    Ten filter wycina wszelkie wartości "arg" ze stringa
    """
    return value.replace(arg, '')


#register.filter('cut', cut)
