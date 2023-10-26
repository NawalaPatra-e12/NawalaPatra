from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prompt(models.Model):
    theme = models.CharField(max_length=200)
    week = models.IntegerField()
    genre = models.CharField(max_length=200)

    # THEMES = [
    #     ("Literature & Fiction", "Another world fantasy"),
    #     ("Mystery, Thriller & Suspense", "Haloween horror time"),
    #     ("Religion & Spirituality", "About a mysterious ritual"),
    #     ("Romance", "Mafia Romance"),
    #     ("Science Fiction & Fantasy", "Abnormal dimension gate"),
    # ]

    # GENRES = [
    #     ("Literature & Fiction", "Literature & Fiction"),
    #     ("Mystery, Thriller & Suspense", "Mystery, Thriller & Suspense"),
    #     ("Religion & Spirituality", "Religion & Spirituality"),
    #     ("Romance", "Romance"),
    #     ("Science Fiction & Fantasy", "Science Fiction & Fantasy"),
    # ]

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    story = models.TextField()
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

