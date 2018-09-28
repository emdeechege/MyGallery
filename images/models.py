from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name= models.CharField(max_length=50)
    description = HTMLField()
    gallery_image = models.ImageField(upload_to='picha/', blank=True)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location)

    @classmethod
    def all_images():

        return Image.objects.all()

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location
