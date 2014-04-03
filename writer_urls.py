from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from general.views import DetailTaskView,SwitchStatusView,LockTaskView
from writer.views import WriterTaskView,WriterActiveTasksView
from writer.views import WriterExpiredTasksView,WriterFinishedTasksView

from comments.views import CreateCommentView,RemoveCommentView 
from userprofile.views import CreateProfileView, UpdateProfileView

import constants as co

user_new = CreateProfileView.as_view(module_name='writer',
                                     group_name=co.WRITER_GROUP)
user_edit = login_required(UpdateProfileView.as_view(module_name='writer',
                                                     allowed_groups=[]),
                           login_url=reverse_lazy('login'))

tasks_list = login_required(WriterTaskView.as_view(module_name='writer'),
                            login_url=reverse_lazy('login'))
tasks_active = login_required(WriterActiveTasksView.as_view(module_name='writer'),
                              login_url=reverse_lazy('login'))
tasks_unprocessed = tasks_list
tasks_finished = login_required(WriterFinishedTasksView.as_view(module_name='writer'),
                                login_url=reverse_lazy('login'))
tasks_expired = login_required(WriterExpiredTasksView.as_view(module_name='writer'),
                               login_url=reverse_lazy('login'))

task_details = login_required(DetailTaskView.as_view(module_name='writer'),
                              login_url=reverse_lazy('login'))

task_lock = login_required(LockTaskView.as_view(module_name='writer'),
                           login_url=reverse_lazy('login'))

comment_new = login_required(
    permission_required('comments.add_comment', raise_exception=True)
      (CreateCommentView.as_view(module_name='writer')),
    login_url=reverse_lazy('login'))
comment_rm = login_required(
    permission_required('comments.delete_comment', raise_exception=True)
      (RemoveCommentView.as_view(module_name='writer')),
    login_url=reverse_lazy('login'))

task_finish = login_required(
      SwitchStatusView.as_view(module_name='writer'),
    login_url=reverse_lazy('login'))

urlpatterns = patterns('',
    url(r'^$', tasks_list),
    url(r'^tasks/$', tasks_list, name='task_list'),
    url(r'^tasks/active$', tasks_active, name='tasks_active'),
    url(r'^tasks/unprocessed$', tasks_unprocessed, name='tasks_unprocessed'),
    url(r'^tasks/finished$', tasks_finished, name='tasks_finished'),
    url(r'^tasks/expired$', tasks_expired, name='tasks_expired'),

    url(r'^comment/(?P<task_id>\d+)/new$', comment_new, name='comment_new'),
    url(r'^comment/(?P<pk>\d+)/remove$', comment_rm, name='comment_remove'),

    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/finish$', task_finish, name='task_finish'),
    url(r'^task/(?P<pk>\d+)/lock$', task_lock, name='task_lock'),

    url(r'profile/new', user_new, name='user_new'),
    url(r'profile/(?P<pk>\d+)/$', user_edit, name='user_details'),
    url(r'profile/(?P<pk>\d+)/edit$', user_edit, name='user_edit'),

    url(r'', include('common_urls')),
)

