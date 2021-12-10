from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Preferences
from django.db import connection


@login_required
def preferences(request):
    print(request)
    data = None
    # with connection.cursor() as cur:
    #     cur.callproc('get_preferences', [request.user.id])
    #     print(cur.fetchone())
    data = Preferences.objects.get(user=request.user)

    if request.POST:
        print(request.POST)
        data.galaxies = 'galaxies' in request.POST
        data.stars = 'stars' in request.POST
        data.planets = 'planets' in request.POST
        data.blackHoles = 'blackHoles' in request.POST
        data.moons = 'moons' in request.POST
        data.save()
        return render(request, "preferences.html", {"user": request.user, "data": data, "successmsg": "Success"})

    return render(request, "preferences.html", {"user": request.user, "data": data})


@login_required
def app(request):
    return render(request, "app.html", {"user": request.user})


@login_required
def locations(request):
    return render(request, "locations.html", {"user": request.user})
