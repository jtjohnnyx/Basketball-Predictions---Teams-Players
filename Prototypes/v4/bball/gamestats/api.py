import requests

def getdata(b,q):
    url = "https://api-nba-v1.p.rapidapi.com/" + b

    headers = {
	"X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=q)

    bdata = response.json()
    return bdata


def getgames():

    url = "https://odds.p.rapidapi.com/v4/sports/basketball/odds"

    querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h,spreads","dateFormat":"iso"}

    headers = {
	"X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    
    return data


def getteams():

    url = "https://api-basketball-nba.p.rapidapi.com/nbateamlist"

    headers = {
        "X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
        "X-RapidAPI-Host": "api-basketball-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()
    return data


def getteaminfo(teamid):

    url = "https://api-basketball-nba.p.rapidapi.com/nbateaminfo"

    querystring = teamid

    headers = {
        "X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
        "X-RapidAPI-Host": "api-basketball-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    return data