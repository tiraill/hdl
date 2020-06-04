from django.contrib import admin
from django.db import models
from django.forms import Textarea
from mptt.admin import MPTTModelAdmin

from .models import Category, Type, Series, Product, ProductImage, TechDoc


class TechDocInline(admin.StackedInline):
    model = TechDoc
    extra = 0
    can_delete = False
    fields = ('uid', 'instruction')

    def has_add_permission(self, request, obj=None):
        return False


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    can_delete = False
    fields = ['uid', 'image', 'priority']

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')


@admin.register(TechDoc)
class TechDocAdmin(admin.ModelAdmin):
    list_display = ('uid', 'get_product')
    list_filter = ('product__title',)
    search_fields = ('product__title',)
    autocomplete_fields = ('product',)
    exclude = ('uid',)

    def get_product(self, instance):
        if instance and instance.product:
            return instance.product.title
        else:
            return f"Продукт не указан, либо был удален"
    get_product.short_description = "Продукт, к которому прикреплена инструкция"


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('uid', 'get_product')
    list_filter = ('product__title',)
    search_fields = ('product__title',)
    autocomplete_fields = ('product',)
    exclude = ('uid',)

    def get_product(self, instance):
        if instance and instance.product:
            return instance.product.title
        else:
            return f"Продукт не указан, либо был удален"
    get_product.short_description = "Продукт, к которому прикреплено фото"


@admin.register(Product)
class ProductAdmin(MPTTModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
        models.CharField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
    }

    list_display = ('title', 'get_category', 'get_type', 'get_manufacturer', 'creation_date', 'qualifier')
    list_filter = ('category__title', 'type__title', 'series__title', 'creation_date')
    autocomplete_fields = ('category', 'type', 'series', 'simlr')
    search_fields = ('title', 'qualifier')
    inlines = (ProductImageInline, TechDocInline)

    def get_category(self, instance):
        if instance:
            all_categories = instance.category.all()
            return ", ".join([item.title for item in all_categories])
        else:
            return f"Категория не указана, либо была удалена"
    get_category.short_description = "Категория товара"

    def get_type(self, instance):
        if instance and instance.type:
            return instance.type.title
        else:
            return f"Тип не указан, либо был удалена"
    get_type.short_description = "Тип товара"

    def get_manufacturer(self, instance):
        if instance and instance.series:
            return instance.series.title
        else:
            return f"Производитель не указан, либо был удалён"
    get_manufacturer.short_description = "Производитель товара"
