from django.forms import ModelForm, ValidationError
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView

from msgs.models import Message
from general.models import Task
from general.views import BaseView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

import constants as co


class MsgsForm(ModelForm):
  def __init__(self, request=None, task_id=None, *args, **kwargs):
    super(MsgsForm, self).__init__(*args, **kwargs)
    self.request = request
    self.task_id = task_id

  class Meta:
    model = Message 
    fields = ['title', 'body', 'mowner', 'mtask', 'visibility', 'readby']

  def clean_mowner(self):
    """Specifies default User parameter."""
    return self.request.user

  def clean_mtask(self):
    """Specifies default task for a message."""
    return Task.objects.get(pk=self.task_id)

  def clean_readby(self):
    """Updates field with user id."""
    return ':'+str(self.request.user.id)+':'
  
  def check_permissions(self, cleaned_data):
    """Raises an exception if there are no permissions to save a form."""
    if not co.CheckPermissions(self.request.user,
        self.cleaned_data['mtask'], co.CAN_MESSAGE):
      raise ValidationError('You can not send a message.') 
 
  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(MsgsForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data


class MsgsEditForm(ModelForm):
  def __init__(self, request=None, *args, **kwargs):
    super(MsgsEditForm, self).__init__(*args, **kwargs)
    self.request = request

  class Meta:
    model = Message 
    fields = ['title', 'body', 'readby']

  def clean_readby(self):
    """Updates field with user id."""
    return ':'+str(self.request.user.id)+':'
  
  def check_permissions(self, cleaned_data):
    """Raises an exception if there are no permissions to save a form."""
    if not co.CheckPermissions(self.request.user,
        self.instance.mtask, co.CAN_EDIT, 'message'):
      raise ValidationError('You can not update a message.') 
 
  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(MsgsEditForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data


class ListMsgsView(BaseView, ListView):
  template_name = 'msgs/index.html'
  context_object_name = 'msgs'
  
  def get_queryset(self):
    if self.request.user.get_group() == co.CUSTOMER_GROUP:
      tasks = Task.objects.filter(owner=self.request.user)
      return Message.objects.filter(Q(mtask__in=tasks),
          Q(visibility__in=[co.MSGS_CUSTOMER])|Q(mowner_id__exact=self.request.user.id))
    elif self.request.user.get_group() == co.WRITER_GROUP:
      tasks = Task.objects.filter(assignee=self.request.user) 
      return Message.objects.filter(Q(mtask__in=tasks),
          Q(visibility__in=[co.MSGS_WRITER])|Q(mowner_id__exact=self.request.user.id))
    return Message.objects.all()


class DetailMsgView(BaseView, DetailView):
  queryset = Message.objects.all()
  template_name = 'msgs/details.html'

  def get_context_data(self, **kwargs):
    """Hook to mark message as read."""
    obj = self.get_object()
    user_id = self.request.user.id
    readby = obj.readby.strip(':').split(':')
    readby.append(str(user_id))
    obj.readby = ':'+':'.join(set(readby))+':'
    obj.save()
    return super(DetailMsgView, self).get_context_data(**kwargs)
    

class UpdateMsgView(BaseView, UpdateView):
  form_class = MsgsEditForm 
  queryset = Message.objects.all()
  template_name = 'msgs/details.html'

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      obj = self.get_object()
    except:
      obj = None
    obj = obj and obj.mtask
    if not co.CheckPermissions(user, obj, co.CAN_EDIT, 'message'):
      raise PermissionDenied

  def get_form_kwargs(self):
    kwargs = super(UpdateMsgView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.object.mtask.id})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())
 

class CreateMsgView(BaseView, CreateView):
  template_name = 'tasks/details.html'
  form_class = MsgsForm
  queryset = Message.objects.all()

  def get_form_kwargs(self):
    kwargs = super(CreateMsgView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.kwargs.get('task_id')})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())


class RemoveMsgView(BaseView, DeleteView):
  template_name = 'tasks/delete.html'
  queryset = Message.objects.all()
  owner_required = True

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      obj = self.get_object()
    except:
      obj = None
    obj = obj and obj.mtask
    if not co.CheckPermissions(user, obj, co.CAN_DELETE, 'message'):
      raise PermissionDenied

  def get_success_url(self):
    task_id = self.object.mtask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().mowner.pk
