from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prompt(models.Model):
    theme = models.CharField(max_length=200)
    week = models.IntegerField()
    genre = models.CharField(max_length=200)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=150, null=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    story = models.TextField()
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

