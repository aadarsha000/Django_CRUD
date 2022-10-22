from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    