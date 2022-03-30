from django import template

register = template.Library()


@register.filter(name='Censor')
def censor(value):
    cens = ['брань', 'Third']
    for i in cens:
        if i in value:
            value = value.replace(i, '***')
    return value


