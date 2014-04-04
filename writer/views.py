from general.models import Task
from general.views import TaskIndexView,SwitchStatusView
import constants as co


class WriterTaskView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterTaskView, self).get_context_data(**kwargs)
    params = {'assignee__isnull': True, 'access_level__in': [co.PUBLIC_ACCESS]}
    context['tasks'] = Task.get_processing_tasks(0, **params)
    context['action_label'] = 'processing'
    return context


class WriterActiveTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterActiveTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_processing_tasks(0, **{'assignee': cur_user})
    context['action_label'] = 'my processing'
    return context


class WriterExpiredTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterExpiredTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_expired_tasks(0, **{'assignee': cur_user,
                                                    'status__exact': co.PROCESSING})
    context['action_label'] = 'my expired'
    return context


class WriterFinishedTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterFinishedTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_finished_tasks(0, **{'assignee': cur_user})
    context['action_label'] = 'my completed'
    return context


class WriterSentTasksView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(WriterSentTasksView, self).get_context_data(**kwargs)
    cur_user = self.request.user
    context['tasks'] = Task.get_sent_tasks(0, **{'assignee': cur_user})
    context['action_label'] = 'my sent'
    return context
