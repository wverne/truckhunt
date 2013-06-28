from django.db import models
from django.contrib.auth.models import User

class FoodTruck(models.Model):
    name           = models.CharField(max_length=100)    
    website        = models.URLField(null=True, blank=True)
    twitter        = models.URLField(null=True, blank=True)
    yelp           = models.URLField(null=True, blank=True)
    city           = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=100, blank=True,
                                      verbose_name="state/province")

    image_name     = models.CharField(max_length=100, null=True)
    description    = models.TextField(blank=True)
    menu           = models.TextField(blank=True)

    last_checkin   = models.DateTimeField(null=True)
    latitude       = models.FloatField(null=True)
    longitude      = models.FloatField(null=True)

    owner          = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'city']
