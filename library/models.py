from django.db import models

# Create your models here.
class Book(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    CATEGORIES = [
        ("Literature & Fiction", "Literature & Fiction"),
        ("Mystery, Thriller & Suspense", "Mystery, Thriller & Suspense"),
        ("Religion & Spirituality", "Religion & Spirituality"),
        ("Romance", "Romance"),
        ("Science Fiction & Fantasy", "Science Fiction & Fantasy"),
    ]
