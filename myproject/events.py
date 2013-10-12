import requests


venue_search = 'https://api.foursquare.com/v2/venues/search'

params = {
    'client_id': 'EU2SUKKZBUJQMOBXNJ543EKWIECOAMAYAKGLQPGI20AT02CM',
    'client_secret': 'JHDQSR2RIIBVLYYJZNMNWIHNC3BZXY1CEUZK1342ZY3B53ID',
    'v': '20130815',
}


venues_search_params = params.copy()
venues_search_params.update(
    # category NightClub
    {'categoryId': '4bf58dd8d48988d11f941735'})


def get_events():
    resp = requests.get(venue_search, params=venues_search_params)
    response = resp.json()['response']
    venues_with_events = [vn for vn in  response['venues'] if vn.get('events')]
    events = []
    for venue_with_event in venues_with_events:
        events.append({
            'participants': [pt['participant']['displayName'] for pt in venue_with_event['events']['items'][0]['participants']],
            'venue_name':  venue_with_event['name'],
            # 'summary': venue_with_event['events']['summary'],
            'event_name' : venue_with_event['events']['items'][0]['name'],
            'lng': venue_with_event['location']['lng'],
            'lat': venue_with_event['location']['lat'],
        })
    return events