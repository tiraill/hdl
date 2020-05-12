import sys
import logging
import uuid

from PIL import Image
from io import BytesIO

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from mptt.models import MPTTModel, TreeForeignKey

from catalog.mixins import SaveModelSlugMixin
from catalog.utils import file_size_and_extension, get_random_filename

from django.conf import settings


log = logging.getLogger(__name__)


class Category(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=250, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")

    def __str__(self):
        return self.title


class Type(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=250, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")

    def __str__(self):
        return self.title


class Series(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серия"

    title = models.CharField(max_length=150, null=True, verbose_name="Наименование")
    slug = models.CharField(max_length=150, null=True, blank=True,
                            verbose_name="Наименование для формирования URL ссылки",
                            help_text="Необязательно для заполнения руками")
    description = models.CharField(max_length=400, null=True, blank=True,
                                   verbose_name="Краткое описание (400 знаков)")
    image = models.ImageField(blank=True, upload_to=get_random_filename)

    def __str__(self):
        return f'{self.title}'


class Product(SaveModelSlugMixin, MPTTModel):

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=250, blank=True, verbose_name="Наименование для создания ссылки")
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
    instruction = models.FileField(blank=True, null=True,
                                   validators=[file_size_and_extension], verbose_name="Инструкция")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    category = models.ManyToManyField(Category, related_name='products')
    type = models.ForeignKey(Type, null=True, blank=True, related_name='products',
                             on_delete=models.SET_NULL)
    series = models.ForeignKey(Series, null=True, blank=True, related_name='products',
                               on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ['priority']

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField(null=True)
    priority = models.IntegerField(default=1)
    product = models.ForeignKey(Product, related_name='images',
                                on_delete=models.CASCADE,
                                null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            temporary_image = Image.open(self.image)
            output_io_stream = BytesIO()
            temporary_image = temporary_image.convert("RGB")
            temporary_image.thumbnail(settings.IMAGE_THUMBNAIL_SIZE, Image.ANTIALIAS)
            temporary_image.save(output_io_stream, format='JPEG', quality=85)
            output_io_stream.seek(0)
            self.image = InMemoryUploadedFile(output_io_stream, 'image',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(output_io_stream), None)
        except ValueError:
            log.warning("Удалён image файл с сохранением объекта")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'<{self.image.name}, размер={self.image.size}, товар={self.product.title}>'
