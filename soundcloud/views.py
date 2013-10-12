from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import requests
from social_auth.models import UserSocialAuth
from myproject.settings import SOCIAL_AUTH_SOUNDCLOUD_KEY 

@login_required
@csrf_exempt
def get_soundcloud_data(request):

    user = request.user
    soundcloud_user = UserSocialAuth.objects.filter(user__id=user.id)
    print(soundcloud_user)
    soundcloud_user_id = soundcloud_user[0].uid
    token = SOCIAL_AUTH_SOUNDCLOUD_KEY

    url = 'http://api.soundcloud.com/users/' + soundcloud_user_id + '/followings.json?client_id=' + token

    request_soundcloud = requests.get(url)
    soundcloud_data = request_soundcloud.json()
    #artists_all
    

    print(soundcloud_data)


    
    return HttpResponse(soundcloud_data)
