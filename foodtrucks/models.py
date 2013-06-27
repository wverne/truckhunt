from django.db import models

class FoodTruck(models.Model):
    name           = models.CharField(max_length=100)    
    website        = models.URLField()
    twitter        = models.URLField()
    website        = models.URLField()
    city           = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, 
                                      verbose_name="state/province")
    image_name     = models.CharField(max_length=100)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'city']


# Create your models here.
