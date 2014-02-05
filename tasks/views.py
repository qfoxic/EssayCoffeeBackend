from django.views.generic.list import ListView

from tasks.models import Categories

class CategoriesView(ListView):
  model = Categories
