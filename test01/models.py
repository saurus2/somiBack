from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=20, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'
