from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tasks.views import CategoriesView, TaskView

urlpatterns = patterns('',
    url(r'^$', CategoriesView.as_view()),

    url(r'^category/$', CategoriesView.as_view(), name='all_tasks'),
    url(r'^category/(?P<category_id>\d{0,4})$', CategoriesView.as_view(), name='tasks_by_category'),
    url(r'^task/(?P<pk>\d+)$', TaskView.as_view(), name='task_by_id'),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^test/', BaseView.as_view(template_name='test/index.html'),{'module_path':'test'}),
)
