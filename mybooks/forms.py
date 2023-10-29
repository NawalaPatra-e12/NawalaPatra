from django.forms import ModelForm
from .models import Bookmark

class RequestForm(ModelForm):

    class Meta:
        model = Bookmark
        fields = ["review"]