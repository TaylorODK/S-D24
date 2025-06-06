from django.shortcuts import render
from .models import (
    Category,
    SubCategory,
    Product,
    ShoppingCart
)
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    ProductCreateSerializer,
    ProductShowSerializer,
    ShoppingCartSerializer
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets, mixins
# Create your views here.


class CategoryViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer


class SubCategoryViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = SubCategory.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = SubCategorySerializer


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all().select_related(
        'subcategory'
    ).prefetch_related(
        'category'
    )
    pagination_class = (PageNumberPagination,)
    permission_classes = (AllowAny,)
    serializer_class = ProductShowSerializer
