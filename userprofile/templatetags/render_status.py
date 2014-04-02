from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
 
register = template.Library()
 
@register.filter(name='render_status')
def render_status(value):
  options = {   0 : _unprocessed,
                1 : _processing,
                2 : _rejected,
                3 : _completed,
                4 : _unprocessed,
                5 : _suspicious,
                6 : _draft,
  }  
  return  mark_safe(options[value]())

render_status.is_safe = False  

def _unprocessed():
  return '<i class="fa fa-square-o has_tooltip" style="font-size:1.5em;color:#CFCFCF" data-placement="right" title="Unprocessed"></i>'

def _completed():
  return '<i class="fa fa-check-square-o has_tooltip" style="font-size:1.5em;color:#2080D0" data-placement="right" title="Completed"></i>'
  
def _suspicious():
  return '<i class="fa fa-exclamation-triangle has_tooltip" style="font-size:1.5em;color:#BF6000" data-placement="right" title="Suspicious"></i>'
  
def _processing():
  return '<i class="fa fa-play-circle has_tooltip" style="font-size:1.5em;color:#2080D0" data-placement="right" title="Processing"></i>'
  
def _rejected():
  return '<i class="fa fa-times-circle has_tooltip" style="font-size:1.5em;color:#A04040" data-placement="right" title="Rejected"></i>'

def _draft():
  return '<i class="fa fa-file-o has_tooltip" style="font-size:1.5em;color:#2080D0" data-placement="right" title="Draft"></i>'