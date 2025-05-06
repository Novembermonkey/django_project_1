from os.path import defpath
from decimal import Decimal

from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    category = models.ForeignKey(Category, related_name = "product", on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField(upload_to = 'products/')
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        return self.price * Decimal(f"{1 - (self.discount/100)}")






