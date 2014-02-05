from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tasks.views import CategoriesView

urlpatterns = patterns('',
    url(r'^$', CategoriesView.as_view()),
    url(r'^tasks/$', CategoriesView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
