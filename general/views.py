import os

from django.conf import settings
from django.utils import translation

import lib.confreader as conf
import constants as co


def check_mobile(request):
  if request.META.has_key('HTTP_USER_AGENT'):
    user_agent = request.META['HTTP_USER_AGENT']
    b = co.reg_b.search(user_agent)
    v = co.reg_v.search(user_agent[0:4])
    if b or v:
      return True
  return False


class BaseView(object):
  """Base class for all views. In addition, it loads settings from "config/" 
  module's directory and then from database.
  """
  module_name = 'general'

  def _init_module_settings(self):
    global_settings = conf.load(co.GLOBAL_MODULE_NAME)
    module_settings = conf.load(self.module_name)
    try:
      self.settings = conf.merge(global_settings, module_settings)
    except (TypeError, AttributeError), e:
      self.settings = {}
      print 'Could not read config files for module %s: %s' % (
          self.module_name, e)

  def get_template_names(self):
    self._init_module_settings()
    try:
      skin_prefix = self.settings['layout']['skin_prefix']
    except KeyError:
      print 'Could not obtain skin prefix skipping to default.'
      skin_prefix = co.DEFAULT_SKIN_PREFIX
    self.template_name = os.path.join(skin_prefix, self.module_name,
                                      self.template_name)
    #if check_mobile(self.request):
    #  self.template_name = os.path.join('mobile',
    #                                    self.module_name, self.template_name)

    return [self.template_name]

#  @method_decorator(login_required(login_url=co.LOGIN_URL))
#  def dispatch(self, request, *args, **kwargs):
#    return super(BaseView, self).dispatch(request, *args, **kwargs)


class TipView(BaseView):
  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    lang = translation.get_language()
    real_path = os.path.join(settings.SITE_ROOT, 'templates', 'tips/%s/%s.html' % ( lang, kwargs['id'] ))
    if_not_path = os.path.join(settings.SITE_ROOT, 'templates', 'tips/en/%s.html' % kwargs['id'])
    
    if not os.path.exists(real_path):
      if not os.path.exists(if_not_path):
        self.template_name = 'tips/en/not_found.html'
      else:  
        self.template_name = 'tips/en/%s.html' % kwargs['id']
    else:
      self.template_name = 'tips/%s/%s.html' % ( lang, kwargs['id'] )
    return kwargs


class HelpView(BaseView):
  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    lang = translation.get_language()
    if not kwargs['id']:
      kwargs['id'] = 'index'  
    real_path = os.path.join(settings.SITE_ROOT, 'templates', 'help/%s/%s.html' % ( lang, kwargs['id'] ))
    if_not_path = os.path.join(settings.SITE_ROOT, 'templates', 'help/en/%s.html' % kwargs['id'])
    
    if not os.path.exists(real_path):
      if not os.path.exists(if_not_path):
        self.template_name = 'help/en/not_found.html'
      else:  
        self.template_name = 'help/en/%s.html' % kwargs['id']
    else:
      self.template_name = 'help/%s/%s.html' % ( lang, kwargs['id'] )
    return kwargs
