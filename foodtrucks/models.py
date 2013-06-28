from django.db import models
from django.contrib.auth.models import User

class FoodTruck(models.Model):
    name           = models.CharField(max_length=100)    
    website        = models.URLField(null=True)
    twitter        = models.URLField(null=True)
    yelp           = models.URLField(null=True)
    city           = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, 
                                      verbose_name="state/province")

    image_name     = models.CharField(max_length=100, null=True)
    description    = models.TextField(null=True)
    menu           = models.TextField(null=True)

    last_checkin   = models.DateTimeField(null=True)
    latitude       = models.FloatField(null=True)
    longitude      = models.FloatField(null=True)

    owner          = models.ForeignKey('User')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'city']
