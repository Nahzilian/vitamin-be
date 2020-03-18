from django.db import models

# Create your models here.
class Guest(models.Model):
    firstname = models.CharField(max_length = 300)
    lastname = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)
    age = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 100)
    fitnesslvl = models.CharField(max_length = 400)
    energylvl = models.CharField(max_length = 400)
    recentissue = models.CharField(max_length = 400)
    prescription = models.CharField(max_length = 400)
    country = models.CharField(max_length = 300)
    city = models.CharField(max_length = 300)
    state = models.CharField(max_length = 300)