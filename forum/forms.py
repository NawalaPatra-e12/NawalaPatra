from django.forms import ModelForm
from forum.models import Discussion

class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ["user","description","date"]