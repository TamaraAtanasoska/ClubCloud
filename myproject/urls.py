from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^callback/$', 'myproject.views.callback'),
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('soundcloud/', include('soundcloud.urls', namespace='soundcloud')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
