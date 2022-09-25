from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.TextField(max_length=300, blank=False, default='')
    active = models.BooleanField(default=False)
    notes = models.TextField(max_length=4000)

