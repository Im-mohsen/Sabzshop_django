from rest_framework import serializers
from shop.models import Product, ProductFeatured


class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatured
        fields = ['name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeaturesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'new_price', 'features']
