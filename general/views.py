import os

from django.conf import settings
from django.utils import translation
from django.views.generic import TemplateView, View
from django.contrib.auth.views import login, logout, password_reset
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied

from general.models import Task
from comments.models import Comment
from general.forms import TaskForm

from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.core.mail import send_mail

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

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
  module_name = 'default'
  owner_required = False # raise an Error if owner is required.

  def __init__(self, **kwargs):
    super(BaseView, self).__init__(**kwargs)
    global_settings = conf.load(co.GLOBAL_MODULE_NAME)
    module_settings = conf.load(self.module_name)
    try:
      self.settings = conf.merge(module_settings, global_settings)
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
    self.template_name = os.path.join(skin_prefix, self.template_name)
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
    return logout(request=self.request, next_page=reverse_lazy('task_list'))


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


class TaskIndexView(BaseView, TemplateView):
  """Displays all tasks for singned users."""
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(TaskIndexView, self).get_context_data(**kwargs)
    if self.request.user.is_authenticated():
      context['tasks'] = Task.objects.all()
    return context


class UpdateTaskView(BaseView, UpdateView):
  template_name = 'tasks/edit.html'
  form_class = TaskForm
  queryset = Task.objects.all()
  owner_required = True

  def get_form_kwargs(self):
    kwargs = super(UpdateTaskView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

  def user_id(self):
    return self.get_object().owner.pk


class CreateTaskView(BaseView, CreateView):
  form_class = TaskForm
  queryset = Task.objects.all()
  template_name = 'tasks/edit.html'

  def get_form_kwargs(self):
    kwargs = super(CreateTaskView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs


class DetailTaskView(BaseView, DetailView):
  queryset = Task.objects.all()
  template_name = 'tasks/detail.html'

  def get_context_data(self, **kwargs):
    context = super(DetailTaskView, self).get_context_data(**kwargs)
    task_id = self.kwargs.get('pk')
    context['comments'] = Comment.objects.filter(ctask_id__exact=task_id)
    return context


class RemoveTaskView(BaseView, DeleteView):
  queryset = Task.objects.all()
  success_url = reverse_lazy('task_list')
  template_name = 'tasks/delete.html'
  owner_required = True

  def user_id(self):
    return self.get_object().owner.pk

