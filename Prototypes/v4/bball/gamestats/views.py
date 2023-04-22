from django.shortcuts import render

from gamestats.forms import TeamForm
from gamestats.forms import PlayerForm
from gamestats import api
from gamestats import apifuncs
from gamestats import cache
from .models import Gamecache

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
        info = cache.get_teamcache(team)
        if info == None:
          print("add to cache")
          dict = api.getdata("teams",None)
          result = apifuncs.find_team_info(dict,team)
          cache.cache_team(team, result)
        else:
          print("get from cache")
          result = info
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


def games(request):  

  avail = cache.is_gamecache()
  print(avail)
  if avail == False:
    print("add to cache")
    info = api.getgames()
    result = apifuncs.find_games(info)
    cache.cache_games(result)
  else:
    print("get from cache")
  games = Gamecache.objects.all()
    #result = stats

  return render(request, 'games.html', {'games': games})#, {'output' : result})

def compare(request, id):
   games = Gamecache.objects.all()
   for game in games:
      if game.id2 == id:
        gg = game
   return render(request, 'comparison.html', {'id' : id, 'game': gg})


#New features coming