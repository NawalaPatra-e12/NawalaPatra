from django.db import models
from django.contrib.auth.models import User

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title=models.TextField()
    date = models.DateField(null=True)
    description = models.TextField()
