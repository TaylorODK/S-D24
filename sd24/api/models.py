from django.db import models

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
        related_name='Subcategory'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f"{self.name}"


class Product(Category):
    """Модель продукта."""

    price = models.DecimalField()
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=False,
        related_name='product'
    )
    image_small = 
