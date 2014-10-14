from general.views import BaseView, serve 
from ftpstorage.forms import UploadForm
from ftpstorage.models import Upload 
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
  template_name = 'orders/order_id.html'

  def get_form_kwargs(self):
    kwargs = super(UploadFileView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs
  
  def get_success_url(self):
    return reverse('order-id', kwargs={'pk': self.kwargs.get('task_id')}) + '?files=1'

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.error(self.request, 'Did you forget to add an attachment?')
    return HttpResponseRedirect(self.get_success_url())


class DownloadFileView(BaseView):
  template_name = 'orders/order_id.html'

  def _check_permissions(self):
    user = self.request.user
    group = user.get_group()
    try:
      self.upload = Upload.objects.get(pk=self.kwargs['pk'])
      task = self.upload.ftask
    except:
      raise Http404
    if not task.owner == user:
        if not self.upload.access_level == co.PUBLIC_ACCESS:
          raise Http404

  def get(self, *args, **kwargs):
    try:
      request = serve(self.request, self.upload.attach.name)
      filename = self.upload.get_filename()
      request['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
      return request 
    except Exception, e:
      messages.add_message(self.request, messages.ERROR, str(e))
      return HttpResponseRedirect(reverse('order-id', kwargs={'pk': self.upload.ftask.pk}))


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
