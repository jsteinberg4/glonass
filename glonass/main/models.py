from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Preferences(models.Model):
    user = models.OneToOneField(
        User, verbose_name=("user"), on_delete=models.CASCADE, primary_key=True)
    galaxies = models.BooleanField(default=True)
    stars = models.BooleanField(default=True)
    planets = models.BooleanField(default=True)
    blackHoles = models.BooleanField(default=True)
    moons = models.BooleanField(default=True)
