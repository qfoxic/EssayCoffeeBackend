from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from general.views import RemoveTaskView,SwitchStatusView
from general.views import CreateTaskView,UpdateTaskView,DetailTaskView,TaskIndexView
from general.models import Task
from msgs.views import CreateMsgView, RemoveMsgView, ListMsgsView,DetailMsgView
from ftpstorage.views import UploadFileView,RemoveUploadView,UpdateUploadView 


from userprofile.views import CreateProfileView, UpdateProfileView

import constants as co

task_rm = login_required(RemoveTaskView.as_view(), login_url=reverse_lazy('login'))

msg_add = login_required(CreateMsgView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
msg_rm = login_required(RemoveMsgView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
msg_list = login_required(ListMsgsView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
msg_detail = login_required(DetailMsgView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
upload_file = login_required(UploadFileView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
upload_rm = login_required(RemoveUploadView.as_view(module_name='customer'), login_url=reverse_lazy('login'))
#upload_visibility = login_required(UpdateUploadView.as_view(module_name='customer'), login_url=reverse_lazy('login'))

user_new = CreateProfileView.as_view(module_name='customer',
                                     group_name=co.CUSTOMER_GROUP)
user_edit = login_required(UpdateProfileView.as_view(module_name='customer'),
                           login_url=reverse_lazy('login'))

task_list = lambda request: login_required(
    TaskIndexView.as_view(module_name='customer', action_label='my orders',
                          queryset=Task.get_all_tasks(0, **{'owner__id': request.user.id})),
    login_url=reverse_lazy('login'))(request)
task_details = login_required(DetailTaskView.as_view(module_name='customer', owner_required=True),
                              login_url=reverse_lazy('login'))
task_new = login_required(
  CreateTaskView.as_view(module_name='customer'),
  login_url=reverse_lazy('login'))
task_status = login_required(
  SwitchStatusView.as_view(module_name='customer'),
  login_url=reverse_lazy('login'))
task_update = login_required(
  UpdateTaskView.as_view(module_name='customer'),
  login_url=reverse_lazy('login'))

urlpatterns = patterns('',
    url(r'^$', task_list),
    url(r'^tasks/$', task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/remove$', task_rm, name='task_remove'),
    url(r'^task/new$', task_new, name='task_new'),
    url(r'^task/(?P<pk>\d+)/edit$', task_update, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/status$', task_status, name='task_status'),

    url(r'^msg/(?P<task_id>\d+)/new$', msg_add, name='msg_add'),
    #url(r'^msg/(?P<pk>\d+)/remove$', msg_rm, name='msg_remove'),
    url(r'^msgs/$', msg_list, name='msgs_list'),
    url(r'^msg/(?P<pk>\d+)/$', msg_detail, name='msg_detail'),

    url(r'^upload/(?P<task_id>\d+)/new$', upload_file, name='upload_file'),
    url(r'^upload/(?P<pk>\d+)/remove$', upload_rm, name='upload_remove'),
    #url(r'^upload/(?P<pk>\d+)/visibility$', upload_visibility, name='upload_visibility'),

    url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_edit, name='user_details'),
    url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),

    url(r'', include('common_urls')),
)

