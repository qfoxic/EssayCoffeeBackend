from general.models import Task
from general.views import TaskIndexView
import constants as co

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


