import logging

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from catalog.mixins import SaveModelSlugMixin
from catalog.utils import file_size_and_extension, get_random_filename


log = logging.getLogger(__name__)


class BrochureCategory(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Категория брошюры'
        verbose_name_plural = 'Категории брошюры'

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=250, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    image = models.ImageField(blank=True, upload_to=get_random_filename)
    svg_file = models.TextField(blank=True, verbose_name="Текст с тегом svg")
    display_name = models.CharField(max_length=250, verbose_name="Название категории вместо изображения", blank=True)
    priority = models.IntegerField(blank=True, default=0)
    general_category = models.BooleanField(default=False, verbose_name='Общая категория')

    def __str__(self):
        return f'{self.title}'


class Brochure(SaveModelSlugMixin, MPTTModel):

    class Meta:
        verbose_name = 'Брошюра'
        verbose_name_plural = 'Брошюра'

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(max_length=250, verbose_name="Наименование")
    slug = models.SlugField(max_length=250, blank=True, verbose_name="Наименование для создания ссылки")
    brochure_file = models.FileField(blank=True, null=True,
                                     validators=[file_size_and_extension], verbose_name="Брошюра")
    brochure_category = models.ForeignKey(BrochureCategory, null=True, blank=True, related_name='brochures',
                                          on_delete=models.SET_NULL)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    priority = models.IntegerField(blank=True, default=0)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




