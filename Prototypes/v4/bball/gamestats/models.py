from django.db import models

# Create your models here.

class Teamcache(models.Model):
    name = models.fields.CharField(max_length=100)
    nick = models.fields.CharField(max_length=100)
    code = models.fields.CharField(max_length=100)
    city = models.fields.CharField(max_length=100)
    teamid = models.fields.IntegerField()
    record = models.fields.CharField(max_length=1000)


class Gamecache(models.Model):
    time = models.fields.CharField(max_length=100)
    home = models.fields.CharField(max_length=100)
    away = models.fields.CharField(max_length=100)
    id2 = models.fields.IntegerField()


class LastUpdate(models.Model):
    hour = models.fields.CharField(max_length=10)
    day = models.fields.CharField(max_length=10)
    month = models.fields.CharField(max_length=10)
    year = models.fields.CharField(max_length=10)