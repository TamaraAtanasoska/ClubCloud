from django.shortcuts import render_to_response

def callback(request):
    return render_to_response('callback.html')

def geo(request):
    return render_to_response('geo.html')
