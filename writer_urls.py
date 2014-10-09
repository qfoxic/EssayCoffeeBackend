from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from general.views import DetailTaskView,SwitchStatusView,LockTaskView
from general.views import TaskIndexView, LoginView
from general.models import Task

from userprofile.views import DetailProfileView
from msgs.views import CreateMsgView, RemoveMsgView, ListMsgsView,DetailMsgView
from ftpstorage.views import UploadFileView,RemoveUploadView,UpdateUploadView 

import constants as co

#user_new = CreateProfileView.as_view(module_name='writer',
#                                     group_name=co.WRITER_GROUP)
user_edit = login_required(DetailProfileView.as_view(module_name='writer',
                                                     allowed_groups=[], owner_required=True),
                           login_url=reverse_lazy('login'))

tasks_list = login_required(TaskIndexView.as_view(module_name='writer',
                                                  queryset=Task.get_processing_tasks(0,
                                                    **{'assignee__isnull': True, 'access_level__in': [co.PUBLIC_ACCESS]}),
                                                  action_label='processing'),
                            login_url=reverse_lazy('login'))
tasks_unprocessed = tasks_list
tasks_active = lambda request: login_required(
    TaskIndexView.as_view(module_name='writer', action_label='my processing',
                          queryset=Task.get_processing_tasks(0, **{'assignee': request.user})),
    login_url=reverse_lazy('login'))(request)

tasks_finished = lambda request: login_required(
    TaskIndexView.as_view(module_name='writer', action_label='my finished',
                          queryset=Task.get_finished_tasks(0, **{'assignee': request.user})),
    login_url=reverse_lazy('login'))(request)

tasks_sent = lambda request: login_required(
    TaskIndexView.as_view(module_name='writer', action_label='my sent',
                          queryset=Task.get_sent_tasks(0, **{'assignee': request.user})),
    login_url=reverse_lazy('login'))(request)
tasks_all = lambda request: login_required(
    TaskIndexView.as_view(module_name='writer', action_label='my all',
                          queryset=Task.get_all_tasks(0, **{'assignee': request.user})),
    login_url=reverse_lazy('login'))(request)

tasks_expired = lambda request: login_required(
    TaskIndexView.as_view(module_name='writer', action_label='my sent',
                          queryset=Task.get_expired_tasks(0, **{'assignee': request.user})),
    login_url=reverse_lazy('login'))(request)

task_details = login_required(DetailTaskView.as_view(module_name='writer'),
                              login_url=reverse_lazy('login'))

task_lock = login_required(LockTaskView.as_view(module_name='writer'),
                           login_url=reverse_lazy('login'))

task_status = login_required(
      SwitchStatusView.as_view(module_name='writer'),
    login_url=reverse_lazy('login'))

msg_add = login_required(CreateMsgView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
msg_rm = login_required(RemoveMsgView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
msg_list = login_required(ListMsgsView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
msg_detail = login_required(DetailMsgView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
upload_file = login_required(UploadFileView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
upload_rm = login_required(RemoveUploadView.as_view(module_name='writer'), login_url=reverse_lazy('login'))
#upload_visibility = login_required(UpdateUploadView.as_view(module_name='writer'), login_url=reverse_lazy('login'))

urlpatterns = patterns('',
    url(r'^$', tasks_list),
    url(r'^tasks/$', tasks_list, name='task_list'),
    url(r'^tasks/active$', tasks_active, name='tasks_active'),
    url(r'^tasks/all$', tasks_all, name='tasks_all'),
    url(r'^tasks/processing$', tasks_unprocessed, name='tasks_unprocessed'),
    url(r'^tasks/finished$', tasks_finished, name='tasks_finished'),
    url(r'^tasks/sent$', tasks_sent, name='tasks_sent'),
    url(r'^tasks/expired$', tasks_expired, name='tasks_expired'),

    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/status$', task_status, name='task_status'),
    url(r'^task/(?P<pk>\d+)/lock$', task_lock, name='task_lock'),

    url(r'^msg/(?P<task_id>\d+)/new$', msg_add, name='msg_add'),
    #url(r'^msg/(?P<pk>\d+)/remove$', msg_rm, name='msg_remove'),
    url(r'^msg/(?P<pk>\d+)/$', msg_detail, name='msg_detail'),
    url(r'^msgs/$', msg_list, name='msgs_list'),
    url(r'^upload/(?P<task_id>\d+)/new$', upload_file, name='upload_file'),
    url(r'^upload/(?P<pk>\d+)/remove$', upload_rm, name='upload_remove'),
    #url(r'^upload/(?P<pk>\d+)/visibility$', upload_visibility, name='upload_visibility'),

    #url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_edit, name='user_details'),
    #url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),

    url(r'^login/$', LoginView.as_view(module_name='writer'), name='login'),
    url(r'', include('common_urls')),
)

