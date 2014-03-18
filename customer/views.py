from general.models import Task
from general.views import TaskIndexView
import constants as co


class CustomerTaskView(TaskIndexView):
  def get_context_data(self, **kwargs):
    context = super(CustomerTaskView, self).get_context_data(**kwargs)
    owner = self.request.user
    context['tasks'] = Task.objects.filter(owner__exact=owner)
    return context

