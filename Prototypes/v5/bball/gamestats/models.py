from django.db import models

# Create your models here.

class Teams(models.Model):
    name = models.fields.CharField(max_length=100)
    teamid = models.fields.CharField(max_length=10, default = "0")
    season = models.fields.CharField(max_length=10)
    wins = models.fields.CharField(max_length=10)
    losses = models.fields.CharField(max_length=10)
    pts = models.fields.CharField(max_length=10)
    opts = models.fields.CharField(max_length=10, default = "0")
    conf = models.fields.CharField(max_length=100, default = "0")
    logo = models.fields.CharField(max_length=100, default = "None")
    code = models.fields.CharField(max_length=10, default = "None")


class Players(models.Model):
    name = models.fields.CharField(max_length=100)
    teamid = models.fields.CharField(max_length=10)
    pic = models.fields.CharField(max_length=100)
    age = models.fields.CharField(max_length=10)
    height = models.fields.CharField(max_length=10)
    playerid = models.fields.CharField(max_length=100)
    extra = models.fields.CharField(max_length=1000, default = "None")


class upcGames(models.Model):
    time = models.fields.CharField(max_length=100)
    home = models.fields.CharField(max_length=100)
    away = models.fields.CharField(max_length=100)
    gameid = models.fields.IntegerField()
    odds = models.fields.CharField(max_length=100, default = "None") 


class pastGames(models.Model):
    time = models.fields.CharField(max_length=100)
    home = models.fields.CharField(max_length=100)
    away = models.fields.CharField(max_length=100)
    gameid = models.fields.IntegerField()
    homescore = models.fields.IntegerField()
    awayscore = models.fields.IntegerField()


class lastGames(models.Model):
    name = models.fields.CharField(max_length=100)
    teamid = models.fields.CharField(max_length=10)
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