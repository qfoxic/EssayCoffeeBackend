from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from comments.models import Comment
from general.models import Task
from general.views import BaseView
from django.core.urlresolvers import reverse


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


class CreateCommentView(BaseView, CreateView):
  form_class = CommentForm
  queryset = Comment.objects.all()
  module_name = 'default'
  template_name = 'detail.html'

  def get_form_kwargs(self):
    kwargs = super(CreateCommentView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['task_id'] = self.kwargs.get('task_id')
    return kwargs

  def get_success_url(self):
    return reverse('task_view', kwargs={'pk': self.kwargs.get('task_id')})


class RemoveCommentView(BaseView, DeleteView):
  module_name = 'default'
  queryset = Comment.objects.all()
  template_name = 'delete.html'
  owner_required = True

  def get_success_url(self):
    task_id = self.object.ctask.pk
    return reverse('task_view', kwargs={'pk': task_id})

  def user_id(self):
    return self.get_object().cowner.pk
