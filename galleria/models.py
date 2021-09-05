from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Cat (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Images(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    image = CloudinaryField('image', default = '')
    categs = models.ForeignKey(Cat,null=True, blank=True,on_delete=models.CASCADE)

    
    def get_image_id(self):
        image_id = self.id
        return image_id
        
    
    class Meta:
        ordering = ['-pk']
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name