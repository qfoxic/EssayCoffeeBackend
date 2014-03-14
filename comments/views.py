from django.forms import ModelForm, ValidationError
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from comments.models import Comment
from general.models import Task
from general.views import BaseView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

import constants as co


class CommentForm(ModelForm):
  def __init__(self, request=None, task_id=None, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.request = request
    self.task_id = task_id

  class Meta:
    model = Comment
    fields = ['title', 'body', 'rating', 'cowner', 'ctask']

  def clean_cowner(self):
    """Specifies default User parameter."""
    return self.request.user

  def clean_ctask(self):
    """Specifies default task for a comment."""
    return Task.objects.get(pk=self.task_id)
  
  def check_permissions(self, cleaned_data):
    """Raises an exception if there are no permissions to save a form."""
    if self.cleaned_data['ctask'].owner != self.request.user:
      raise ValidationError('Only owners of this entity can leave comments.')
    if self.cleaned_data['ctask'].status == co.DRAFT:
      raise ValidationError('Items with a draft status can not be commented.') 
 
  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(CommentForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data
     


class CreateCommentView(BaseView, CreateView):
  module_name = 'default'
  template_name = 'tasks/detail.html'
  form_class = CommentForm
  queryset = Comment.objects.all()

  def get_form_kwargs(self):
    kwargs = super(CreateCommentView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.kwargs.get('task_id')})

  def form_invalid(self, form):
    # If form is invalid redirect to task details with an error.
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())


class RemoveCommentView(BaseView, DeleteView):
  module_name = 'default'
  template_name = 'tasks/delete.html'
  queryset = Comment.objects.all()
  owner_required = True

  def get_success_url(self):
    task_id = self.object.ctask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().cowner.pk
