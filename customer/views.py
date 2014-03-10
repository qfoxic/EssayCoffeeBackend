from general.models import Task, Categories
from general.views import BaseView, TaskIndexView, CreateTaskView, UpdateTaskView, DetailTaskView
import constants as co


class CustomerTaskView(TaskIndexView):
  template_name = 'tasks/index.html'
  module_name = 'customer'

  def get_context_data(self, **kwargs):
    context = super(CustomerTaskView, self).get_context_data(**kwargs)
    owner = self.request.user
    context['tasks'] = Task.objects.filter(owner__exact=owner)
    return context


class CustomerCreateTaskView(CreateTaskView):
  module_name = 'customer'
  template_name = 'tasks/edit.html'


class CustomerUpdateTaskView(UpdateTaskView):
  module_name = 'customer'
  template_name = 'tasks/edit.html'


class CustomerDetailTaskView(DetailTaskView):
  module_name = 'customer'
  template_name = 'tasks/detail.html'

