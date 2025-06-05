from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
from django.utils.text import slugify

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    """Модель подкатегории."""

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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField(
        max_length=120,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=120,
        verbose_name='Слаг'
    )
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
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение'
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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
