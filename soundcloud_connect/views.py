from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import requests
from social.apps.django_app.default.models import UserSocialAuth
from myproject.settings import SOCIAL_AUTH_SOUNDCLOUD_KEY
import soundcloud

@login_required
@csrf_exempt
def get_soundcloud_artists(request):

    user = request.user
    soundcloud_user = UserSocialAuth.objects.filter(user__id=user.id)
    soundcloud_user_id = soundcloud_user[0].uid
    token = SOCIAL_AUTH_SOUNDCLOUD_KEY

    url = 'http://api.soundcloud.com/users/' + soundcloud_user_id + '/followings.json?client_id=' + token

    request_soundcloud = requests.get(url)
    soundcloud_data = request_soundcloud.json()
    artists = []
    for artist in soundcloud_data:
        artists.append({
                        'id':artist['id'],
                        'username': artist['username'],   
                        'full_name': artist['full_name'],   
                        'image_url':artist['avatar_url'],
                        'link_to_profile':artist['uri'],
                      })
    
    return HttpResponse(soundcloud_data)


@login_required
@csrf_exempt
def get_track(request):
    permalink = request.GET.get('link')
    permalink = "http://soundcloud.com/forss/flickermood"
    if not permalink:
        return HttpResponse("Please provide song link")
    user = request.user

    client = soundcloud.Client(client_id=SOCIAL_AUTH_SOUNDCLOUD_KEY)

    embed_info = client.get('/oembed', url=permalink)

    return render_to_response({'embed_player': embed_info['html']})


@login_required
@csrf_exempt
def get_soundcloud_favorites(request):

    user = request.user

    return HttpResponse(get_user_favorites(user))


def get_user_favorites(user):
    try:
        soundcloud_user = UserSocialAuth.objects.get(user__id=user.id)
    except UserSocialAuth.DoesNotExist:
        return []
    soundcloud_user_id = soundcloud_user.uid
    token = SOCIAL_AUTH_SOUNDCLOUD_KEY

    url = 'http://api.soundcloud.com/users/' + soundcloud_user_id + '/favorites.json?client_id=' + token

    request_soundcloud = requests.get(url)
    soundcloud_data = request_soundcloud.json()
    favorites = []

    for favorite in soundcloud_data:
        favorites.append({
                        'track_id':favorite['id'],
                        'track_url':favorite['permalink_url'],
                        'track_title': favorite['title'],
                        'track_favorites':favorite['favoritings_count'],
                        'track_is_downloadable':favorite['downloadable'],
                        'track_downloads':favorite['download_count'],
                        'track_playings':favorite['playback_count'],
                        'genre': favorite['genre'],
                        'user_id': favorite['user']['id'],
                        'user_username': favorite['user']['username'],
                        'user_image_url': favorite['user']['avatar_url'],
                        'user_link_to_profile': favorite['user']['uri'],
                        'user_permalink': favorite['user']['permalink'],
                      })
    return favorites