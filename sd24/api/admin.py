from django.contrib import admin
from .models import Category, SubCategory, Product
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image_tag'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ['name']}

    @admin.display(description="Превью")
    def image_tag(self, obj):
        return mark_safe(
            '<img src="/media/%s" width="50" height="50" />' % (
                obj.image
            )
        )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
        'image'
    )
    list_filter = ('name', 'category',)
    search_fields = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ['name']}

    @admin.display(description="Превью")
    def image_tag(self, obj):
        return mark_safe(
            '<img src="/media/%s" width="50" height="50" />' % (
                obj.image
            )
        )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'subcategory',
        'image',
        'price'
    )
    list_filter = ('name', 'subcategory', 'price',)
    search_fields = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ['name']}

    @admin.display(description="Превью")
    def image_tag(self, obj):
        return mark_safe(
            '<img src="/media/%s" width="50" height="50" />' % (
                obj.image
            )
        )