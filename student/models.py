from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class studentdata(models.Model):
    M = 'Male'
    F = 'Female'
    GenderChoices= [(M, 'Male'), (F, 'Female')]

    Name = models.CharField(max_length=20, null=True)
    Regid = models.IntegerField()
    Address = models.TextField()
    Gender = models.CharField(max_length=10, choices=GenderChoices)
    Country = CountryField(null=True)
    Markspercentage = models.FloatField()
