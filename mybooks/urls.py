from django.urls import path
from mybooks.views import show_mybooks

app_name = 'mybooks'

urlpatterns = [
    path('', show_mybooks, name='show_mybooks')
]