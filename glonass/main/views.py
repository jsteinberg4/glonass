from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Preferences


@login_required
def preferences(request):
    print(request)
    data = Preferences.objects.get(user=request.user)

    if request.POST:
        print(request.POST)
        data.galaxies = True if request.POST['galaxies'] == "True" else False
        data.stars = True if request.POST['stars'] == "True" else False
        data.planets = True if request.POST['planets'] == "True" else False
        data.blackHoles = True if request.POST['blackHoles'] == "True" else False
        data.moons = True if request.POST['moons'] == "True" else False
        data.save()

    return render(request, "preferences.html", {"user": request.user, "data": data})
