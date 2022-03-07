from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

# Create your models here.

class Product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    title = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)