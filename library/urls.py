from django.urls import path
from library.views import show_library, bookmark_book
from library.views import search_products, filter_category
from library.views import show_json, show_json_by_id, show_xml, show_xml_by_id

app_name = 'library'

urlpatterns = [
    path('', show_library, name='show_library'),
    path('search/<str:search_string>/', search_products, name='search_products'),
    path('filter/<int:id>/', filter_category, name='filter_category'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('bookmark_book/', bookmark_book, name='bookmark_book'),
]