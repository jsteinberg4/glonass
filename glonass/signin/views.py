from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
        User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:  # prob not needed
            login(request, user)
            return redirect('/')
    return render(request, "create.html")
