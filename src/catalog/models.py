import logging
import uuid

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from catalog.mixins import SaveModelSlugMixin, SaveModelImageMixin
from catalog.utils import file_size_and_extension, get_random_filename

log = logging.getLogger(__name__)


class Category(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов с пробелами")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    image = models.ImageField(null=True, blank=True, upload_to=get_random_filename,
                              verbose_name="Картинка категории")
    svg_image = models.TextField(null=True, blank=True, verbose_name="Картинка в формате SVG с тегом svg")

    def __str__(self):
        return self.title


class Type(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов с пробелами")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")

    def __str__(self):
        return self.title


class Series(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = "Серия продукта"
        verbose_name_plural = "Серии продуктов"

    title = models.CharField(max_length=250, null=True, verbose_name="Наименование",
                             help_text="Не более 250 символов с пробелами")
    slug = models.CharField(max_length=350, null=True, blank=True,
                            verbose_name="Наименование для формирования URL ссылки",
                            help_text="Необязательно для заполнения руками")
    description = models.CharField(max_length=400, null=True, blank=True,
                                   verbose_name="Краткое описание (400 знаков)")
    image = models.ImageField(blank=True, upload_to=get_random_filename)

    def __str__(self):
        return f'{self.title}'


class Currency(models.Model):

    class Meta:
        verbose_name = "Список валют"
        verbose_name_plural = "Список валют"

    code = models.CharField(max_length=10, verbose_name="Кодовое название",  primary_key=True)
    title = models.CharField(max_length=50, verbose_name="Наименование",
                             help_text="Не более 50 символов с пробелами")
    slug = models.SlugField(max_length=100, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    svg_logo = models.TextField(blank=True, verbose_name="Изображение в формате svg")
    char_logo = models.CharField(max_length=20, verbose_name="Символ валюты вместо изображения", blank=True)

    def __str__(self):
        return f'{self.title}'


class Product(SaveModelSlugMixin, MPTTModel):

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов с пробелами")
    slug = models.SlugField(max_length=350, blank=True, verbose_name="Наименование для создания ссылки")
    short_description = models.TextField(verbose_name="Краткое описание товара в карточке товара",
                                         null=True, blank=True)
    general_description = models.TextField(verbose_name="Общее описание")
    func_description = models.TextField(verbose_name="Функции")
    tech_description = models.TextField(verbose_name="Характеристики")
    meta_keywords = models.CharField(max_length=1000, null=True, blank=True,
                                     verbose_name="Слова для тэга keywords (SEO)",
                                     help_text="Не более 1000 символов с пробелами")
    meta_description = models.CharField(max_length=1000, null=True, blank=True,
                                        verbose_name="Описание для тэга description(SEO)",
                                        help_text="Не более 1000 символов с пробелами")
    qualifier = models.CharField(max_length=50, null=True, blank=True, verbose_name="Артикул")
    simlr = models.ForeignKey('self', null=True, blank=True, related_name='similar',
                              on_delete=models.SET_NULL,
                              verbose_name="С каким товаром должен рекомендоваться данный товар",
                              help_text='Укажите в карточке какого товара данный'
                                        ' товар будет показан в разделе \"Рекомендованные товары\"')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children',
                            help_text='В этом поле можно использовать автозаполнение для поиска')
    category = models.ManyToManyField(
        Category,
        related_name='products',
        verbose_name="Категория продукта",
        help_text='В этом поле можно использовать автозаполнение для поиска'
    )
    type = models.ForeignKey(Type, null=True, blank=True, related_name='products',
                             on_delete=models.SET_NULL, verbose_name="Тип продукта",
                             help_text='В этом поле можно использовать автозаполнение для поиска')
    series = models.ForeignKey(Series, null=True, blank=True, related_name='products',
                               on_delete=models.SET_NULL, verbose_name="Серия продукта",
                               help_text='В этом поле можно использовать автозаполнение для поиска')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modified = models.DateTimeField(auto_now=True)
    active_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True,
                                        blank=True, verbose_name="Отображаемая цена")

    def __str__(self):
        return self.title


class TechDoc(models.Model):

    class Meta:
        verbose_name = 'Техническая инструкция к товару'
        verbose_name_plural = 'Технические инструкции к товару'

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    instruction = models.FileField(blank=True, null=True,
                                   validators=[file_size_and_extension], verbose_name="Инструкция")
    product = models.ManyToManyField(
        Product,
        blank=True,
        related_name='instructions',
        verbose_name="Товары к которым привязана инструкция",
        help_text='В этом поле можно использовать автозаполнение'
    )

    def __str__(self):
        return self.instruction.name or '(unknown instruction)'


class ProductImage(SaveModelImageMixin, models.Model):

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField(null=True)
    product = models.ManyToManyField(
        Product,
        blank=True,
        verbose_name="Товары к которым привязана картинка",
        help_text='В этом поле можно использовать автозаполнение',
        through='ProductXImage'
    )

    def __str__(self):
        return f'<{self.image.name}>'


class ProductXImage(models.Model):
    class Meta:
        ordering = ['priority']

    priority = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_links')
    link = models.ForeignKey(ProductImage, on_delete=models.CASCADE)


class ProductXCurrency(models.Model):

    price = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')

    class Meta:
        unique_together = ('currency', 'product')
