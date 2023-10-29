from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookRate(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    rate = models.IntegerField(default=0)

    CATEGORIES = [
        ("Literature & Fiction", "Literature & Fiction"),
        ("Mystery, Thriller & Suspense", "Mystery, Thriller & Suspense"),
        ("Religion & Spirituality", "Religion & Spirituality"),
        ("Romance", "Romance"),
        ("Science Fiction & Fantasy", "Science Fiction & Fantasy"),
    ]

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coment = models.CharField(max_length=255)