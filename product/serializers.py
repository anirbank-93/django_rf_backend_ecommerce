from rest_framework import serializers

# Model
from .models import Product
from .models import ProductCategory

class CreateProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name']

    def create(self, validated_data):
        return ProductCategory.objects.create(**validated_data)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "inventory_count", "category"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']

class ViewProductsSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', "inventory_count", 'category']