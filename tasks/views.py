from tasks.models import Task, Categories
from general.views import BaseView


class CategoriesView(BaseView):
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


class TaskView(BaseView):
  model = Task
  template_name = 'task_form.html'
  context_object_name = 'task'
  module_name = 'tasks'
