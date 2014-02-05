from django.views.generic.list import ListView

from tasks.models import Categories

class TasksView(ListView):
  model = Categories
