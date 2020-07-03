# Generated by Django 2.2 on 2020-05-11 18:45

import catalog.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 250 символов', max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=350, verbose_name='Наименование для создания ссылки')),
            ],
            options={
                'verbose_name': 'Тема статьи',
                'verbose_name_plural': 'Темы статей',
            },
            bases=(catalog.mixins.SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 250 символов', max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=350, verbose_name='Наименование для создания ссылки')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='article.Topic', verbose_name='Тема статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-date'],
            },
            bases=(catalog.mixins.SaveModelSlugImageMixin, models.Model),
        ),
    ]