from django import forms
from gamestats import cache

teams = cache.get_teamlist()
years = [(str(y),str(y)) for y in range(2022, 2020, -1)]
years = [("2023","2023(current)")] + years
confs = [("Western Conference","Western Conference"), ("Eastern Conference","Eastern Conference")]
players = cache.get_playerlist()

class TeamForm(forms.Form):
   Team_Name = forms.CharField(required=True, widget=forms.Select(choices=teams))
   Season = forms.CharField(required=True, widget=forms.Select(choices=years))
   # email = forms.EmailField()
   #message = forms.CharField(max_length=1000)
   #integer = forms.IntegerField(max_value=10000, min_value=-10000)

class PlayerForm(forms.Form):
   Player_Name = forms.CharField(required=True,widget=forms.Select(choices=players))

class StandingForm(forms.Form):
   Conference = forms.CharField(required=True, widget=forms.Select(choices=confs))
   Season = forms.CharField(required=True, widget=forms.Select(choices=years))