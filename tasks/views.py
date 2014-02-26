from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from tasks.models import Task, Categories
from comments.models import Comment
from general.views import BaseView


class TaskForm(ModelForm):
  def __init__(self, request=None, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    self.request = request

  class Meta:
    model = Task
    fields = ['first_name', 'last_name', 'gender', 'email', 'country', 'phone',
              'paper_title', 'discipline', 'assigment', 'level', 'urgency',
              'spacing', 'page_number', 'style', 'source_number',
              'instructions', 'attach', 'discount', 'accept_terms', 'category',
              'owner']

  def clean_owner(self):
    """Specifies default User parameter."""
    return self.request.user


class CategoriesView(BaseView, TemplateView):
  """Displays categories with their tasks.

  If category_id is missed then displays all tasks else displays tasks for
  specified category id.
  """
  template_name = 'index.html'
  module_name = 'tasks'

  def get_context_data(self, **kwargs):
    context = super(CategoriesView, self).get_context_data(**kwargs)
    category_id = self.kwargs.get('category_id')

    if category_id:
      context['tasks'] = Task.objects.filter(category_id__exact=category_id)
    else:
      context['tasks'] = Task.objects.all()
    context['categories'] = Categories.objects.all()
    return context


class UpdateTaskView(BaseView, UpdateView):
  template_name = 'edit.html'
  form_class = TaskForm
  queryset = Task.objects.all()
  module_name = 'tasks'
  owner_required = True

  def get_form_kwargs(self):
    kwargs = super(UpdateTaskView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

  def user_id(self):
    return self.get_object().owner.pk


class CreateTaskView(BaseView, CreateView):
  module_name = 'tasks'
  form_class = TaskForm
  queryset = Task.objects.all()
  template_name = 'edit.html'

  def get_form_kwargs(self):
    kwargs = super(CreateTaskView, self).get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs


class DetailTaskView(BaseView, DetailView):
  module_name = 'tasks'
  queryset = Task.objects.all()
  template_name = 'detail.html'

  def get_context_data(self, **kwargs):
    context = super(DetailTaskView, self).get_context_data(**kwargs)
    task_id = self.kwargs.get('pk')
    context['comments'] = Comment.objects.filter(ctask_id__exact=task_id)
    return context


class RemoveTaskView(BaseView, DeleteView):
  module_name = 'tasks'
  queryset = Task.objects.all()
  success_url = reverse_lazy('all_tasks')
  template_name = 'delete.html'
  owner_required = True

  def user_id(self):
    return self.get_object().owner.pk

