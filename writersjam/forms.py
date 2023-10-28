from django.forms import ModelForm
from writersjam.models import Submission, Prompt

class submissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ["title", "story", "date", "user", "username"]
