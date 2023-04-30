from django.shortcuts import render

from gamestats.forms import TeamForm, PlayerForm, StandingForm
from gamestats import cache
from .models import Teams, upcGames, pastGames, Players, lastGames, LastUpdate

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
    #Teams.objects.filter(season = "2022").all().delete()
    #Teams.objects.filter(season = "2021").all().delete()
    #cache.cache_currteams()
    #for i in range(2022, 2020, -1):
    # cache.cache_pastteams(str(i))

  return render(request,
         'teamform.html',
         {'form': form, 'team': info, 'year': year,'found': found, 'pageid': 1})


def team(request, teamid, pageid):
  team = Teams.objects.filter(season = "2023").filter(teamid = teamid).first()
  return render(request,
         'team.html',
         {'team': team, 'pageid': pageid})


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

    #lastGames.objects.all().delete()
    #for i in range(5):
    #  teams = Teams.objects.filter(season = "2023").all()
    #  for tm in teams:
    #    lastGames.objects.create(name = tm.name, teamid = tm.teamid, home = "Home", away = "Away", time = "Time", homescore = -2, awayscore = -3, gameid = -1)

    #Teams.objects.all().delete()
    #Players.objects.all().delete()
    #for i in range(2022, 2020, -1):
    #  cache.cache_pastteams(str(i))
    #cache.cache_currteams()
    #cache.cache_players()
  
  
  return render(request,
         'playerform.html',
         {'form': form, 'player': info, 'team': team, 'found': found, 'pageid': 2})


def player(request, teamid, playerid, pageid):
  player = Players.objects.filter(playerid = playerid).first()
  team = Teams.objects.filter(teamid = teamid).first() 
  return render(request,
         'player.html',
         {'team': team, 'player': player, 'pageid': pageid})

def aboutpage(request):
    return render(request, 'about.html')

def roster(request, teamid, pageid):
  team = Teams.objects.filter(teamid = teamid).first()
  players = cache.get_players(teamid = teamid)

  return render(request,
         'roster.html',
         {'players': players, 'team': team, 'pageid': pageid})


def pastgames(request):

  avail = cache.pastgames_avail()
  print("Cache:", avail)
  if avail == False:
    print("add to cache")
    cache.cache_pastgames()
  else:
    print("got from cache")
  games = pastGames.objects.order_by("-gameid")

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
  odds = game.odds.split(' ')
  odds1 = odds[0]
  odds2 = odds[1]
  lg1 = list(lastGames.objects.filter(name = game.home).all())
  lg2 = list(lastGames.objects.filter(name = game.away).all())
  l1 = []
  l2 = []

  for g1 in lg1:
    if g1.name == g1.home:
      if g1.homescore > g1.awayscore:
        l1 += [1]
      elif g1.homescore == g1.awayscore:
        l1 += [0]
      else:
        l1 += [-1]
    else:
      if g1.homescore > g1.awayscore:
        l1 += [-1]
      elif g1.homescore == g1.awayscore:
        l1 += [0]
      else:
        l1 += [1]

  for g2 in lg2:
    if g2.name == g2.home:
      if g2.homescore > g2.awayscore:
        l2 += [1]
      elif g2.homescore == g2.awayscore:
        l2 += [0]
      else:
        l2 += [-1]
    else:
      if g2.homescore > g2.awayscore:
        l2 += [-1]
      elif g2.homescore == g2.awayscore:
        l2 += [0]
      else:
        l2 += [1]

  results = zip(lg1, lg2, l1, l2)
  team1 = Teams.objects.filter(season = "2023").filter(name = game.home).first()
  team2 = Teams.objects.filter(season = "2023").filter(name = game.away).first()
  pteam1 = Teams.objects.filter(season = "2022").filter(name = game.home).first()
  pteam2 = Teams.objects.filter(season = "2022").filter(name = game.away).first()
 
  return render(request, 'comparison.html', {'odds1' : odds1, 'odds2': odds2, 'team1': team1, 'team2': team2, 'pteam1': pteam1, 'pteam2': pteam2, 'results': results})


def standings(request):

  conf = None
  year = None
  found = True
  teams = None

  if request.method == 'POST': 
      # create an instance of our form, and fill it with the POST data
      form = StandingForm(request.POST)
      #upcGames.objects.all().delete()

      if form.is_valid():
        #print(form.cleaned_data)
        conf = form.cleaned_data['Conference']
        year = form.cleaned_data['Season']

        teams = Teams.objects.filter(season = year).filter(conf = conf).order_by('-wins','-losses', '-pts').all()

        if teams == None:
          found = False

  else:
  # this must be a GET request, so create an empty form
    form = StandingForm()
  
  
  return render(request, 'standingform.html', {'form': form, 'teams': teams, 'conf': conf, 'season': year, 'found': found, 'pageid': 6})
