from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def include_fallback(context, *template_choices):
    t = template.loader.select_template(template_choices)
    return t.render(context)