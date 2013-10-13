from django.conf.urls import patterns, include, url
from soundcloud_connect.views import get_soundcloud_artists, get_soundcloud_favorites, get_track

urlpatterns = patterns('',
    url(r'^artists/', get_soundcloud_artists),
    url(r'^favorites/', get_soundcloud_favorites),
    url(r'^track/', get_track),
)

