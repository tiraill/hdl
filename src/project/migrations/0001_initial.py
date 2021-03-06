# Generated by Django 2.2 on 2020-05-14 19:30

import catalog.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 450 символов', max_length=450, verbose_name='Наименование проектв')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=750, verbose_name='Наименование для создания ссылки')),
                ('text', models.TextField(verbose_name='Текст описания проекта')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Выполненный проект',
                'verbose_name_plural': 'Выполненные проекты',
                'ordering': ['-date'],
            },
            bases=(catalog.mixins.SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 250 символов', max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=350, verbose_name='Наименование для создания ссылки')),
            ],
            options={
                'verbose_name': 'Категория проекта',
                'verbose_name_plural': 'Категории проектов',
            },
            bases=(catalog.mixins.SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Загрузить картинку')),
                ('priority', models.IntegerField(default=1, verbose_name='Приоритет отображения картинки в галереях')),
                ('project', models.ForeignKey(blank=True, help_text='В этом поле можно использовать автозаполнение', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project.Project', verbose_name='Товар для картинки')),
            ],
            options={
                'verbose_name': 'Изображение проекта',
                'verbose_name_plural': 'Изображения проектов',
                'ordering': ['priority'],
            },
            bases=(catalog.mixins.SaveModelImageMixin, models.Model),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='project.ProjectCategory', verbose_name='Категория проекта'),
        ),
    ]
