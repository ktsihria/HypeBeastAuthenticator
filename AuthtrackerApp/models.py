from django.db import models

# Create your models here.

class Barcode(models.Model):
    barcode = models.CharField(max_length=9)
