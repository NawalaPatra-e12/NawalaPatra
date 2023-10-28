from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    rate = models.IntegerField(default=0)
    CATEGORIES = [
        ("Literature & Fiction", "Literature & Fiction"),
        ("Mystery, Thriller & Suspense", "Mystery, Thriller & Suspense"),
        ("Religion & Spirituality", "Religion & Spirituality"),
        ("Romance", "Romance"),
        ("Science Fiction & Fantasy", "Science Fiction & Fantasy"),
    ]

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    reason = models.TextField()