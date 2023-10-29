from django.urls import path
from writersjam.views import show_story, get_story_json, submit_story_ajax
from writersjam.views import story_xml, story_xml_id, story_json, story_json_id, filter_genre

app_name = 'writersjam'

urlpatterns = [
    path('', show_story, name='show_story'),
    path('get-story/', get_story_json, name='get_story_json'),
    path('submit-story/', submit_story_ajax, name='submit_story_ajax'),
    path('xml', story_xml, name='story_xml'),
    path('json', story_json, name='story_json'),
    path('xml/<int:id>/', story_xml_id, name='story_xml_id'),
    path('json/<int:id>/', story_json_id, name='story_json_id'),
    path('filter_genre/', filter_genre, name='filter_genre'),
]