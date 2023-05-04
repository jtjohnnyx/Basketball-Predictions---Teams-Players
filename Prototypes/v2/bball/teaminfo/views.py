from django.shortcuts import render
from django.utils import timezone

import datetime
from .api import getdata

from datetime import datetime, timedelta
import requests

from teaminfo.forms import TeamForm
from teaminfo.forms import PlayerForm
from teaminfo import api
from teaminfo import apifuncs



import requests
import json
from datetime import datetime


def get_upcoming_games():
    url = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard'
    params = {'limit': 5}
    response = requests.get(url, params=params)
    data = response.json()

    games = []
    for event in data['events']:
        game_time = datetime.strptime(event['date'], '%Y-%m-%dT%H:%MZ')
        game_timestamp = int(game_time.timestamp())
        game_id = event['id']
        home_team = event['competitions'][0]['competitors'][0]['team']['displayName']
        home_score = event['competitions'][0]['competitors'][0]['score']
        away_team = event['competitions'][0]['competitors'][1]['team']['displayName']
        away_score = event['competitions'][0]['competitors'][1]['score']
        games.append({'id': game_id, 'time': game_timestamp, 'home_team': home_team, 'home_score': home_score, 'away_team': away_team, 'away_score': away_score})

    return games


def display(request):
    games = get_upcoming_games()
    return render(request, 'teaminfo/display.html', {'result': games})

def team_info(request): 

  result = ''
  if request.method == 'POST': 
      # create an instance of our form, and fill it with the POST data
      form = TeamForm(request.POST)

      if form.is_valid():
         team = form.cleaned_data['Team_name']
         dict = api.getdata("teams",None)
         result = apifuncs.find_team_info(dict,team)
  else:
  # this must be a GET request, so create an empty form
    form = TeamForm()

  return render(request,
         'teaminfo/teamnameform.html',
         {'form': form, 'result': result, 'id': 1})

def player_info(request):

  result = ''
  if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      form = PlayerForm(request.POST)

      if form.is_valid():
         player = form.cleaned_data['Player_name']
         dict = api.getdata("players",{"country":"usa"})
         result = apifuncs.find_player_info(dict,player)
  else:
  # this must be a GET request, so create an empty form
    form = PlayerForm()
  return render(request,
         'teaminfo/nameform.html',
         {'form': form, 'result': result, 'id': 2})


def live_scores(request):
    dict = api.getdata("games", None)
    result = apifuncs.get_live_scores(dict)
    return render(request, 'teaminfo/display.html', {'result': result})

def aboutpage(request):
    return render(request, 'teaminfo/about.html')

#New features coming

