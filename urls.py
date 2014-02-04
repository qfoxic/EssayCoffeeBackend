from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tasks.views import TasksView

urlpatterns = patterns('',
    url(r'^$', TasksView.as_view()),
    url(r'^tasks/$', TasksView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
