
from django.contrib import admin
from gamestats import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bball/', views.display),
    path('bball/team/', views.team_info),
    path('bball/team/<str:teamid>/<int:pageid>/', views.team, name = 'team'),
    path('bball/roster/<str:teamid>/<int:pageid>/', views.roster, name = 'roster'),
    path('bball/player/', views.player_info),
    path('bball/player/<str:teamid>/<str:playerid>/<int:pageid>/', views.player, name = 'player'),
    path('bball/about/', views.aboutpage),
    path('bball/standing/', views.standings),
    path('bball/upcoming-games/', views.upcgames),
    path('bball/past-games/', views.pastgames),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    #path('/accounts/google/login/', ) 
    path('logout/', LogoutView.as_view()),
    #path('bball/compare/', views.compare),
    path('bball/compare/<int:id>/', views.compare, name = 'comparison'),
]
