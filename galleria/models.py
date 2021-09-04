from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey("Categories", on_delete= models.CASCADE)
    location = models.ForeignKey("Location", on_delete= models.CASCADE)
    

    class Meta:
        ordering = ['-pk']


    def __str__(self):
        return f'{self.name}'

class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Location(models.Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location