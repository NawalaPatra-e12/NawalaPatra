from django.urls import path
from forum.views import show_discussion,get_discussion_json, submit_discussion_ajax, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'forum'

urlpatterns = [
    path('', show_discussion, name='show_discussion'),
    path('get-discussion/', get_discussion_json, name='get_discussion_json'),
    path('submit-discussion/', submit_discussion_ajax, name='submit_discussion_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]