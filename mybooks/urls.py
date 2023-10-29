from django.urls import path
from mybooks.views import show_mybooks, get_bookmark_json

app_name = 'mybooks'

urlpatterns = [
    path('', show_mybooks, name='show_mybooks'),
    path('get_bookmark_json/', get_bookmark_json, name='get_bookmark_json'),
]