from general.models import Task
from general.forms import TaskSubmitForm
from general.views import BaseView, TaskIndexView, CreateTaskView, UpdateTaskView, DetailTaskView
from comments.views import CreateCommentView, RemoveCommentView 
from userprofile.views import CreateProfileView, UpdateProfileView
import constants as co


class CustomerTaskView(TaskIndexView):
  template_name = 'tasks/index.html'
  module_name = 'customer'

  def get_context_data(self, **kwargs):
    context = super(CustomerTaskView, self).get_context_data(**kwargs)
    owner = self.request.user
    context['tasks'] = Task.objects.filter(owner__exact=owner)
    return context


class CustomerCreateDraftTaskView(CreateTaskView):
  module_name = 'customer'
  template_name = 'tasks/edit.html'


class CustomerSubmitTaskView(UpdateTaskView):
  form_class = TaskSubmitForm 
  module_name = 'customer'
  template_name = 'tasks/detail.html'
  
  def get_success_url(self):
    return self.object.to_link()
  

class CustomerUpdateTaskView(UpdateTaskView):
  module_name = 'customer'
  template_name = 'tasks/edit.html'


class CustomerDetailTaskView(DetailTaskView):
  module_name = 'customer'
  template_name = 'tasks/detail.html'
  owner_required = True

  def user_id(self):
    return self.get_object().owner.pk


class CreateProfileCustomerView(CreateProfileView):
  module_name = 'customer'
  group_name = co.CUSTOMER_GROUP


class UpdateProfileCustomerView(UpdateProfileView):
  module_name = 'customer'
  group_name = co.CUSTOMER_GROUP


class CustomerCreateCommentView(CreateCommentView):
  module_name = 'customer'

class CustomerRemoveCommentView(RemoveCommentView):
  module_name = 'customer'
