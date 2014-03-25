from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from general.views import SwitchStatusView,DetailTaskView

from comments.views import CreateCommentView,RemoveCommentView 

from administer.views import AdminActiveTasksView,AdminRejectedTasksView,AdminUnprocessedTasksView,AdminFinishedTasksView 
from administer.views import AdminSuspiciousTasksView,AdminWritersView,AdminUpdateTaskView,AdminCustomersView,AdminExpiredTasksView

from userprofile.views import CreateProfileView, UpdateProfileView

import constants as co

writers = login_required(AdminWritersView.as_view(module_name='administer'),
                         login_url=reverse_lazy('login'))
customers = login_required(AdminCustomersView.as_view(module_name='administer'),
                           login_url=reverse_lazy('login'))
user_new = CreateProfileView.as_view(module_name='administer',
                                     group_name=co.ADMIN_GROUP)
user_edit = login_required(UpdateProfileView.as_view(module_name='administer',
                                                     allowed_groups=[co.WRITER_GROUP,co.CUSTOMER_GROUP]),
                           login_url=reverse_lazy('login'))

comment_new = login_required(
    permission_required('comments.add_comment', raise_exception=True)
      (CreateCommentView.as_view(module_name='customer')),
    login_url=reverse_lazy('login'))
comment_rm = login_required(
    permission_required('comments.delete_comment', raise_exception=True)
      (RemoveCommentView.as_view(module_name='customer')),
    login_url=reverse_lazy('login'))

tasks_list = login_required(AdminUnprocessedTasksView.as_view(module_name='administer'),
                            login_url=reverse_lazy('login'))
tasks_active = login_required(AdminActiveTasksView.as_view(module_name='administer'),
                              login_url=reverse_lazy('login'))
tasks_rejected = login_required(AdminRejectedTasksView.as_view(module_name='administer'),
                                login_url=reverse_lazy('login'))
tasks_suspicious = login_required(AdminSuspiciousTasksView.as_view(module_name='administer'),
                                  login_url=reverse_lazy('login'))
tasks_unprocessed = tasks_list
tasks_finished = login_required(AdminFinishedTasksView.as_view(module_name='administer'),
                                login_url=reverse_lazy('login'))
tasks_expired = login_required(AdminExpiredTasksView.as_view(module_name='administer'),
                               login_url=reverse_lazy('login'))

task_details = login_required(DetailTaskView.as_view(module_name='administer'),
                              login_url=reverse_lazy('login'))
task_update = login_required(
  permission_required('general.change_task', raise_exception=True)
    (AdminUpdateTaskView.as_view(module_name='administer')),
  login_url=reverse_lazy('login'))

task_approve = login_required(
    permission_required('general.change_task', raise_exception=True)
      (SwitchStatusView.as_view(module_name='administer')),
    login_url=reverse_lazy('login'))
task_reject = task_approve
task_suspect = task_approve


urlpatterns = patterns('',
    url(r'^$', tasks_list),
    url(r'^tasks/$', tasks_list, name='task_list'),
    url(r'^tasks/active$', tasks_active, name='tasks_active'),
    url(r'^tasks/rejected$', tasks_rejected, name='tasks_rejected'),
    url(r'^tasks/suspicious$', tasks_suspicious, name='tasks_suspicious'),
    url(r'^tasks/unprocessed$', tasks_unprocessed, name='tasks_unprocessed'),
    url(r'^tasks/finished$', tasks_finished, name='tasks_finished'),
    url(r'^tasks/expired$', tasks_expired, name='tasks_expired'),

    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/approve$', task_approve, name='task_approve'),
    url(r'^task/(?P<pk>\d+)/reject$', task_reject, name='task_reject'),
    url(r'^task/(?P<pk>\d+)/suspect$', task_suspect, name='task_suspect'),
    url(r'^task/(?P<pk>\d+)/edit$', task_update, name='task_edit'),

    url(r'^comment/(?P<task_id>\d+)/new$', comment_new, name='comment_new'),
    url(r'^comment/(?P<pk>\d+)/remove$', comment_rm, name='comment_remove'),

    url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_edit, name='user_details'),
    url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),

    url(r'^writers/$', writers, name='writers'),
    url(r'^customers/$', customers, name='customers'),

    url(r'', include('common_urls')),
)

