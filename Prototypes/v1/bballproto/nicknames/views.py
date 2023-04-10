from django.shortcuts import render

from nicknames.forms import TeamForm
from nicknames import api
from nicknames import searchapi

def find_nick(request):

  result = ' '
  if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      form = TeamForm(request.POST)

      if form.is_valid():
         team = form.cleaned_data['Team_name']
         dict = api.getdata()
         #print(searchapi.findnick(dict,team))
         result = searchapi.findnick(dict,team)
  else:
  # this must be a GET request, so create an empty form
    form = TeamForm()

  return render(request,
         'nicknames/displayform.html',
         {'form': form, 'result': result})
