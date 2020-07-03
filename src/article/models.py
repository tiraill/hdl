from django.db import models
from django.utils import timezone

from catalog.mixins import SaveModelSlugMixin, SaveModelSlugImageMixin


class Topic(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статей'

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")

    def __str__(self):
        return self.title


class Article(SaveModelSlugImageMixin, models.Model):

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    text = models.TextField(verbose_name="Текст статьи")
    topic = models.ForeignKey(Topic, related_name='articles',
                              on_delete=models.SET_NULL,
                              blank=True, null=True,
                              verbose_name="Тема статьи")
    date = models.DateField(default=timezone.now)
    image = models.ImageField()
