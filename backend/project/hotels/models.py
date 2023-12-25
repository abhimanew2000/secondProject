from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    availability = models.BooleanField(default=True)
    amenities = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name