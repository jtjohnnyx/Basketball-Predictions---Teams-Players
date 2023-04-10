from django.shortcuts import render

from teaminfo.forms import TeamForm
from teaminfo.forms import PlayerForm
from teaminfo import api
from teaminfo import apifuncs

def display(request):
  return render(request,
         'teaminfo/display.html',
          )

def team_info(request):

  result = ''
  if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      form = TeamForm(request.POST)

      if form.is_valid():
         team = form.cleaned_data['Team_name']
         dict = api.getdata("teams",None)
         result = apifuncs.find_team_info(dict,team)
  else:
  # this must be a GET request, so create an empty form
    form = TeamForm()

  return render(request,
         'teaminfo/nameform.html',
         {'form': form, 'result': result, 'id': 1})

def player_info(request):

  result = ''
  if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      form = PlayerForm(request.POST)

      if form.is_valid():
         player = form.cleaned_data['Player_name']
         dict = api.getdata("players",{"country":"usa"})
         result = apifuncs.find_player_info(dict,player)
  else:
  # this must be a GET request, so create an empty form
    form = PlayerForm()
  return render(request,
         'teaminfo/nameform.html',
         {'form': form, 'result': result, 'id': 2})
