from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
