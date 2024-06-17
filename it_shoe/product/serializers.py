from rest_framework import serializers

from product.entity.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'productName', 'productPrice', 'productDescription', 'registeredDate', 'updatedDate']
        read_only_fields = ['registeredDate', 'updatedDate']