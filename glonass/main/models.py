from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Preferences(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.RESTRICT, primary_key=True)
    galaxies = models.BooleanField(default=True)
    stars = models.BooleanField(default=True)
    planets = models.BooleanField(default=True)
    blackHoles = models.BooleanField(default=True)
    moons = models.BooleanField(default=True)

class UsersLocations(models.Model):
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.RESTRICT)
    label = models.CharField(max_length=255)
    primary = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

admin.site.register(Preferences)
admin.site.register(UsersLocations)