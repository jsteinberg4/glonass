from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Preferences
from django.db import connection
from django.contrib.auth import logout


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
        if pref.survey_star:
            cur.callproc('get_survey_stars', [])
            for x in cur.fetchall():
                data.append(x) if x not in data else None

        if pref.high_magnitude:
            cur.callproc('get_high_mag_stars', [])
            for x in cur.fetchall():
                data.append(x) if x not in data else None

        if pref.high_variability:
            cur.callproc('get_high_var_stars', [])
            for x in cur.fetchall():
                data.append(x) if x not in data else None

        if pref.low_variability:
            cur.callproc('get_low_var_stars', [])
            for x in cur.fetchall():
                data.append(x) if x not in data else None

        if pref.multi_star_system:
            cur.callproc('get_multi_stars', [])
            for x in cur.fetchall():
                data.append(x) if x not in data else None

        print(data)

    return render(request, "app.html", {"user": request.user, "data": data})

@login_required
def delete(request):
    u = User.objects.get(user=request.POST.user)
    logout(u)
    u.delete()

    return redirect('/')

@login_required
def locations(request):
    return render(request, "locations.html", {"user": request.user})
