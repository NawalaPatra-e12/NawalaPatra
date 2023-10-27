from django.forms import ModelForm
from main.models import Discussion

class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ["Description"]