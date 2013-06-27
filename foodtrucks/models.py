from django.db import models

class FoodTruck(models.Model):
    name           = models.CharField(max_length=100)    
    website        = models.URLField()
    twitter        = models.URLField()
    yelp           = models.URLField()
    city           = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, 
                                      verbose_name="state/province")

    image_name     = models.CharField(max_length=100)
    description    = models.TextField()
    menu           = models.TextField()

    last_checkin   = models.DateTimeField()
    latitude       = models.FloatField()
    longitude      = models.FloatField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'city']
