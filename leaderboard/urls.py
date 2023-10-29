from django.urls import path
from .views import *

app_name = 'leaderboard'

urlpatterns = [
    path('',show_leaderboard,name='show_leaderboard'),
    path('filter/<int:id>/', filter_leaderboard, name='filter_leaderboard'),
    path('rate_button',rate_button,name='rate_button'),
    path('get_book_json',get_book_json,name='get_book_json'),
    path('add_comment', add_comment, name = 'add_comment'),
    path('get_comment_json', get_comment_json, name='get_comment_json'),
    path('comments/',show_comment, name="show_comment"),
    ]