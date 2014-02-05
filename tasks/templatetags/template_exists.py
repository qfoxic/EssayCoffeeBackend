# from django import template
# 
# register = template.Library()
# 
# @register.simple_tag
# def template_exists(template_name):
#     try:
#         template.loader.get_template(template_name)
#         return True
#     except template.TemplateDoesNotExist:
#         return False
    
from django import template
from django.template.loader_tags import do_include
from django.template.defaulttags import CommentNode
register = template.Library()

@register.tag('template_exists')
def do_include_maybe(parser, token):
    try:
        return do_include(parser, token)
    except template.TemplateDoesNotExist:
        return CommentNode()    