from django.shortcuts import render

from gamestats.forms import TeamForm
from gamestats.forms import PlayerForm
from gamestats import api
from gamestats import apifuncs


def display(request):
  return render(request,
         'display.html',
          )

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
         'nameform.html',
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
         'nameform.html',
         {'form': form, 'result': result, 'id': 2})


def aboutpage(request):
    return render(request, 'about.html')


def odds(request):  

  stats = api.getodds()
  print(stats)
  result = apifuncs.find_odds_info(stats)
  return render(request, 'odds.html', {'output' : result})

#New features coming