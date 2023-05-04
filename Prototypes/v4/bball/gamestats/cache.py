#import datetime

from .models import Teamcache, Gamecache
import ast
from gamestats import datefuncs, api, apifuncs

#print(datetime.datetime.now().time())

#def get_cache():
 #   return

#def add_cache_team(info):
#    Team.objects.create(name = stud_name[i], nick = stud_age[i], code = stud_marks[i], city = )

def get_teamcache(name):
    #Teamcache.objects.all().delete()
    team = Teamcache.objects.filter(name = name).first()
    return team
    
'''def get_gamecache():
    Gamecache.objects.all().delete()
    if Gamecache.objects.exists() == False:
        return None
    else:
        games = Gamecache.objects.all()
        #print(type(infos.info))
        ls = []
        for game in games:
            ls += [[game.time, game.home, game.away]]
        return ls'''

def is_gamecache():
    #Gamecache.objects.all().delete()
    '''
    date = LastUpdate.objects.first()
    a_date, upd = datefuncs.is_next_day(date)
    if upd == True:
        LastUpdate.objects.all().delete()
        LastUpdate.objects.create(hour = a_date[0], day = a_date[1], month = a_date[2], year = a_date[3])'''
    if datefuncs.needupdate() == True:
        datefuncs.update()
        Gamecache.objects.all().delete()
    #LastUpdate.objects.all().delete()
    #LastUpdate.objects.create(hour = "16", day = "21", month = "04", year = "2023")
    print("Need update?:", datefuncs.needupdate())
    return Gamecache.objects.exists()
    
'''def cache_team(result):
    Teamcache.objects.create(name = result[5], nick = result[0], code = result[1], city = result[2],
                             teamid = result[3], record = result[4])
    return'''

def cache_team(name):
    res = False
    dict = api.getteams()
    teamid = apifuncs.find_team_id(dict, name)
    if teamid != None:
        dict2 = api.getteaminfo(teamid)
        result = apifuncs.find_team_info(dict2)
        Teamcache.objects.create(name = result[5], nick = result[0], code = result[1], city = result[2],
                             teamid = result[3], record = result[4])
        res = True
    return res

def cache_games(result):
    i = 0
    for res in result:
        Gamecache.objects.create(time = res[0], home = res[1], away = res[2], id2 = i)
        i += 1
    return

