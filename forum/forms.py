from django.forms import ModelForm
from forum.models import Discussion, Reply

class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ["user","description","date"]

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['text']