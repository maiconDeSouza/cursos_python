from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model_year = models.IntegerField(max_length=4, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
