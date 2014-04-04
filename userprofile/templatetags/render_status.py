from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import constants
 
register = template.Library()
 
@register.filter(name='render_status')
def render_status(value):

  options = {   
    constants.UNPROCESSED : _unprocessed,
    constants.PROCESSING  : _processing,
    constants.REJECTED    : _rejected,
    constants.COMPLETED   : _completed,
    constants.DRAFT       : _draft,
    constants.SUSPICIOUS  : _suspicious,
    constants.SENT        : _sent,
  }  

  return  mark_safe(options[value]())

render_status.is_safe = False  

def _unprocessed():
  return '<i class="fa fa-square-o has_tooltip" style="color:#CFCFCF" data-placement="right" title="Unprocessed"></i>'

def _completed():
  return '<i class="fa fa-check-square-o has_tooltip" style="color:#2080D0" data-placement="right" title="Completed"></i>'

def _sent():
  return '<i class="fa fa-share-square-o has_tooltip" style="color:#555" data-placement="right" title="Sent"></i>'
  
def _suspicious():
  return '<i class="fa fa-exclamation-triangle has_tooltip" style="color:#BF6000" data-placement="right" title="Suspicious"></i>'
  
def _processing():
  return '<i class="fa fa-play-circle has_tooltip" style="color:#2080D0" data-placement="right" title="Processing"></i>'
  
def _rejected():
  return '<i class="fa fa-times-circle has_tooltip" style="color:#A04040" data-placement="right" title="Rejected"></i>'

def _draft():
  return '<i class="fa fa-file-o has_tooltip" style="color:#9A9A9A" data-placement="right" title="Draft"></i>'
