from .models import Product, Category, SubCategory, ShoppingCart
from rest_framework import serializers
from django.core.files.base import ContentFile
import uuid
import base64


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            data = ContentFile(base64.b64decode(imgstr), name=filename)

        return super().to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        requred=True,
        allow_null=False
    )
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image'
        )


class SubCategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        requred=True,
        allow_null=False
    )
    slug = serializers.SlugField(required=False)

    class Meta:
        model = SubCategory
        fields = (
            'name',
            'slug',
            'image',
            'category'
        )


class ProductShowSerializer(serializers.ModelSerializer):
    image_medium = serializers.SerializerMethodField()
    image_small = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(),
        many=False
    )

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'image',
            'image_medium',
            'image_small'
        )

    def get_image_medium(self, obj):
        if obj.image_medium:
            return self.context['request'].build_absolute_uri(obj.image_medium.url)
        return None

    def get_image_small(self, obj):
        if obj.image_small:
            return self.context['request'].build_absolute_url(obj.image_small.url)
        return None
    
    def get_category(self, obj):
        if obj.subcategory:
            return obj.subcategory.category.name
        return None


class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'subcategory',
            'price',
            'image'
        )


class ShoppingCartSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = (
            'user',
            'product',
            'count',
            'price'
        )

    def get_count(self, obj):
        return ShoppingCart.objects.filter(user=obj.user, product=obj.product).count()

    def get_price(self, obj):
        products = ShoppingCart.objects.filter(user=obj.user)
        price = 0
        for product in products:
            price += product.price
        return price
