def findnick(dict,key):
    found = 0
    i = 0
    while (found != 1 and i <= 62):
        if dict['response'][i]['name'] == key:
            fkey = dict['response'][i]['nickname']
            found = 1
        else:
            i += 1
    if found == 1:
        return fkey
    else:
        return "None"