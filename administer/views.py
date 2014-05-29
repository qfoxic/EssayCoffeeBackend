from general.views import UpdateTaskView
from general.forms import ForceSwitchStatusForm


class AdminForceSwitchStatusView(UpdateTaskView):
  form_class = ForceSwitchStatusForm 
  template_name = 'tasks/details.html'
  owner_required = False 
  
  def _check_permissions(self):
    pass  
  
  def get_success_url(self):
    return self.object.to_link()

