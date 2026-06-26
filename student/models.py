from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    mellinumber = models.CharField(max_length=100)
    address = models.TextField()
    birthday = models.DateField()
    


# Create your models here.
