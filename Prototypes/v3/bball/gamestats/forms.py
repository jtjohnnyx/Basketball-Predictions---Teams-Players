from django import forms

class TeamForm(forms.Form):
   Team_name = forms.CharField(required=True)
   # email = forms.EmailField()
   #message = forms.CharField(max_length=1000)
   #integer = forms.IntegerField(max_value=10000, min_value=-10000)

class PlayerForm(forms.Form):
   Player_name = forms.CharField(required=True)