from django.views.generic.list import ListView

from tasks.models import TasksTree

class TasksView(ListView):
  model = TasksTree
