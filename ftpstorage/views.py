from general.views import BaseView 
from ftpstorage.forms import UploadForm, UploadVisibilityForm 
from ftpstorage.models import Upload 
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

import constants as co


class UploadFileView(BaseView, CreateView):
  form_class = UploadForm
  queryset = Upload.objects.all() 
  template_name = 'tasks/details.html'

  def get_form_kwargs(self):
    kwargs = super(UploadFileView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs
  
  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.kwargs.get('task_id')})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())


class UpdateUploadView(BaseView, UpdateView):
  form_class = UploadVisibilityForm 
  queryset = Upload.objects.all() 
  template_name = 'tasks/details.html'

  def get_form_kwargs(self):
    kwargs = super(UpdateUploadView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.object.ftask.id})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())


class RemoveUploadView(BaseView, DeleteView):
  template_name = 'tasks/delete.html'
  queryset = Upload.objects.all()
  owner_required = True

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      obj = self.get_object()
    except:
      obj = None
    obj = obj and obj.ftask
    if not co.CheckPermissions(user, obj, co.CAN_DELETE, 'upload'):
      raise PermissionDenied

  def get_success_url(self):
    task_id = self.object.ftask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().fowner.pk
