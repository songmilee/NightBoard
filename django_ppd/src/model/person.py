from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=False)
    year = models.DecimalField(max_digits=9999)
    month = models.DecimalField(max_digits=12)
    day = models.DecimalField(max_digits=31)
    #sex = models.BooleanField()