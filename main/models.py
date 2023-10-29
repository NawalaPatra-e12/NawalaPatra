from django.db import models
from django.contrib.auth.models import User
from library.models import Book

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bookmarked_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.user.username