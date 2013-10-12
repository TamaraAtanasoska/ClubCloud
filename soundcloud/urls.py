from django.conf.urls import patterns, include, url
from soundcloud.views import get_soundcloud_artists, get_soundcloud_favorites

urlpatterns = patterns('',
    url(r'^artists/', get_soundcloud_artists),
    url(r'^favorites/', get_soundcloud_favorites),
)

