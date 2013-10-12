from django.conf.urls import patterns, include, url
from soundcloud.views import get_soundcloud_data

urlpatterns = patterns('',
    url(r'^data/', get_soundcloud_data),
)

