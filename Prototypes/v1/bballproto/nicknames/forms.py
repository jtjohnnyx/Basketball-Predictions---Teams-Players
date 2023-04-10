# listings/forms.py

from django import forms

class TeamForm(forms.Form):
   Team_name = forms.CharField(required=True)
   #email = forms.EmailField()
   #message = forms.CharField(max_length=1000)