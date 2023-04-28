#import datetime

from .models import Teams, upcGames, pastGames, Players
import ast
from gamestats import datefuncs, api, apifuncs

#print(datetime.datetime.now().time())

#def get_cache():
 #   return

#def add_cache_team(info):
#    Team.objects.create(name = stud_name[i], nick = stud_age[i], code = stud_marks[i], city = )

def get_teams(name, year):
    #Teams.objects.all().delete()
    team = Teams.objects.filter(season = year).filter(name = name).first()
    #team = Teams.objects.filter(name = name).first()
    return team

def get_teamlist():
    ls = []
    ls3 = []
    teams = Teams.objects.values("name").distinct()
    #teams = Teams.objects.filter(season = "2022").all()
    for team in teams:
        ls += [team['name']]
        ls2 = sorted(ls)
        ls3 = [(l,l) for l in ls2]
    return ls3

def get_players(teamid):
    ls = []
    players = Players.objects.filter(teamid = teamid).all()
    for player in players:
        ls += [player]
    return ls

    
'''def get_upcGames():
    upcGames.objects.all().delete()
    if upcGames.objects.exists() == False:
        return None
    else:
        games = upcGames.objects.all()
        #print(type(infos.info))
        ls = []
        for game in games:
            ls += [[game.time, game.home, game.away]]
        return ls'''

def upcgames_avail():
    #upcGames.objects.all().delete()
    
    if upcGames.objects.exists() == True:
        print("Need update?:", datefuncs.needupdate("upcoming"))
        if datefuncs.needupdate("upcoming") == True:
            datefuncs.update("upcoming")
            upcGames.objects.all().delete()

    return upcGames.objects.exists()

def pastgames_avail():
    #upcGames.objects.all().delete()
    
    if pastGames.objects.exists() == True:
        print("Need update?:", datefuncs.needupdate("past"))
        if datefuncs.needupdate("past") == True:
            datefuncs.update("past")
            pastGames.objects.all().delete()

    return pastGames.objects.exists()
    
'''def cache_team(result):
    Teams.objects.create(name = result[5], nick = result[0], code = result[1], city = result[2],
                             teamid = result[3], record = result[4])
    return'''

def cache_pastteams(year):
    i = 0
    dict = api.getteamstats({"leagueYear": year})
    print(dict)
    result = apifuncs.find_past_teams(dict)
    for res in result:
        #Teams.objects.create(name = res[0], ast = res[1], orb = res[2], ftd = res[3], wins = res[4], losses = res[5], pts = res[6], season = year)
        ref = Teams.objects.filter(season = "2023").filter(name = res[0]).first()
        Teams.objects.create(name = res[0], wins = res[4], losses = res[5], pts = res[6], season = year, teamid = ref.teamid, conf = ref.conf, opts = res[7])
        i += 1
    return


def cache_currteams():
    dict = api.getcurrteams()
    print(dict)
    result = apifuncs.find_curr_teams(dict)
    for res in result:
        Teams.objects.create(name = res[0], pts = res[1], teamid = res[2], wins = res[3], losses = res[4], conf = res[5], opts = res[6], season = "2023")
    return

def cache_upcgames():
    i = 0
    info = api.getgames()
    result = apifuncs.find_upcgames(info)
    for res in result:
        upcGames.objects.create(home = res[0], away = res[1], time = res[2], gameid = i)
            #pastGames.objects.create(home = res[0], away = res[1], time = res[2], homescore = res[3], awayscore = res[4], gameid = i)
        i += 1
    return

def cache_pastgames():
    i = 0
    info = api.getgames()
    result = apifuncs.find_pastgames(info)
    for res in result:
        pastGames.objects.create(home = res[0], away = res[1], time = res[2], homescore = res[3], awayscore = res[4], gameid = i)
        i += 1
    return


def cache_players():
    info = api.getcurrteams()
    for i in range(30):
        result = apifuncs.find_all_players(info, i)
        for res in result:
            Players.objects.create(name = res[0], teamid = res[1], pic = res[2], playerid = res[3], age = str(datefuncs.calculate_age(res[4])), height = res[5])
    return