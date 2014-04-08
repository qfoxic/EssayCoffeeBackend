import os

from django.conf import settings
from django.utils import translation
from django.views.generic import TemplateView, View
from django.contrib.auth.views import login, logout, password_reset
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied

from general.models import Task
from userprofile.models import UserProfile
from comments.models import Comment
from reports.models import Report
from general.forms import TaskForm, SwitchStatusForm, LockTaskForm, UnlockTaskForm

from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.core.mail import send_mail

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

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


def get_stats(request):
  user = request.user
  group = user.is_anonymous() or request.user.get_group()
  if group == co.WRITER_GROUP:
    return {
      'finished': Task.get_finished_tasks(1, **{'assignee': user}), 
      'sent': Task.get_sent_tasks(1, **{'assignee': user}), 
      'unprocessed': Task.get_unprocessed_tasks(1, **{'assignee': user}),
      'active': Task.get_processing_tasks(1, **{'assignee': user}),
      'expired': Task.get_expired_tasks(1, **{'assignee': user,
                                              'status__exact': co.PROCESSING}),
    }
  elif group == co.ADMIN_GROUP or group == co.EDITOR_GROUP: 
    return {
      'completed': Task.get_finished_tasks(1), 
      'sent': Task.get_sent_tasks(1), 
      'unproc': Task.get_unprocessed_tasks(1),
      'suspect': Task.get_suspicious_tasks(1), 
      'rejected': Task.get_rejected_tasks(1), 
      'process': Task.get_processing_tasks(1),
      'expired': Task.get_expired_tasks(1, **{'status__exact': co.UNPROCESSED}),
      'adm_reports': Report.objects.all().count() 
    }
  else:
    return {}


class BaseView(View):
  """Base class for all views. In addition, it loads settings from "config/" 
  module's directory and then from database.
  """
  module_name = 'global'
  owner_required = False # raise an Error if owner is required.
  allowed_groups = [] # For these groups owner won't be checked.
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
  
  def _check_permissions(self):
    # Do nothing by default should be overloaded for different groups.
    pass
  
  def _owner_required(self, user, owner_id):
    """Checks whether user is owner of an entity."""
    user_group = UserProfile.objects.get(
        pk=owner_id).get_group()
    skip_owner_check = set(self.allowed_groups).intersection([user_group])
    if skip_owner_check:
      return
    if not user.is_superuser and not owner_id == user.pk:
      raise PermissionDenied

  def dispatch(self, request, *args, **kwargs):
    if self.owner_required:
      self._owner_required(request.user, self.user_id())
    self._check_permissions()
    return super(BaseView, self).dispatch(request, *args, **kwargs)

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    user = self.request.user
    # Pass constants to templates.
    context['co'] = co
    try:
      obj = context.get('object') or self.get_object()
    except:
      obj = None
    context['perm'] = {
      'can_comment': co.CheckPermissions(user, obj, co.CAN_COMMENT),
      'can_edit': co.CheckPermissions(user, obj, co.CAN_EDIT),
      'can_see_comments': co.CheckPermissions(user, obj, co.CAN_SEE_COMMENTS),
      'can_submit': co.CheckPermissions(user, obj, co.CAN_SUBMIT),
      # approve, suspect, reject
      'can_approve': co.CheckPermissions(user, obj, co.CAN_APPROVE),
      'can_reject': co.CheckPermissions(user, obj, co.CAN_REJECT),
      'can_suspect': co.CheckPermissions(user, obj, co.CAN_SUSPECT),
      # can writers mark task as sent.
      'can_send': co.CheckPermissions(user, obj, co.CAN_SEND),
      # Can admins put reports on task.
      'can_report': co.CheckPermissions(user, obj, co.CAN_REPORT),
      'can_lock': co.CheckPermissions(user, obj, co.CAN_LOCK) and not obj.is_locked(user),
      'can_unlock': co.CheckPermissions(user, obj, co.CAN_UNLOCK) and obj.is_locked(user, by_user=True),
      'can_delete': co.CheckPermissions(user, obj, co.CAN_DELETE),
      'can_complete': co.CheckPermissions(user, obj, co.CAN_COMPLETE)
    }
    context['stats'] = get_stats(self.request)
    context.setdefault('action_label', 'all')
    return super(BaseView, self).render_to_response(context, **response_kwargs)

  def get_template_names(self):
    return [self.template_name]


class LoginView(BaseView, TemplateView):
  template_name='general/login.html'

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
  template_name='general/password_reset_form.html'
  email_template_name='general/password_reset_email.html'
  
  def get_email_template(self):
     return os.path.join(self.module_name, self.email_template_name)

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
  template_name='general/password_reset_confirm.html'

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
  template_name='general/password_reset_complete.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset_complete(request=self.request,
        template_name=self.get_template_names(), extra_context=context)


class ResetPswdDoneView(BaseView, TemplateView):
  template_name='general/password_reset_done.html'

  def render_to_response(self, context, **response_kwargs):
    context.update(self.settings)
    return password_reset_done(request=self.request,
                               template_name=self.get_template_names(),
                               extra_context=context)


class TaskIndexView(BaseView, TemplateView):
  """Displays all tasks for singned users."""
  template_name = 'tasks/index.html'


class UpdateTaskView(BaseView, UpdateView):
  template_name = 'tasks/edit.html'
  form_class = TaskForm
  queryset = Task.objects.all()
  owner_required = True
  
  def render_to_response(self, context, **response_kwargs):
    obj = context['object'] or self.instance
    return super(UpdateTaskView, self).render_to_response(context, **response_kwargs)

  def get_form_kwargs(self):
    kwargs = super(UpdateTaskView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())

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
  template_name = 'tasks/details.html'
  
  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      obj = self.get_object()
    except:
      obj = None
    if group == co.WRITER_GROUP:
      # For writers we should check whether task
      # has been already assigned to another writer.
      if obj and obj.assignee and user.id != obj.assignee.id:
        raise PermissionDenied
 
  def get_context_data(self, **kwargs):
    context = super(DetailTaskView, self).get_context_data(**kwargs)
    task_id = self.kwargs.get('pk')
    context['comments'] = Comment.objects.filter(ctask_id__exact=task_id)
    context['reports'] = Report.objects.filter(rtask_id__exact=task_id)
    return context

  def user_id(self):
    return self.get_object().owner.pk


class RemoveTaskView(BaseView, DeleteView):
  queryset = Task.objects.all()
  success_url = reverse_lazy('task_list')
  template_name = 'tasks/delete.html'
  owner_required = True

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      obj = self.get_object()
    except:
      obj = None
    if group in co.CUSTOMER_GROUP:
      # We can remove task only in draft version.
      if not co.CheckPermissions(user, obj, co.CAN_DELETE):
        raise PermissionDenied

  def user_id(self):
    return self.get_object().owner.pk


class SwitchStatusView(UpdateTaskView):
  form_class = SwitchStatusForm 
  template_name = 'tasks/details.html'
  owner_required = False 
  
  def get_success_url(self):
    return self.object.to_link()


class LockTaskView(UpdateTaskView):
  form_class = LockTaskForm 
  template_name = 'tasks/details.html'
  owner_required = False 
  
  def get_success_url(self):
    return self.object.to_link()


class UnlockTaskView(UpdateTaskView):
  form_class = UnlockTaskForm 
  template_name = 'tasks/details.html'
  owner_required = False 
  
  def get_success_url(self):
    return self.object.to_link()


class StaticHtmlView(BaseView,TemplateView):
  def get_template_names(self):
    template_name = 'html/' + self.kwargs['path']  
    return [template_name]

