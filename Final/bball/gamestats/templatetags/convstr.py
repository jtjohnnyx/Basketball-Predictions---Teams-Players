from django import template
register = template.Library()

def conv(str):
    return eval(str)

register.filter("conv", conv)

def pct(team):
    return round((int(team.wins) /  (int(team.wins) + int(team.losses))), 3) 

register.filter("pct", pct)