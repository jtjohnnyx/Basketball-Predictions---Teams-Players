def find_team_info(dict,key):
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
        return [None]