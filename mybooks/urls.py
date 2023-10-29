from django.urls import path
from mybooks.views import get_bookmark_json, remove_bookmark, show_mybooks, filter_category, show_json, show_xml, add_review_ajax, show_json_by_id, show_xml_by_id

app_name = 'mybooks'

urlpatterns = [
    path('', show_mybooks, name='show_mybooks'),
    path('get_bookmark_json/', get_bookmark_json, name='get_bookmark_json'),
    path('remove_bookmark/', remove_bookmark, name='remove_bookmark'),
    path('filterbookmark/<int:id>/', filter_category, name='filter_category'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('add_review_ajax/<int:id>/', add_review_ajax, name="add_review_ajax")
]