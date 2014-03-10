from general.models import Task, Categories
from general.views import BaseView, TaskIndexView, DetailTaskView
from userprofile.views import DetailProfileView,UpdateProfileView
import constants as co


class AdminTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'


class AdminDetailTaskView(DetailTaskView):
  module_name = 'administer'
  template_name = 'tasks/detail.html'


class AdminDetailProfileView(DetailProfileView):
  module_name = 'administer'
  template_name = 'userprofile/detail.html'


class AdminUpdateProfileView(UpdateProfileView):
  module_name = 'administer'
  template_name = 'userprofile/edit.html'
  group_name = co.ADMIN_GROUP 
  owner_required = True


class AdminUnprocessedTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminUnprocessedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.UNPROCESSED)
    return context


class AdminRejectedTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminRejectedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.REJECTED)
    return context


class AdminActiveTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminActiveTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.ACTIVE)
    return context


class AdminFinishedTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminFinishedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.FINISHED)
    return context
