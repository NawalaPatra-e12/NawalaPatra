from django.forms import ModelForm
from forum.models import Discussion, Reply

class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ["description"]

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['text']