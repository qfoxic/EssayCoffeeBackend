from django.forms import ModelForm, ValidationError
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from reports.models import Report
from general.models import Task
from general.views import BaseView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

import constants as co


class ReportForm(ModelForm):
  def __init__(self, request=None, task_id=None, *args, **kwargs):
    super(ReportForm, self).__init__(*args, **kwargs)
    self.request = request
    self.task_id = task_id

  class Meta:
    model = Report 
    fields = ['title', 'body', 'rowner', 'rtask']

  def clean_rowner(self):
    """Specifies default User parameter."""
    return self.request.user

  def clean_rtask(self):
    """Specifies default task for a comment."""
    return Task.objects.get(pk=self.task_id)
  
  def check_permissions(self, cleaned_data):
    """Raises an exception if there are no permissions to save a form."""
    if not co.CheckPermissions(self.request.user,
        self.cleaned_data['rtask'], co.CAN_REPORT):
      raise ValidationError('It is not allowed to put reports on a task.') 
 
  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(ReportForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data
     


class CreateReportView(BaseView, CreateView):
  template_name = 'tasks/details.html'
  form_class = ReportForm
  queryset = Report.objects.all()

  def get_form_kwargs(self):
    kwargs = super(CreateReportView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.kwargs.get('task_id')})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())


class RemoveReportView(BaseView, DeleteView):
  template_name = 'tasks/delete.html'
  queryset = Report.objects.all()
  owner_required = True

  def get_success_url(self):
    task_id = self.object.rtask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().rowner.pk
