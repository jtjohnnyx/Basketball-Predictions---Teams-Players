from django.shortcuts import render

from gamestats.forms import TeamForm
from gamestats.forms import PlayerForm
from gamestats import api
from gamestats import apifuncs
from gamestats import cache
from .models import Teamcache, upcGames, pastGames

def display(request):
  return render(request, 'display.html')

def team_info(request): 

  info = None
  year = None
  found = True
  if request.method == 'POST': 
      # create an instance of our form, and fill it with the POST data
      form = TeamForm(request.POST)
      #upcGames.objects.all().delete()

      if form.is_valid():
        #print(form.cleaned_data)
        team = form.cleaned_data['Team_Name']
        year = form.cleaned_data['Season']
        info = Teamcache.objects.filter(season = year).filter(name = team).first()
        if info == None:
          found = False
        '''
        if info == None:
          print("add to cache")
          res = cache.cache_team(team)
          if res == False:
            print("No team found")
            found = 0
          else:
            info = cache.get_teamcache(team)
        else:
          print("got from cache")'''
        
  else:
  # this must be a GET request, so create an empty form
    form = TeamForm()
    #Teamcache.objects.all().delete()
    #for i in range(2005,2023):
    #  cache.cache_teams(str(i))
   
  return render(request,
         'teamform.html',
         {'form': form, 'team': info, 'year': year, 'found': found, 'pageid': 1})


def player_info(request):

  '''NOT FINISHED!!!!
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
         {'form': form, 'result': result, 'id': 2})'''
  return render(request, 'about.html')


def aboutpage(request):
    return render(request, 'about.html')


def pastgames(request):  
  avail = cache.pastgames_avail()
  print("Cache:", avail)
  if avail == False:
    print("add to cache")
    cache.cache_pastgames()
  else:
    print("got from cache")
  games = pastGames.objects.all()
  return render(request, 'pastgames.html', {'games': games, 'pageid': 3})


def upcgames(request):  
  avail = cache.upcgames_avail()
  print("Cache:", avail)
  if avail == False:
    print("add to cache")
    cache.cache_upcgames()
  else:
    print("got from cache")
  games = upcGames.objects.all()

  return render(request, 'upcgames.html', {'games': games, 'pageid': 4 })


def compare(request, id):
  '''NOT FINISHED'''
  game = upcGames.objects.filter(gameid = id).first()
  team1 = Teamcache.objects.filter(season = "2022").filter(name = game.home).first()
  team2 = Teamcache.objects.filter(season = "2022").filter(name = game.away).first()

  return render(request, 'comparison.html', {'id' : id, 'team1': team1, 'team2': team2})
