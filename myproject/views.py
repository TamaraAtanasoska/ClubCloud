from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import random
import json

from django.http.response import HttpResponse
from events import get_events, get_tips
from soundcloud_connect.views import get_user_favorites

MOCK_LOCATION = True
MOCK_MATCHING = False
MOCK_FAVORITES = False


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
    if MOCK_LOCATION == True:
        lat = '52.5029'
        lng = '13.447424'
    else:
        lat=request.session['lat']
        lng=request.session['lng']

    events = get_events(lat=lat, lng=lng)
    if not MOCK_FAVORITES:
        favorites = get_user_favorites(request.user)

        with open("favorites.json", "w") as f:
            json.dump(favorites, f)
    else:
        with open("favorites.json") as f:
            favorites = json.load(f)
    matching_events = match_user_events(favorites, events)
    return render_to_response('yourevents.html', {'events': matching_events})


def match_user_events(favorites, events):
    # TODO optimize
    matching_events = []

    #favorites = [favorite for favorite in favorites_orig if favorite['genre'] and favorite['user_username']]
    artists = set([])

    uniq_per_artist = []
    for favorite in favorites:
        if favorite['user_username'] not in artists:
            uniq_per_artist.append(favorite)
            artists.add(favorite['user_username'])
    if MOCK_MATCHING:
        num_of_mock_events = 5
        num_of_mock_events = len(events) if num_of_mock_events > len(events) else num_of_mock_events
        match_events = random.sample(events, num_of_mock_events)
        matching_events = []
        for event, favorite in zip(match_events, uniq_per_artist):
            event.update(favorite)
            matching_events.append(event)
    else:
        for favorite in uniq_per_artist:
            for event in events:
                if match_artist_event(event['participants'], favorite['user_username']):
                    event.update(favorite)
                    matching_events.append(event)
    distance = 1.5
    for event in matching_events:
        if not event['genre']:
            event['genre']  = 'Techno'
        event['distance'] = str(distance)
        distance += 0.2
    return matching_events


def home(request):
    return render_to_response('home.html', {})


def match_artist_event(participants, artist):
    for p in participants:
        if p.lower() in artist.lower() or artist.lower() in p.lower():
            return True
    return False

def detail(request):
    return render_to_response('detail.html', {})

def location(request):
    return render_to_response('location.html', {})
def livefeed(request):
    return render_to_response('livefeed.html', {})
def listen(request):
    return render_to_response('listen.html', {})
def atmoshphere(request):
    return render_to_response('atmosphere.html', {})

