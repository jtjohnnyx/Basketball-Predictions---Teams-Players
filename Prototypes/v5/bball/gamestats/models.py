from django.db import models

# Create your models here.

class Teamcache(models.Model):
    name = models.fields.CharField(max_length=100)
    teamid = models.fields.IntegerField()
    season = models.fields.CharField(max_length=10)
    ast = models.fields.CharField(max_length=10)
    orb = models.fields.CharField(max_length=10)
    ftd = models.fields.CharField(max_length=10)

class upcGames(models.Model):
    time = models.fields.CharField(max_length=100)
    home = models.fields.CharField(max_length=100)
    away = models.fields.CharField(max_length=100)
    gameid = models.fields.IntegerField()


class pastGames(models.Model):
    time = models.fields.CharField(max_length=100)
    home = models.fields.CharField(max_length=100)
    away = models.fields.CharField(max_length=100)
    gameid = models.fields.IntegerField()
    homescore = models.fields.IntegerField()
    awayscore = models.fields.IntegerField()


class LastUpdate(models.Model):
    hour = models.fields.CharField(max_length=10)
    day = models.fields.CharField(max_length=10)
    month = models.fields.CharField(max_length=10)
    year = models.fields.CharField(max_length=10)
    type = models.fields.CharField(max_length=10)