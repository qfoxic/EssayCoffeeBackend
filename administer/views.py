from general.models import Task
from general.views import TaskIndexView, DetailTaskView, UpdateTaskView
from general.views import DetailTaskView, UpdateTaskView
from general.forms import TaskApproveForm, TaskRejectForm, TaskSuspectForm 
from userprofile.views import DetailProfileView, UpdateProfileView
from userprofile.views import CreateProfileView
import constants as co

########task related views.
class AdminDetailTaskView(DetailTaskView):
  module_name = 'administer'
  template_name = 'tasks/detail.html'


class AdminApproveTaskView(UpdateTaskView):
  form_class = TaskApproveForm 
  module_name = 'administer'
  template_name = 'tasks/detail.html'
  owner_required = False
  
  def get_success_url(self):
    return self.object.to_link()


class AdminRejectTaskView(UpdateTaskView):
  form_class = TaskRejectForm 
  module_name = 'administer'
  template_name = 'tasks/detail.html'
  owner_required = False
  
  def get_success_url(self):
    return self.object.to_link()


class AdminSuspectTaskView(UpdateTaskView):
  form_class = TaskSuspectForm 
  module_name = 'administer'
  template_name = 'tasks/detail.html'
  owner_required = False
  
  def get_success_url(self):
    return self.object.to_link()

###################admin profiles
class AdminDetailProfileView(DetailProfileView):
  module_name = 'administer'
  template_name = 'userprofile/detail.html'


class AdminUpdateProfileView(UpdateProfileView):
  module_name = 'administer'
  template_name = 'userprofile/edit.html'
  group_name = co.ADMIN_GROUP 
  owner_required = True


class AdminCreateProfileView(CreateProfileView):
  module_name = 'administer'
  group_name = co.ADMIN_GROUP

#######################listings
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


class AdminSuspiciousTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminSuspiciousTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.SUSPICIOUS)
    return context


class AdminFinishedTasksView(TaskIndexView):
  module_name = 'administer'
  template_name = 'tasks/index.html'

  def get_context_data(self, **kwargs):
    context = super(AdminFinishedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.FINISHED)
    return context


