from rest_framework import serializers
from app.models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category"]
        depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
