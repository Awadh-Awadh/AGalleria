from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Images(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    image = CloudinaryField('image', default = '')

    def save_image(self):
        self.save()
    
    class Meta:
        ordering = ['-pk']
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name