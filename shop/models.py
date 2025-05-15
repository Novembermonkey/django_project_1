
from decimal import Decimal

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    category = models.ForeignKey(Category, related_name = "product", on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField(upload_to = 'products/')
    discount = models.IntegerField(default=0)
    amount = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        return self.price * Decimal(f"{1 - (self.discount/100)}")

class Order(BaseModel):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"{self.name} - {self.quantity}"


class Comment(BaseModel):
    class RatingChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE, null = True, blank = True)
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.THREE)

    def __str__(self):
        return f"{self.name} - {self.rating}"

