from general.views import BaseView, serve 
from ftpstorage.forms import UploadForm, UploadVisibilityForm 
from ftpstorage.models import Upload 
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
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


class DownloadFileView(BaseView):
  template_name = 'tasks/details.html'

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      self.upload = Upload.objects.get(pk=self.kwargs['pk'])
      task = self.upload.ftask
    except:
      raise Http404
    if group == co.WRITER_GROUP:
      if not task.is_locked(user, by_user=True):
        raise Http404
      if not self.upload.access_level == co.PUBLIC_ACCESS:
        # Don't raise Permission denied to avoid hacker attacks.
        raise Http404
    elif group == co.CUSTOMER_GROUP:
      if not self.upload.access_level == co.PUBLIC_ACCESS:
        # Don't raise Permission denied to avoid hacker attacks.
        raise Http404
      if not task.owner == user:
        # Don't raise Permission denied to avoid hacker attacks.
        raise Http404

  def get(self, *args, **kwargs):
    try:
      request = serve(self.request, self.upload.attach.name)
      filename = self.upload.get_filename()
      request['Content-Disposition'] = 'attachment; filename=%s' % filename 
      return request 
    except Exception, e:
      messages.add_message(self.request, messages.ERROR, str(e))
      return HttpResponseRedirect(reverse('task_view', kwargs={'pk': self.upload.ftask.pk}))
      
  

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
    if not co.CheckPermissions(user, obj, co.CAN_DELETE, 'upload'):
      raise PermissionDenied

  def get_success_url(self):
    task_id = self.object.ftask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().fowner.pk
