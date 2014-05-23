import tempfile
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
from django.http import (CompatibleStreamingHttpResponse, Http404,
    HttpResponse, HttpResponseRedirect, HttpResponseNotModified)
from general.views import LoginView, LogoutView, ResetPswdView, StaticHtmlView
from general.views import ResetPswdDoneView, ResetPswdConfirmView, ResetPswdCompleteView
from ftpstorage.storage import FTPStorage 
from django.views.static import serve as djserve
from userprofile.views import RemoveProfileView

def serve(request, path, document_root=None, show_indexes=False):
    ftp = FTPStorage()
    if not ftp.exists(path):
        raise Http404(_('"%(path)s" does not exist') % {'path': path})
    tmp_file = tempfile.NamedTemporaryFile() 
    ftp.cp(path, tmp_file)
    return djserve(request, tmp_file.name, '/')


user_remove = login_required(RemoveProfileView.as_view(), login_url=reverse_lazy('login'))
urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^reset/$', ResetPswdView.as_view(), name='pswd_reset'),
    url(r'^resetdone/$', ResetPswdDoneView.as_view(), name='pswd_reset_done'),
    url(r'^resetconfirm/(?P<uidb64>.*)/(?P<token>.*)$', ResetPswdConfirmView.as_view(), name='pswd_reset_confirm'),
    url(r'^resetcomplete/$', ResetPswdCompleteView.as_view(), name='pswd_reset_complete'),
    url(r'^html/(?P<path>.*)$', StaticHtmlView.as_view(), name='html'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'profile/(?P<pk>\d+)/remove$', user_remove, name='user_remove'),
    (r'^media/(?P<path>.*)$', serve),
)

