from django.contrib import admin
from .models import Submission, Prompt

# Register your models here.
admin.site.register(Submission)
admin.site.register(Prompt)