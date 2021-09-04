from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

