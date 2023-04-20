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



def get_upcoming_games():
    url = "https://api-nba-v1.p.rapidapi.com/games/date/"

    headers = {
	"X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    # Get the date of the upcoming Monday
    today = datetime.today()
    monday = today + timedelta(days=-today.weekday(), weeks=1)

    # Get the dates for the upcoming week
    dates = []
    for i in range(7):
        date = monday + timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))

    games = []
    for date in dates:
        params = {"date": date}
        response = requests.request("GET", url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            games += data["api"]["games"]

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

