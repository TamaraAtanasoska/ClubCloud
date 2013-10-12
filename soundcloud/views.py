from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import requests
from social.apps.django_app.default.models import UserSocialAuth
from myproject.settings import SOCIAL_AUTH_SOUNDCLOUD_KEY 

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
    
    return HttpResponse(artists)

@login_required
@csrf_exempt
def get_soundcloud_favorites(request):

    user = request.user
    soundcloud_user = UserSocialAuth.objects.filter(user__id=user.id)
    soundcloud_user_id = soundcloud_user[0].uid
    token = SOCIAL_AUTH_SOUNDCLOUD_KEY

    url = 'http://api.soundcloud.com/users/' + soundcloud_user_id + '/favorites.json?client_id=' + token

    request_soundcloud = requests.get(url)
    soundcloud_data = request_soundcloud.json()
    favorites = []
    for favorite in soundcloud_data:
        favorites.append({
                        'id':favorite['id'],
                        'track_title': favorite['title'],   
                        'user_id': favorite['user']['id'],   
                        'user_username': favorite['user']['username'],   
                        'user_image_url': favorite['user']['avatar_url'],   
                        'user_link_to_profile': favorite['user']['uri'],   
                        'user_permalink': favorite['user']['permalink'],   
                      })
    return HttpResponse(favorites)

