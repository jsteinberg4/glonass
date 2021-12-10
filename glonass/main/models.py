from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.


class Preferences(models.Model):
    user = models.OneToOneField(User, verbose_name=(
        "user"), on_delete=models.RESTRICT, primary_key=True)
    survey_star = models.BooleanField(default=True)
    high_magnitude = models.BooleanField(default=True)
    high_variability = models.BooleanField(default=True)
    low_variability = models.BooleanField(default=True)
    multi_star_system = models.BooleanField(default=True)


class UsersLocations(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "user"), on_delete=models.RESTRICT)
    label = models.CharField(max_length=255)
    primary = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)


admin.site.register(Preferences)
admin.site.register(UsersLocations)
