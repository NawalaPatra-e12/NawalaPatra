from django.urls import path
from .views import *

app_name = 'leaderboard'

urlpatterns = [
    path('filter/<int:id>/', filter_leaderboard, name='filter_leaderboard'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]