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
    
def get_gamecache():
    if Gamecache.objects.exists() == False:
        return None
    else:
        ls = []
        infos = Gamecache.objects.all()
        for i in infos:
            ls += [i.info]
        return 

def cache_team(name,result):
    Teamcache.objects.create(name = name, nick = result[0], code = result[1], city = result[2])
    return

def cache_livegames(ls):
    Gamecache.objects.create(info = ls)
    return

def cache_compare(name1, name2, stats1, stats2):
    Comcache.objects.create(name1 = name1, name2 = name2, stats1 = stats1, stats2 = stats2)
    return
