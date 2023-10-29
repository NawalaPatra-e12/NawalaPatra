from django.forms import ModelForm
from .models import Comment

class RequestForm(ModelForm):

    class Meta:
        model = Comment
        fields = ["comment"]