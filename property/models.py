from django.db import models


class Property(models.Model):
    url = models.CharField(max_length=512, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    number_of_bedrooms = models.IntegerField(null=False, blank=False)
    is_furnished = models.BooleanField(null=False, blank=False)
    location = models.CharField(max_length=300, null=True, blank=True)
