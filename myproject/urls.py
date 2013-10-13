from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^callback/$', 'myproject.views.callback'),
    url(r'^feed/$', TemplateView.as_view(template_name="feed.html")),
    url(r'^geo/$', 'myproject.views.geo'),
    url(r'^where_to_go/$', 'myproject.views.get_my_favorite_venues'),
    # url(r'^$', 'myproject.views.home', name='home'),
    url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('soundcloud/', include('soundcloud_connect.urls', namespace='soundcloud_connect')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
