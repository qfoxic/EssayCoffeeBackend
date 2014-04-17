from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from general.views import DetailTaskView,SwitchStatusView,LockTaskView,UnlockTaskView
from general.views import TaskIndexView,UpdateTaskView
from general.models import Task

from reports.views import CreateReportView,RemoveReportView 

from administer.views import AdminForceSwitchStatusView

from userprofile.views import CreateProfileView, UpdateProfileView, ListProfileView
from userprofile.models import UserProfile
from msgs.views import CreateMsgView, RemoveMsgView, ListMsgsView,DetailMsgView
from ftpstorage.views import UploadFileView,RemoveUploadView 

import constants as co

writers = login_required(ListProfileView.as_view(module_name='administer',
                         queryset=UserProfile.objects.filter(groups__name=co.WRITER_GROUP),
                         action_label='writers', context_object_name='users'),
                         login_url=reverse_lazy('login'))
customers = login_required(ListProfileView.as_view(module_name='administer',
                           queryset=UserProfile.objects.filter(groups__name=co.CUSTOMER_GROUP),
                           action_label='customers', context_object_name='users'),
                           login_url=reverse_lazy('login'))
editors = login_required(ListProfileView.as_view(module_name='administer',
                         queryset=UserProfile.objects.filter(groups__name=co.EDITOR_GROUP),
                         action_label='editors', context_object_name='users'),
                         login_url=reverse_lazy('login'))
admins = login_required(ListProfileView.as_view(module_name='administer',
                        queryset=UserProfile.objects.filter(groups__name=co.ADMIN_GROUP),
                        action_label='admins', context_object_name='users'),
                        login_url=reverse_lazy('login'))
user_new = CreateProfileView.as_view(module_name='administer',
                                     group_name=co.ADMIN_GROUP)
user_edit = login_required(UpdateProfileView.as_view(module_name='administer',
                                                     allowed_groups=[co.WRITER_GROUP,co.CUSTOMER_GROUP]),
                           login_url=reverse_lazy('login'))


msg_add = login_required(CreateMsgView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
msg_rm = login_required(RemoveMsgView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
msg_list = login_required(ListMsgsView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
msg_detail = login_required(DetailMsgView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
upload_file = login_required(UploadFileView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
upload_rm = login_required(RemoveUploadView.as_view(module_name='administer'), login_url=reverse_lazy('login'))
report_new = login_required(
    CreateReportView.as_view(module_name='administer'),
    login_url=reverse_lazy('login'))
report_rm = login_required(
    RemoveReportView.as_view(module_name='administer'),
    login_url=reverse_lazy('login'))

tasks_list = login_required(TaskIndexView.as_view(module_name='administer',
                                                  queryset=Task.get_unprocessed_tasks(0),
                                                  action_label='unprocessed'),
                            login_url=reverse_lazy('login'))
tasks_active = login_required(TaskIndexView.as_view(module_name='administer',
                                                    queryset=Task.get_processing_tasks(0),
                                                    action_label='active'),
                              login_url=reverse_lazy('login'))
tasks_rejected = login_required(TaskIndexView.as_view(module_name='administer',
                                                      queryset=Task.get_rejected_tasks(0),
                                                      action_label='rejected'),
                                login_url=reverse_lazy('login'))
tasks_suspicious = login_required(TaskIndexView.as_view(module_name='administer',
                                                      queryset=Task.get_suspicious_tasks(0),
                                                      action_label='suspicious'),
                                  login_url=reverse_lazy('login'))
tasks_unprocessed = tasks_list
tasks_finished = login_required(TaskIndexView.as_view(module_name='administer',
                                                      queryset=Task.get_finished_tasks(0),
                                                      action_label='finished'),
                                login_url=reverse_lazy('login'))
tasks_sent = login_required(TaskIndexView.as_view(module_name='administer',
                                                  queryset=Task.get_sent_tasks(0),
                                                  action_label='sent'),
                            login_url=reverse_lazy('login'))
tasks_expired = login_required(TaskIndexView.as_view(module_name='administer',
                                                     queryset=Task.get_expired_tasks(0),
                                                     action_label='expired'),
                               login_url=reverse_lazy('login'))

task_details = login_required(DetailTaskView.as_view(module_name='administer'),
                              login_url=reverse_lazy('login'))
task_update = login_required(
  UpdateTaskView.as_view(module_name='administer', owner_required=False),
  login_url=reverse_lazy('login'))

task_status = login_required(
    SwitchStatusView.as_view(module_name='administer'),
    login_url=reverse_lazy('login'))

task_force_status = login_required(
    AdminForceSwitchStatusView.as_view(module_name='administer'),
    login_url=reverse_lazy('login'))

task_lock = login_required(LockTaskView.as_view(module_name='administer'),
                           login_url=reverse_lazy('login'))
task_unlock = login_required(UnlockTaskView.as_view(module_name='administer'),
                             login_url=reverse_lazy('login'))

urlpatterns = patterns('',
    url(r'^$', tasks_list),
    url(r'^tasks/$', tasks_list, name='task_list'),
    url(r'^tasks/active$', tasks_active, name='tasks_active'),
    url(r'^tasks/rejected$', tasks_rejected, name='tasks_rejected'),
    url(r'^tasks/suspicious$', tasks_suspicious, name='tasks_suspicious'),
    url(r'^tasks/unprocessed$', tasks_unprocessed, name='tasks_unprocessed'),
    url(r'^tasks/finished$', tasks_finished, name='tasks_finished'),
    url(r'^tasks/sent$', tasks_sent, name='tasks_sent'),
    url(r'^tasks/expired$', tasks_expired, name='tasks_expired'),

    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/status$', task_status, name='task_status'),
    url(r'^task/(?P<pk>\d+)/fstatus$', task_force_status, name='task_force_status'),
    url(r'^task/(?P<pk>\d+)/edit$', task_update, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/lock$', task_lock, name='task_lock'),
    url(r'^task/(?P<pk>\d+)/unlock$', task_unlock, name='task_unlock'),

    url(r'^msg/(?P<task_id>\d+)/new$', msg_add, name='msg_add'),
    url(r'^msg/(?P<pk>\d+)/remove$', msg_rm, name='msg_remove'),
    url(r'^msgs/$', msg_list, name='msgs_list'),
    url(r'^msg/(?P<pk>\d+)/$', msg_detail, name='msg_detail'),

    url(r'^upload/(?P<task_id>\d+)/new$', upload_file, name='upload_file'),
    url(r'^upload/(?P<pk>\d+)/remove$', upload_rm, name='upload_remove'),

    url(r'^report/(?P<task_id>\d+)/new$', report_new, name='report_new'),
    url(r'^report/(?P<pk>\d+)/remove$', report_rm, name='report_remove'),

    url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_edit, name='user_details'),
    url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),

    url(r'^writers/$', writers, name='writers'),
    url(r'^customers/$', customers, name='customers'),
    url(r'^editors/$', editors, name='editors'),
    url(r'^admins/$', admins, name='admins'),

    url(r'', include('common_urls')),
)

