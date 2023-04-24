#import datetime

from .models import Teamcache, upcGames, pastGames
import ast
from gamestats import datefuncs, api, apifuncs

#print(datetime.datetime.now().time())

#def get_cache():
 #   return

#def add_cache_team(info):
#    Team.objects.create(name = stud_name[i], nick = stud_age[i], code = stud_marks[i], city = )

def get_teamcache(name, year):
    #Teamcache.objects.all().delete()
    team = Teamcache.objects.filter(season = year).filter(name = team).first()
    #team = Teamcache.objects.filter(name = name).first()
    return team

def get_teamlist():
    ls = []
    teams = Teamcache.objects.values("name").distinct()
    #teams = Teamcache.objects.filter(season = "2022").all()
    for team in teams:
        ls += [(team['name'], team['name'])]
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
    Teamcache.objects.create(name = result[5], nick = result[0], code = result[1], city = result[2],
                             teamid = result[3], record = result[4])
    return'''

def cache_teams(year):
    i = 0
    dict = api.getteamstats({"leagueYear": year})
    result = apifuncs.find_all_teams(dict)
    for res in result:
        Teamcache.objects.create(name = res[0], teamid = i, ast = res[1], orb = res[2], ftd = res[3], season = year)
        i += 1
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

