from general.models import Task
from general.views import TaskIndexView,SwitchStatusView
import constants as co


class WriterTaskView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterTaskView, self).get_context_data(**kwargs)
    context['tasks'] = Task.get_unprocessed_tasks(0, **{'assignee__isnull': True})
    return context


class WriterActiveTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterActiveTasksView, self).get_context_data(**kwargs)
    status = self.request.GET.get('status')
    cur_user = self.request.user
    context['tasks'] = Task.get_active_tasks(0, **{'assignee': cur_user})
    return context


class WriterExpiredTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterExpiredTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_expired_tasks(0, **{'assignee': cur_user,
                                                    'status__exact': co.ACTIVE})
    return context


class WriterFinishedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterFinishedTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_finished_tasks(0, **{'assignee': cur_user})
    return context


class WriterSwitchStatusView(SwitchStatusView):
  def form_valid(self, form):
    """If form is valid assign user to a task."""
    self.object.assignee = self.request.user
    return super(WriterSwitchStatusView, self).form_valid(form) 
