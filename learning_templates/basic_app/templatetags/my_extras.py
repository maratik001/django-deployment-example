from django import template

register = template.Library()


@register.filter(name='cuttos')
def cutt(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')


# register.filter('cuttos', cutt)
