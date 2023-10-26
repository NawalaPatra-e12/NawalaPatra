from django.urls import path
from writersjam.views import show_story
# from writersjam.views import ...

app_name = 'writersjam'

urlpatterns = [
    path('', show_story, name='show_story'),
]