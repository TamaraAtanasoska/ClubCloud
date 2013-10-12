from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse

def callback(request):
    return render_to_response('callback.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def geo(request):
    if request.method == "POST":
        request.session['lat'] = request.POST['lat']
        request.session['lng'] = request.POST['lng']
    return render_to_response('geo.html', {'lat': request.session.get('lat', ''), 'lng': request.session.get('lng', '')})




