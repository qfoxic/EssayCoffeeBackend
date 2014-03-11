from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()
import constants as co

from general.views import TaskIndexView, UpdateTaskView, CreateTaskView
from general.views import RemoveTaskView, DetailTaskView
from customer.views import CustomerTaskView,CustomerCreateDraftTaskView,CustomerUpdateTaskView
from customer.views import CustomerDetailTaskView,CustomerSubmitTaskView

from userprofile.views import CreateProfileWriterView, DetailProfileWriterView
from userprofile.views import CreateProfileCustomerView, DetailProfileCustomerView, UpdateProfileCustomerView
from userprofile.views import RemoveProfileView, UpdateProfileWriterView

from comments.views import CreateCommentView, RemoveCommentView
from general.views import LoginView, LogoutView, ResetPswdView
from general.views import ResetPswdDoneView, ResetPswdConfirmView, ResetPswdCompleteView

task_rm = login_required(
    permission_required('general.delete_task', raise_exception=True)(RemoveTaskView.as_view()),
    login_url=reverse_lazy('login'))

comment_new = login_required(
    permission_required('comments.add_comment', raise_exception=True)(CreateCommentView.as_view()),
    login_url=reverse_lazy('login'))
comment_rm = login_required(
    permission_required('comments.delete_comment', raise_exception=True)(RemoveCommentView.as_view()),
    login_url=reverse_lazy('login'))

user_new = CreateProfileCustomerView.as_view()
user_details = login_required(DetailProfileCustomerView.as_view(), login_url=reverse_lazy('login'))
user_edit = login_required(UpdateProfileCustomerView.as_view(), login_url=reverse_lazy('login'))
user_remove = login_required(RemoveProfileView.as_view(), login_url=reverse_lazy('login'))

task_list = login_required(CustomerTaskView.as_view(), login_url=reverse_lazy('login'))
task_details = CustomerDetailTaskView.as_view()
task_new = login_required(
  permission_required('general.add_task', raise_exception=True)(CustomerCreateDraftTaskView.as_view()),
  login_url=reverse_lazy('login'))
task_submit = login_required(
  permission_required('general.change_task', raise_exception=True)(CustomerSubmitTaskView.as_view()),
  login_url=reverse_lazy('login'))
task_update = login_required(
  permission_required('general.change_task', raise_exception=True)(CustomerUpdateTaskView.as_view()),
  login_url=reverse_lazy('login'))

urlpatterns = patterns('',
    url(r'^$', task_list),
    url(r'^tasks/$', task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', task_details, name='task_view'),
    url(r'^task/(?P<pk>\d+)/remove$', task_rm, name='task_remove'),
    url(r'^task/new$', task_new, name='task_new'),
    url(r'^task/(?P<pk>\d+)/edit$', task_update, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/submit$', task_submit, name='task_submit'),

    url(r'^comment/(?P<task_id>\d+)/new$', comment_new, name='comment_new'),
    url(r'^comment/(?P<pk>\d+)/remove$', comment_rm, name='comment_remove'),

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
