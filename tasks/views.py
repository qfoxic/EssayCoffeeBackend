from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from tasks.models import Categories, Task
from general.views import BaseView


class CategoriesView(BaseView, ListView):
  """Displays categories with their tasks.

  If category_id is missed then displays all tasks else displays tasks for
  specified category id.
  """
  template_name = 'categories_list.html'
  model = Categories
  context_object_name = 'categories'
  module_name = 'tasks'

  def get_context_data(self, **kwargs):
    context = super(CategoriesView, self).get_context_data(**kwargs)
    category_id = self.kwargs.get('category_id')

    if category_id:
      context['tasks'] = Task.objects.filter(category_id__exact=category_id)
    else:
      context['tasks'] = Task.objects.all()
    return context


class TaskView(BaseView, DetailView):
  model = Task
  template_name = 'task_form.html'
  context_object_name = 'task'
  module_name = 'tasks'
