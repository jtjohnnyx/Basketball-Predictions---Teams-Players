#import datetime

from .models import Teamcache, Gamecache, Comcache
import ast

#print(datetime.datetime.now().time())

#def get_cache():
 #   return

#def add_cache_team(info):
#    Team.objects.create(name = stud_name[i], nick = stud_age[i], code = stud_marks[i], city = )

def get_teamcache(name):
    team = Teamcache.objects.filter(name = name).first()
    if team:
        return [team.nick, team.code, team.city]
    else:
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
    return Gamecache.objects.exists()
    
def cache_team(name,result):
    Teamcache.objects.create(name = name, nick = result[0], code = result[1], city = result[2])
    return

def cache_games(result):
    i = 0
    for res in result:
        Gamecache.objects.create(time = res[0], home = res[1], away = res[2], id2 = i)
        i += 1
    return

def cache_compare(name1, name2, stats1, stats2):
    Comcache.objects.create(name1 = name1, name2 = name2, stats1 = stats1, stats2 = stats2)
    return
