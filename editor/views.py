from general.models import Task
from general.views import TaskIndexView,UpdateTaskView

from userprofile.models import UserProfile
from userprofile.views import ListProfileView
import constants as co


class EditorUpdateTaskView(UpdateTaskView):
  owner_required=False


class EditorWritersView(ListProfileView):
  def get_context_data(self, **kwargs):
    context = super(EditorWritersView, self).get_context_data(**kwargs)
    context['users'] = UserProfile.objects.filter(groups__name=co.WRITER_GROUP)
    context['action_label'] = 'writers'
    return context


class EditorRejectedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorRejectedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_rejected_tasks(0)
    context['action_label'] = 'rejected'
    return context


class EditorExpiredTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorExpiredTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    if status == co.UNASSIGNED_ORDER:
      context['tasks'] = Task.get_expired_tasks(0, **{'assignee__isnull': True,
                                                      'status__exact': co.UNPROCESSED})
    elif status == co.ASSIGNED_ORDER:
      context['tasks'] = Task.get_expired_tasks(0, **{'assignee__isnull': False, 
                                                      'status__exact': co.UNPROCESSED})
    else:
      context['tasks'] = Task.get_expired_tasks(0, **{'status__exact': co.UNPROCESSED})
    context['action_label'] = 'expired'
    return context


class EditorActiveTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorActiveTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    if status == co.UNASSIGNED_ORDER:
      context['tasks'] = Task.get_processing_tasks(0, **{'assignee__isnull': True})
    elif status == co.ASSIGNED_ORDER:
      context['tasks'] = Task.get_processing_tasks(0, **{'assignee__isnull': False})
    else:
      context['tasks'] = Task.get_processing_tasks(0)
    context['action_label'] = 'processing'
    return context


class EditorSuspiciousTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorSuspiciousTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_suspicious_tasks(0)
    context['action_label'] = 'suspicious'
    return context


class EditorFinishedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorFinishedTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_finished_tasks(0)
    context['action_label'] = 'completed'
    return context


class EditorSentTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(EditorSentTasksView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_sent_tasks(0)
    context['action_label'] = 'sent'
    return context
