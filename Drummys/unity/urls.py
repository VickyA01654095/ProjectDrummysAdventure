from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # --- AUTH  ---
    path('login', views.login, name='game/login'),
    # --- API ---
    path('party', views.game_party, name='game/party'),
    path('level', views.level, name='level')
]