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
        data.survey_star = 'survey_star' in request.POST
        data.high_magnitude = 'high_magnitude' in request.POST
        data.high_variability = 'high_variability' in request.POST
        data.low_variability = 'low_variability' in request.POST
        data.multi_star_system = 'multi_star_system' in request.POST
        data.save()
        return render(request, "preferences.html", {"user": request.user, "data": data, "successmsg": "Success"})

    return render(request, "preferences.html", {"user": request.user, "data": data})


@login_required
def app(request):
    pref = Preferences.objects.get(user=request.user)
    data = []
    with connection.cursor() as cur:
        cur.callproc('get_survey_stars', []) if pref.survey_star else None
        data.append(cur.fetchall())
        cur.callproc('get_high_mag_stars', []) if pref.high_magnitude else None
        data.append(cur.fetchall())
        cur.callproc('get_high_var_stars', []
                     ) if pref.high_variability else None
        data.append(cur.fetchall())
        cur.callproc('get_low_var_stars', []) if pref.low_variability else None
        data.append(cur.fetchall())
        cur.callproc('get_multi_stars', []) if pref.multi_star_system else None
        data.append(cur.fetchall())
    print(data)

    return render(request, "app.html", {"user": request.user, "data": data})


@login_required
def locations(request):
    return render(request, "locations.html", {"user": request.user})
