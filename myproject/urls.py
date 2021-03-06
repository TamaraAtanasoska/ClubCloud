from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from events import get_photos

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^callback/$', 'myproject.views.callback'),
    url(r'^photos/$', get_photos),
    url(r'^geo/$', 'myproject.views.geo'),
    url(r'^dashboard/$', 'myproject.views.get_my_favorite_venues'),
    url(r'^dashboard/location/$', 'myproject.views.location'),
    url(r'^dashboard/livefeed/$', 'myproject.views.livefeed'),
    url(r'^dashboard/listen/$', 'myproject.views.listen'),
    url(r'^dashboard/atmosphere/$', 'myproject.views.atmosphere'),
    url(r'^detail/$', 'myproject.views.detail'),
    # url(r'^$', 'myproject.views.home', name='home'),
    url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('soundcloud/', include('soundcloud_connect.urls', namespace='soundcloud_connect')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
