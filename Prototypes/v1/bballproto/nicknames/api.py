import requests

def getdata():
    url = "https://api-nba-v1.p.rapidapi.com/teams"

    headers = {
	"X-RapidAPI-Key": "1140719bf0mshb79f4957c134d32p181b91jsna45ef7333ea5",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    bdata = response.json()
    return bdata