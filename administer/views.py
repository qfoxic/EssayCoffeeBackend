from general.models import Task
from general.views import TaskIndexView,UpdateTaskView

from userprofile.models import UserProfile
from userprofile.views import ListProfileView
import constants as co


class AdminUpdateTaskView(UpdateTaskView):
  owner_required=False


class AdminWritersView(ListProfileView):
  def get_context_data(self, **kwargs):
    context = super(AdminWritersView, self).get_context_data(**kwargs)
    context['users'] = UserProfile.objects.filter(groups__name=co.WRITER_GROUP)
    return context


class AdminCustomersView(ListProfileView):
  def get_context_data(self, **kwargs):
    context = super(AdminCustomersView, self).get_context_data(**kwargs)
    context['users'] = UserProfile.objects.filter(groups__name=co.CUSTOMER_GROUP)
    return context


class AdminUnprocessedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminUnprocessedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.UNPROCESSED)
    return context


class AdminRejectedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminRejectedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.REJECTED)
    return context


class AdminActiveTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminActiveTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    if status == co.UNASSIGNED_ORDER:
      context['tasks'] = Task.objects.filter(status__exact=co.ACTIVE,
                                             assignee__isnull=True)
    elif status == co.ASSIGNED_ORDER:
      context['tasks'] = Task.objects.filter(status__exact=co.ACTIVE,
                                             assignee__isnull=False)
    else:
      context['tasks'] = Task.objects.filter(status__exact=co.ACTIVE)
    return context


class AdminSuspiciousTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminSuspiciousTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.SUSPICIOUS)
    return context


class AdminFinishedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminFinishedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.objects.filter(status__exact=co.FINISHED)
    return context


