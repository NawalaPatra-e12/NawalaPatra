from django.urls import path
from .views import *

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('rate_button/<int:book_id>',rate_button,name='rate_button')
]