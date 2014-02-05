from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tasks.views import CategoriesView
from general.views import BaseView, FileView

urlpatterns = patterns('',
    url(r'^$', CategoriesView.as_view()),
    url(r'^tasks/$', CategoriesView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^file/(?P<module>[a-z]+)/(?P<file>[a-zA-Z0-9_.-]+)/$',FileView.as_view(),{'module_path':'file'}),
    url(r'^test/', BaseView.as_view(template_name='test/index.html'),{'module_path':'test'}),
)
