from django.urls import path
from mybooks.views import get_bookmark_json, remove_bookmark, show_mybooks, filter_category, show_json, show_xml

app_name = 'mybooks'

urlpatterns = [
    path('', show_mybooks, name='show_mybooks'),
    path('get_bookmark_json/', get_bookmark_json, name='get_bookmark_json'),
    path('remove_bookmark/', remove_bookmark, name='remove_bookmark'),
    path('filter/<int:id>/', filter_category, name='filter_category'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
]