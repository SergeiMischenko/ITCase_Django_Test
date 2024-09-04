from rest_framework import serializers

from .models import ProductImage, ProductParameter, Product


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'caption', 'sort_order']


class ProductParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ['name', 'value', 'price', 'sort_order']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    parameters = ProductParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'base_price', 'images', 'parameters', 'sort_order']
