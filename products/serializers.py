from rest_framework import serializers
from .models import Product, ImageProduct


class ImageProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ImageProduct
        fields = ('image', )


class ProductSerializer(serializers.ModelSerializer):
    image = ImageProductSerializer(many=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'user', 'image')