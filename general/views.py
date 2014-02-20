import os

from django.conf import settings
from django.utils import translation
from django.views.generic import TemplateView, View
from django.contrib.auth.views import login, logout, password_reset
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied

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


def owner_required(user, owner_id):
  """Checks whether user is owner of an entity."""
  if not user.is_superuser and not owner_id == user.pk :
    raise PermissionDenied


class BaseView(View):
  """Base class for all views. In addition, it loads settings from "config/" 
  module's directory and then from database.
  """
  module_name = 'general'
  owner_required = False # raise an Error if owner is required.

  def __init__(self, **kwargs):
    super(BaseView, self).__init__(**kwargs)
    global_settings = conf.load(co.GLOBAL_MODULE_NAME)
    module_settings = conf.load(self.module_name)
    try:
      self.settings = conf.merge(global_settings, module_settings)
    except (TypeError, AttributeError), e:
      self.settings = {}
      print 'Could not read config files for module %s: %s' % (
          self.module_name, e)

  def dispatch(self, request, *args, **kwargs):
    if self.owner_required:
      owner_required(request.user, self.user_id())
    return super(BaseView, self).dispatch(request, *args, **kwargs)

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return super(BaseView, self).render_to_response(context, **response_kwargs)

  def get_template_names(self):
    try:
      skin_prefix = self.settings['layout']['skin_prefix']
    except KeyError:
      print 'Could not obtain skin prefix skipping to default.'
      skin_prefix = co.DEFAULT_SKIN_PREFIX
    self.template_name = os.path.join(skin_prefix, self.module_name,
                                      self.template_name)
    return [self.template_name]


class LoginView(BaseView, TemplateView):
  template_name='login.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return login(request=self.request, template_name=self.get_template_names(),
        extra_context=context)

  def post(self, *args, **kwargs):
    kwargs.update(self.settings)
    return login(request=self.request, template_name=self.get_template_names(),
                 extra_context=kwargs)


class LogoutView(BaseView, TemplateView):
  def render_to_response(self, context, **response_kwargs):
    return logout(request=self.request, next_page=reverse_lazy('all_tasks'))


class ResetPswdView(BaseView, TemplateView):
  template_name='password_reset_form.html'
  email_template_name='password_reset_email.html'
  
  def get_email_template(self):
    try:
      skin_prefix = self.settings['layout']['skin_prefix']
    except KeyError:
      print 'Could not obtain skin prefix skipping to default.'
      skin_prefix = co.DEFAULT_SKIN_PREFIX
    return os.path.join(skin_prefix, self.module_name, self.email_template_name)

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset(request=self.request,
                          template_name=self.get_template_names(),
                          email_template_name=self.get_email_template(),
                          post_reset_redirect=reverse_lazy('pswd_reset_done'),
                          extra_context=context)

  def post(self, *args, **kwargs):
    return password_reset(request=self.request,
                          template_name=self.get_template_names(),
                          email_template_name=self.get_email_template(),
                          post_reset_redirect=reverse_lazy('pswd_reset_done'))


class ResetPswdConfirmView(BaseView, TemplateView):
  template_name='password_reset_confirm.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset_confirm(request=self.request,
        uidb64=context['uidb64'], token=context['token'],
        template_name=self.get_template_names(),
        post_reset_redirect=reverse_lazy('pswd_reset_complete'),
        extra_context=context)

  def post(self, *args, **kwargs):
    return password_reset_confirm(request=self.request,
        uidb64=kwargs['uidb64'], token=kwargs['token'],
        post_reset_redirect=reverse_lazy('pswd_reset_complete'))


class ResetPswdCompleteView(BaseView, TemplateView):
  template_name='password_reset_complete.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset_complete(request=self.request,
        template_name=self.get_template_names(), extra_context=context)


class ResetPswdDoneView(BaseView, TemplateView):
  template_name='password_reset_done.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset_done(request=self.request,
                               template_name=self.get_template_names(),
                               extra_context=context)

