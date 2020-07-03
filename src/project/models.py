import uuid

from django.db import models
from django.utils import timezone

from catalog.mixins import SaveModelSlugMixin, SaveModelImageMixin


class ProjectCategory(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    title = models.CharField(max_length=250, verbose_name="Наименование",
                             help_text="Не более 250 символов")
    slug = models.SlugField(max_length=350, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")

    def __str__(self):
        return self.title


class Project(SaveModelSlugMixin, models.Model):

    class Meta:
        verbose_name = 'Выполненный проект'
        verbose_name_plural = 'Выполненные проекты'
        ordering = ['-date']

    title = models.CharField(max_length=450, verbose_name="Наименование проектв",
                             help_text="Не более 450 символов")
    slug = models.SlugField(max_length=750, blank=True,
                            verbose_name="Наименование для создания ссылки",
                            help_text="Необязательно для заполнения руками")
    text = models.TextField(verbose_name="Текст описания проекта")
    category = models.ForeignKey(ProjectCategory, related_name='projects',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 verbose_name="Категория проекта")
    date = models.DateField(default=timezone.now)


class ProjectImage(SaveModelImageMixin, models.Model):

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"
        ordering = ['priority']

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField(null=True, verbose_name="Загрузить картинку",)
    priority = models.IntegerField(default=1, verbose_name="Приоритет отображения картинки в галереях")
    project = models.ForeignKey(Project, related_name='images',
                                on_delete=models.CASCADE, verbose_name="Проект к которому привязана картинка",
                                help_text='В этом поле можно использовать автозаполнение')

    def __str__(self):
        return f'<{self.image.name}, размер={self.image.size}, проект={self.project.title}>'
