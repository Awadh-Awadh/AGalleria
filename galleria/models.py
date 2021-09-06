from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Cat (models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def get_all_categories(cls):
        return Cat.objects.all()

    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
'''
model creation for image model
contains a link to the cloudinary image fields
each image has one to many relationship with with categories and location
'''
class Images(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    image = CloudinaryField('image', default = '')
    categs = models.ForeignKey(Cat,null=True, blank=True,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,null=True, blank=True,on_delete=models.CASCADE)
    '''
    A function that generates an id for each image
    '''
    def search_images(self, id):
        image = Images.objects.filter(id = id)
        return self.image

    def get_image_id(self):
        image_id = self.id
        return image_id

    def filter_image_by_location(self, location):
        image = Images.objects.filter(location__name = location)
        return self.image

    

    @classmethod
    def get_images(cls):
        return Images.objects.all()
    '''
    An inner optional class meta that defines the ordering of image objects
    '''
    
    class Meta:
        ordering = ['-pk']
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name