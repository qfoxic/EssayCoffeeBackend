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
  return '<i class="fa fa-square-o" style="font-size:1.5em"></i>'

def _completed():
  return '<i class="fa fa-check-square-o" style="font-size:1.5em;color:#008F00"></i>'  
  
def _suspicious():
  return '<i class="fa fa-exclamation-triangle" style="font-size:1.5em;color:#BF6000"></i>'    
  
def _processing():
  return '<i class="fa fa-play-circle" style="font-size:1.5em;color:#2080D0"></i>'
  
def _rejected():
  return '<i class="fa fa-times-circle" style="font-size:1.5em;color:#A04040"></i>'

def _draft():
  return '<i class="fa fa-file-o" style="font-size:1.5em;color:#2080D0"></i>'
      