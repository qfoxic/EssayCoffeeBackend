from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tasks.views import TasksView

urlpatterns = patterns('',
    url(r'^tasks/$', TasksView),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
