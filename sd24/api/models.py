from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        max_length=120,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=120,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"


class SubCategory(Category):
    """Модель подкатегории."""

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        related_name='Subcategorys'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f"{self.name}"


class Product(Category):
    """Модель продукта."""

    price = models.DecimalField(
        blank=False,
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
        null=False
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=False,
        related_name='products'
    )
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 200)],
        format='JPEG',
        options={'quality': 60}
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name}"


class ShoppingCart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Продуктовая корзина'
        verbose_name_plural = 'Продуктовые корзины'
