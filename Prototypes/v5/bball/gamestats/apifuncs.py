'''def find_team_info(dict,key):
    found = 0
    i = 0
    while (found != 1 and i < 63):
        if dict['response'][i]['name'] == key:
            info = ['Nickname: ' + dict['response'][i]['nickname'],
                    'Team Code: ' + dict['response'][i]['code'],
                    'City: ' + dict['response'][i]['city'],]
            found = 1
        else:
            i += 1
    if found == 1:
        return info
    else:
        return [None]

def find_team_id(dict, name):
    found = 0
    i = 0
    while (found != 1 and i < len(dict['sports'][0]['leagues'][0]['teams'])):
        if dict['sports'][0]['leagues'][0]['teams'][i]['team']['displayName'] == name:
            teamid = dict['sports'][0]['leagues'][0]['teams'][i]['team']['id']
            found = 1
        else:
            i += 1
    if found == 1:
        return {"teamid": teamid}
    else:
        return None

def find_team_info(dict):
    ls = [dict['team']['name'],
          dict['team']['abbreviation'],
          dict['team']['location'],
          dict['team']['id'],
          dict['team']['record']['items'][0]['summary'],
          dict['team']['displayName']]
    return ls
    
def find_player_info(dict,key):
    found = 0
    i = 0
    while (found != 1 and i < 915):
        if dict['response'][i]['firstname'] + ' ' + dict['response'][i]['lastname'] == key:
            info = ['Country: ' + dict['response'][i]['birth']['country'],
                    'DoB: ' + dict['response'][i]['birth']['date'],
                    'First Appearance: ' + str(dict['response'][i]['nba']['start']),
                    'Height: ' + dict['response'][i]['height']['meters'],
                    'Affiliation: ' + dict['response'][i]['affiliation']]
            found = 1
        else: 
            i += 1
    if found == 1:
        return info
    else:
        return [None]'''
    

def find_upcgames(list):
    games = []
    for i in range(len(list)):
        if list[i]['completed'] == False:
            games += [[list[i]['home_team'], list[i]['away_team'], list[i]['commence_time']]]
            #games += [[list[i]['home_team'], list[i]['away_team'], list[i]['commence_time'], int(list[i]['scores'][0]['score']), int(list[i]['scores'][1]['score'])]]
    return games

def find_pastgames(list):
    games = []
    for i in range(len(list)):
        if list[i]['completed'] == True:
            games += [[list[i]['home_team'], list[i]['away_team'], list[i]['commence_time'], int(list[i]['scores'][0]['score']), int(list[i]['scores'][1]['score'])]]
    return games

def find_all_teams(dict):
    teams = []
    for team in dict['stats']:
        teams += [[team, dict['stats'][team]['Per Game']["AST"], dict['stats'][team]['Per Game']["ORB"], dict['stats'][team]['Per Game']["FT%"]]]

    return teams