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
    context['tasks'] = Task.get_unprocessed_tasks(0)
    return context


class AdminRejectedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminRejectedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_rejected_tasks(0)
    return context


class AdminExpiredTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminExpiredTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    if status == co.UNASSIGNED_ORDER:
      context['tasks'] = Task.get_expired_tasks(0, **{'assignee__isnull': True})
    elif status == co.ASSIGNED_ORDER:
      context['tasks'] = Task.get_expired_tasks(0, **{'assignee__isnull': False})
    else:
      context['tasks'] = Task.get_expired_tasks(0)
    return context


class AdminActiveTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminActiveTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    if status == co.UNASSIGNED_ORDER:
      context['tasks'] = Task.get_active_tasks(0, **{'assignee__isnull': True})
    elif status == co.ASSIGNED_ORDER:
      context['tasks'] = Task.get_active_tasks(0, **{'assignee__isnull': False})
    else:
      context['tasks'] = Task.get_active_tasks(0)
    return context


class AdminSuspiciousTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminSuspiciousTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_suspicious_tasks(0)
    return context


class AdminFinishedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(AdminFinishedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_finished_tasks(0)
    return context


