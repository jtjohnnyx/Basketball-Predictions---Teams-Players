import requests

def getdata(b,q):
    url = "https://basketball-data.p.rapidapi.com/team/schedule"

    querystring = {"teamId":"1442"}

    headers = {
        "X-RapidAPI-Key": "f8f4dc7431mshc9098903b1f983ep135e3ajsnb77bd5f6bc42",
        "X-RapidAPI-Host": "basketball-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)