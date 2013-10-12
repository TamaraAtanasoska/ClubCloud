from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse
from events import get_events, get_tips
from soundcloud.views import get_user_favorites

def callback(request):
    return render_to_response('callback.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def geo(request):
    if request.method == "POST":
        request.session['lat'] = request.POST['lat']
        request.session['lng'] = request.POST['lng']
    return render_to_response('geo.html', {'lat': request.session.get('lat', ''), 'lng': request.session.get('lng', '')})



@login_required
@csrf_exempt
def get_my_favorite_venues(request):
    # TODO check no session
    events = get_events(lat=request.session['lat'], lng=request.session['lng'])
    favorites = get_user_favorites(request.user)
    pass


def match_user_events(favorites, events):
    # TODO optimize
    favorite_events = []
    for favorite in favorites:
        for event in events:
            if favorite['user_username'] in event['participants']:
                favorite_events.append()