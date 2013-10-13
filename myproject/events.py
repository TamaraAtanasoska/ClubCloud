import requests


venue_search = 'https://api.foursquare.com/v2/venues/search'
venue_explore = 'https://api.foursquare.com/v2/venues/explore'

params = {
    'client_id': 'EU2SUKKZBUJQMOBXNJ543EKWIECOAMAYAKGLQPGI20AT02CM',
    'client_secret': 'JHDQSR2RIIBVLYYJZNMNWIHNC3BZXY1CEUZK1342ZY3B53ID',
    'v': '20130815',
}

venue_explore_params = params.copy()
venue_explore_params.update(

)

venues_search_params = params.copy()
venues_search_params.update(
    # category NightClub
    {'categoryId': '4bf58dd8d48988d11f941735'})

MOCK_EVENTS = [
    {
            'participants': ['kollektiv turmstrasse'],
            'venue_name':  'Ritter Butzke',
            # 'summary': venue_with_event['events']['summary'],
            'id': '4aeca2a8f964a520b6c921e3',
            'event_name' : 'Kollektiv Turmstrasse',
            'lng': '13.39062251962172',
            'lat': '52.51496666046718',
    },
    {
            'participants': ['butch'],
            'venue_name':  'Watergate Club',
            # 'summary': venue_with_event['events']['summary'],
            'id': '4adcda7bf964a520284721e3',
            'event_name' : 'butch',
            'lng': '13.39062251962172',
            'lat': '52.51496666046718',
    },
    {
            'participants': ['djtennis'],
            'venue_name':  'Berghain',
            # 'summary': venue_with_event['events']['summary'],
            'id': '4ae778a5f964a520a5ab21e3',
            'event_name' : 'Dj Tennis',
            'lng': '13.445209340768438',
            'lat': '52.501070081112715',
    },
]

def explore_events(lat=None, lng=None, address=None):
    if (not lat or not lng) and not address:
        raise Exception("NO ADDRESS provided")
    if lat and lng:
        location = {'ll': str(lat) + ',' + str(lng)}
    else:
        location = {'near': address}
    venue_explore_params.update(location)

def get_events(lat=None, lng=None, address=None):
    if (not lat or not lng) and not address:
        raise Exception("NO ADDRESS provided")
    if lat and lng:
        location = {'ll': str(lat) + ',' + str(lng)}
    else:
        location = {'near': address}
    return MOCK_EVENTS
    venues_search_params.update(location)
    resp = requests.get(venue_search, params=venues_search_params)
    response = resp.json()['response']
    venues_with_events = [vn for vn in  response['venues'] if vn.get('events')]
    events = []

    for venue_with_event in venues_with_events:
        if not venue_with_event['events'].get('items'):
            print "skipping event: %s" % venue_with_event['events']
            continue
        events.append({
            'participants': [pt['participant']['displayName'] for pt in venue_with_event['events']['items'][0]['participants']],
            'venue_name':  venue_with_event['name'],
            # 'summary': venue_with_event['events']['summary'],
            'id': venue_with_event['id'],
            'event_name' : venue_with_event['events']['items'][0]['name'],
            'lng': venue_with_event['location']['lng'],
            'lat': venue_with_event['location']['lat'],
        })
    return events


def get_tips(venue_id):
    # venue_id = '4ae778a5f964a520a5ab21e3'
    venue_tips = "https://api.foursquare.com/v2/venues/" + str(venue_id) + "/tips"
    resp = requests.get(venue_tips, params=params)
    tips_json = resp.json()
    return tips_json['response']['tips']['items']
# TODO get venue by name
#


