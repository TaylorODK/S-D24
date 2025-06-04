from .models import Product, Category, SubCategory, ShoppingCart
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    