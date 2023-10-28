from django.forms import ModelForm
from .models import Request

class RequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ["book_title", "book_author", "reason"]