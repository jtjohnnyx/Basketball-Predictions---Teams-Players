
from django.contrib import admin
from gamestats import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bball/', views.display),
    path('bball/team/', views.team_info),
    path('bball/player/', views.player_info),
    path('bball/about/', views.aboutpage),
    path('bball/odds/', views.odds),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
]
