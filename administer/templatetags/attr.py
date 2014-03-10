# from django import template
# register = template.Library()
#  
# @register.filter(name='addcss')
# def addcss(field, css):
#    return field.as_widget(attrs={"class":css})

from django import template
register = template.Library()
 
@register.filter(name='attr')
def attr(field, attr):
  attrs = {}
  definition = attr.split(',')

  for d in definition:
    t, v = d.split(':')
    attrs[t] = v

  return field.as_widget(attrs=attrs) 
