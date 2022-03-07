from .models import Product, Order
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'stock', 'description', 'created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'owner','address', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        product = Product.objects.get(id=validated_data['product'].id)
        if product.stock > 0:
            return Order.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("Product out of stock")