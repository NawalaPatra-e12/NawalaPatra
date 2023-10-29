from django.db import models
from django.contrib.auth.models import User
from main.models import UserProfile
from library.models import Book

# Create your models here.
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(blank=True, max_length=1000)


