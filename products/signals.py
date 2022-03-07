from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product, Order

@receiver(post_save, sender=Order)
def decrement_stock(sender, instance=None, created=False, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product.id)
        print(product)
        product.stock -= 1
        product.save()