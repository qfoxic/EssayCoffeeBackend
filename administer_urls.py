from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()
import constants as co

from general.views import UpdateTaskView

from administer.views import AdminActiveTasksView, AdminRejectedTasksView, AdminUnprocessedTasksView, AdminFinishedTasksView 
from administer.views import AdminDetailTaskView 
from administer.views import AdminDetailProfileView,AdminUpdateProfileView,AdminCreateProfileView 
from administer.views import AdminApproveTaskView, AdminRejectTaskView 

from userprofile.views import RemoveProfileView

from general.views import LoginView, LogoutView, ResetPswdView
from general.views import ResetPswdDoneView, ResetPswdConfirmView, ResetPswdCompleteView


user_new = AdminCreateProfileView.as_view()
user_remove = login_required(RemoveProfileView.as_view(), login_url=reverse_lazy('login'))
user_details = login_required(AdminDetailProfileView.as_view(), login_url=reverse_lazy('login'))
user_edit = login_required(AdminUpdateProfileView.as_view(), login_url=reverse_lazy('login'))

task_list = login_required(AdminUnprocessedTasksView.as_view(), login_url=reverse_lazy('login'))
tasks_active = login_required(AdminActiveTasksView.as_view(), login_url=reverse_lazy('login'))
tasks_rejected = login_required(AdminRejectedTasksView.as_view(), login_url=reverse_lazy('login'))
tasks_unprocessed = login_required(AdminUnprocessedTasksView.as_view(), login_url=reverse_lazy('login'))
tasks_finished = login_required(AdminFinishedTasksView.as_view(), login_url=reverse_lazy('login'))

task_details = AdminDetailTaskView.as_view()
task_approve = login_required(
    permission_required('general.change_task', raise_exception=True)(AdminApproveTaskView.as_view()),
    login_url=reverse_lazy('login'))
task_reject = login_required(
    permission_required('general.change_task', raise_exception=True)(AdminRejectTaskView.as_view()),
    login_url=reverse_lazy('login'))
task_update = login_required(
    permission_required('general.change_task', raise_exception=True)(UpdateTaskView.as_view()),
    login_url=reverse_lazy('login'))


urlpatterns = patterns('',
    url(r'^$', task_list),
    url(r'^tasks/$', task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/approve$', task_approve, name='task_approve'),
    url(r'^task/(?P<pk>\d+)/reject$', task_reject, name='task_reject'),
    url(r'^tasks/active$', tasks_active, name='tasks_active'),
    url(r'^tasks/rejected$', tasks_rejected, name='tasks_rejected'),
    url(r'^tasks/unprocessed$', tasks_unprocessed, name='tasks_unprocessed'),
    url(r'^tasks/finished$', tasks_finished, name='tasks_finished'),

    url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_details, name='user_details'),
    url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),
    url(r'profile/(?P<pk>\d+)/remove', user_remove, name='user_remove'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^reset/$', ResetPswdView.as_view(), name='pswd_reset'),
    url(r'^resetdone/$', ResetPswdDoneView.as_view(), name='pswd_reset_done'),
    url(r'^resetconfirm/(?P<uidb64>.*)/(?P<token>.*)$', ResetPswdConfirmView.as_view(), name='pswd_reset_confirm'),
    url(r'^resetcomplete/$', ResetPswdCompleteView.as_view(), name='pswd_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)


# Displays uploaded files.
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

