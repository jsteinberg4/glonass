from django.shortcuts import render
from main.models import Preferences

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import connection

def signin(request):
    print(request.POST)
    if request.POST:
        user = authenticate(
            username=request.POST['uname'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "signin.html", {"errormsg": "Incorrect username or password"})
    return render(request, "signin.html")


def createAccount(request):
    if request.POST:
        username = request.POST['uname']
        password = request.POST['password']
        if password != request.POST['confirm']:
            return render(request, "create.html", {"errormsg": "Passwords don't match"})
        # check if username is duplicate
        with connection.cursor() as cur:
            cur.execute("SELECT username_exists(%s);", [username])
            if cur.fetchone()[0]: # if username exists
                return render(request, "create.html", {"errormsg": "Username already exists, try signing in"})

        User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:  # prob not needed
            login(request, user)
            p = Preferences(user=user)
            p.save()
            return redirect('/')
    return render(request, "create.html")
