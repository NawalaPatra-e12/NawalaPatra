from django.urls import path
from .views import *

app_name = 'leaderboard'

urlpatterns = [
    path('',show_leaderboard,name='show_leaderboard'),
    path('filter/<int:id>/', filter_leaderboard, name='filter_leaderboard'),
    path('rate_button',rate_button,name='rate_button')
]