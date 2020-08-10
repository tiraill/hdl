from django import forms
from django.contrib import admin, messages
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.forms import Textarea
from django.shortcuts import redirect
from django.urls import path
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


from .models import Category, Type, Series, Product, ProductImage, TechDoc, ProductXImage, Currency, ProductXCurrency


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
    verbose_name_plural = "Связи документации и товара"
    verbose_name = "связь документации и товара"


class ProductImageInline(admin.TabularInline):
    model = ProductImage.product.through
    extra = 0
    readonly_fields = (image_preview,)
    verbose_name_plural = "Изображения товара"
    verbose_name = "изображение товара"


class ProductXImageInline(admin.TabularInline):
    model = ProductXImage
    extra = 0
    verbose_name_plural = "Связи с товарами"
    verbose_name = "связь с товаром"


class ProductXCurrencyInline(admin.TabularInline):

    model = ProductXCurrency
    extra = 0
    verbose_name_plural = "Цены в разных валютах"
    verbose_name = "цену в валюте"


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


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'char_logo')
    search_fields = ('title', 'slug')

    def has_delete_permission(self, request, obj=None):
        return False

    def set_active_currency(self, obj: ProductImage):
        return format_html('<a class="button" href="%s/set_active_currency/">Применить для всех товаров</a>' % obj.id)

    set_active_currency.short_description = 'Установить по умолчанию'
    set_active_currency.allow_tags = True

    def get_urls(self):
        custom_urls = []
        urls = super().get_urls()
        custom_urls += [
            path('<path:object_id>/set_active_currency/', self.admin_site.admin_view(set_currency_method),
                 name='vision_questionarioistituzionescolastica_generatepdf')
        ]
        return custom_urls + urls


def set_currency_method(request, object_id, form_url='', extra_context=None):
    currency = Currency.objects.filter(pk=object_id).first()
    update_count = Product.objects.all().update(active_currency=currency)
    messages.add_message(request, messages.INFO, f'Валюта {currency} установлена для {update_count} продуктов')
    return redirect(request.META['HTTP_REFERER'])


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        exclude = ('parent', 'slug', 'modified', 'lft', 'rght', 'tree_id', 'level')

    title = Field(attribute='title', column_name='Title')
    slug = Field(attribute='slug', column_name='slug')
    short_description = Field(attribute='short_description', column_name='short_description')
    general_description = Field(attribute='general_description', column_name='general_description')
    func_description = Field(attribute='func_description', column_name='func_description')
    tech_description = Field(attribute='tech_description', column_name='tech_description')
    meta_keywords = Field(attribute='meta_keywords', column_name='meta_keywords')
    meta_description = Field(attribute='meta_description', column_name='meta_description')
    qualifier = Field(attribute='qualifier', column_name='qualifier')
    rub_price = Field()
    usd_price = Field()
    eur_price = Field()
    prices = Field(
        attribute='prices',
        widget=widgets.ManyToManyWidget(
            ProductXCurrency,
            field='price',
            separator='|')
    )

    def save(self, commit=True):
        rub_price = self.cleaned_data.get('rub_price', None)
        # ...do something with extra_field here...
        return super(ProductResource, self).save(commit=commit)

    def dehydrate_rub_price(self, product: Product):
        rub_price = product.prices.filter(currency_id='RUB').first()
        return getattr(rub_price, 'price', '-')

    def dehydrate_usd_price(self, product: Product):
        usd_price = product.prices.filter(currency_id='USD').first()
        return getattr(usd_price, 'price', '-')

    def dehydrate_eur_price(self, product: Product):
        eur_price = product.prices.filter(currency_id='EUR').first()
        return getattr(eur_price, 'price', '-')

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):

    # def import_data(self, dataset, dry_run=False, raise_errors=False,
    #                 use_transactions=None, collect_failed_rows=False, **kwargs):
    #
    #     return super().import_data(dataset, dry_run, raise_errors, use_transactions, collect_failed_rows, **kwargs)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):

    class Media:
        css = {
            'all': ('css/admin/admin.css',)
        }

    resource_class = ProductResource
    form = ProductCustomAdminForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
        models.CharField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
    }

    list_display = ('title', 'get_category', 'get_type', 'get_manufacturer', 'creation_date', 'qualifier')
    list_filter = ('category__title', 'type__title', 'series__title', 'creation_date')
    autocomplete_fields = ('category', 'type', 'series', 'simlr')
    search_fields = ('title', 'qualifier')
    exclude = ('parent', 'simlr')
    inlines = (ProductXCurrencyInline, ProductImageInline, TechDocInline)

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

