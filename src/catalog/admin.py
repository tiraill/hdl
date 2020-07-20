from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.forms import Textarea
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe

from .models import Category, Type, Series, Product, ProductImage, TechDoc, ProductXImage


def image_preview(self):
    if self.link:
        return mark_safe(
            '<a href="{0}" target="_blank"><img src="{0}" alt="{0}" width="80" height="80"/></a>'.format(self.link.image.url)
        )
    else:
        return '(No image)'


class TechDocInline(admin.TabularInline):
    model = TechDoc.product.through
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage.product.through
    extra = 0
    readonly_fields = (image_preview,)


class ProductXImageInline(admin.TabularInline):
    model = ProductXImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TechDoc)
class TechDocAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'links',)
    exclude = ('uid', 'product')
    inlines = (TechDocInline,)

    def file_name(self, obj: TechDoc):
        f_name = getattr(obj.instruction, 'name', None)
        return f_name or '(No file)'
    file_name.short_description = 'Имя файла'

    def links(self, obj: TechDoc):
        return obj.product.count()
    links.short_description = 'Количество ссылок на продукты'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'links', 'image_preview')
    exclude = ('uid',)

    def file_name(self, obj: ProductImage):
        return obj.image.name
    file_name.short_description = 'Имя файла'

    def links(self, obj: ProductImage):
        return obj.product.count()
    links.short_description = 'Количество ссылок на продукты'

    def image_preview(self, obj: ProductImage):
        return mark_safe(
            '<a href="{0}" target="_blank"><img src="{0}" alt="{0}" width="80" height="80"/></a>'.format(obj.image.url)
        )
    image_preview.short_description = 'Изображение'

    inlines = (ProductXImageInline,)


class ProductCustomAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    extra_simlr = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        required=False,
        label="Отметьте, какие объекты будут рекомендоваться",
        widget=FilteredSelectMultiple("объекты", is_stacked=False)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['extra_simlr'].widget.attrs.update({'class': 'custom__simlr'})
        self.fields['extra_simlr'].queryset = self.fields['extra_simlr'].queryset.exclude(slug=self.instance.slug).all()
        if self.instance:
            dependent = Product.objects.filter(simlr=self.instance).all().values_list('id', flat=True)
            if dependent:
                self.fields['extra_simlr'].initial = [el for el in dependent]

    def save(self, *args, commit=True, **kwargs):
        choices = self.cleaned_data['extra_simlr']
        already_dependent = Product.objects.filter(simlr=self.instance).all()
        remove_conn = already_dependent.difference(choices)
        for element in choices:
            element.simlr = self.instance
            element.save()
        for element in remove_conn:
            element.simlr = None
            element.save()
        return super().save(commit=commit)


@admin.register(Product)
class ProductAdmin(MPTTModelAdmin):

    class Media:
        css = {
            'all': ('css/admin/admin.css',)
        }

    form = ProductCustomAdminForm

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
