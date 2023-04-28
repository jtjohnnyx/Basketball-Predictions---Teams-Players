from django.shortcuts import render

from gamestats.forms import TeamForm, PlayerForm
from gamestats import cache
from .models import Teams, upcGames, pastGames, Players

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
        info = Teams.objects.filter(season = year).filter(name = team).first()
        if info == None:
          found = False

  else:
  # this must be a GET request, so create an empty form
    form = TeamForm()
    #Teams.objects.all().delete()
    #for i in range(2022, 2020, -1):
    #  cache.cache_pastteams(str(i))
    #cache.cache_currteams()
   
  return render(request,
         'teamform.html',
         {'form': form, 'team': info, 'year': year,'found': found, 'pageid': 1})


def player_info(request):

  info = None
  team = None
  found = True
  if request.method == 'POST': 
      # create an instance of our form, and fill it with the POST data
      form = PlayerForm(request.POST)
      #upcGames.objects.all().delete()

      if form.is_valid():
        #print(form.cleaned_data)
        player = form.cleaned_data['Player_Name']
        info = Players.objects.filter(name = player).first()
        if info == None:
          print("no player")
          found = False
        else:
          print("yes player")
          teamid = info.teamid
          team = Teams.objects.filter(teamid = teamid).first()
        
  else:
  # this must be a GET request, so create an empty form
    form = PlayerForm()

    #Teams.objects.all().delete()
    #Players.objects.all().delete()
    #for i in range(2022, 2020, -1):
    #  cache.cache_pastteams(str(i))
    #cache.cache_currteams()
    #cache.cache_players()
  
  
  return render(request,
         'playerform.html',
         {'form': form, 'player': info, 'team': team, 'found': found, 'pageid': 2})


def player(request, teamid, playerid):
  player = Players.objects.filter(playerid = playerid).first()
  team = Teams.objects.filter(teamid = teamid).first() 
  return render(request,
         'player.html',
         {'team': team, 'player': player})

def aboutpage(request):
    return render(request, 'about.html')

def roster(request, id):
  team = Teams.objects.filter(teamid = id).first()
  players = cache.get_players(teamid = id)
  return render(request,
         'roster.html',
         {'players': players, 'team': team})

def pastgames(request):
  '''  
  avail = cache.pastgames_avail()
  print("Cache:", avail)
  if avail == False:
    print("add to cache")
    cache.cache_pastgames()
  else:
    print("got from cache")'''
  games = pastGames.objects.all()
  return render(request, 'pastgames.html', {'games': games, 'pageid': 3})


def upcgames(request):
  '''  
  avail = cache.upcgames_avail()
  print("Cache:", avail)
  if avail == False:
    print("add to cache")
    cache.cache_upcgames()
  else:
    print("got from cache")'''
  games = upcGames.objects.all()

  return render(request, 'upcgames.html', {'games': games, 'pageid': 4 })


def compare(request, id):
  '''NOT FINISHED'''
  game = upcGames.objects.filter(gameid = id).first()
  team1 = Teams.objects.filter(season = "2023").filter(name = game.home).first()
  team2 = Teams.objects.filter(season = "2023").filter(name = game.away).first()
  pteam1 = Teams.objects.filter(season = "2022").filter(name = game.home).first()
  pteam2 = Teams.objects.filter(season = "2022").filter(name = game.away).first()
 
  return render(request, 'comparison.html', {'id' : id, 'team1': team1, 'team2': team2, 'pteam1': pteam1, 'pteam2': pteam2})
