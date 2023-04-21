from django.db import models

# Create your models here.

class Teamcache(models.Model):
    name = models.fields.CharField(max_length=100)
    nick = models.fields.CharField(max_length=100)
    code = models.fields.CharField(max_length=100)
    city = models.fields.CharField(max_length=100)

class Gamecache(models.Model):
    info = models.fields.CharField(max_length=2500)

class Comcache(models.Model):
    name1 = models.fields.CharField(max_length=100)
    name2 = models.fields.CharField(max_length=100)
    stats1 = models.fields.CharField(max_length=1000)
    stats2 = models.fields.CharField(max_length=1000)