# Generated by Django 2.2 on 2020-05-07 15:02

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid

from catalog.mixins import SaveModelSlugMixin
from catalog.utils import get_random_filename, file_size_and_extension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=250, verbose_name='Наименование для создания ссылки')),
            ],
            bases=(SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Наименование')),
                ('slug', models.CharField(blank=True, help_text='Необязательно для заполнения руками', max_length=150, null=True, verbose_name='Наименование для формирования URL ссылки')),
                ('description', models.CharField(blank=True, max_length=400, null=True, verbose_name='Краткое описание (400 знаков)')),
                ('image', models.ImageField(blank=True, upload_to=get_random_filename)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
            bases=(SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товара',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, help_text='Необязательно для заполнения руками', max_length=250, verbose_name='Наименование для создания ссылки')),
            ],
            bases=(SaveModelSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=250, verbose_name='Наименование для создания ссылки')),
                ('general_description', models.CharField(max_length=200, verbose_name='Общее описание')),
                ('func_description', models.CharField(max_length=200, verbose_name='Функции')),
                ('tech_description', models.CharField(max_length=200, verbose_name='Характеристики')),
                ('meta_keywords', models.CharField(blank=True, help_text='Не более 1000 символов с пробелами', max_length=1000, null=True, verbose_name='Слова для тэга keywords (SEO)')),
                ('meta_description', models.CharField(blank=True, help_text='Не более 1000 символов с пробелами', max_length=1000, null=True, verbose_name='Описание для тэга description(SEO)')),
                ('qualifier', models.CharField(blank=True, max_length=50, null=True, verbose_name='Артикул')),
                ('instruction', models.FileField(blank=True, null=True, upload_to='', validators=[
                    file_size_and_extension], verbose_name='Инструкция')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('category', models.ManyToManyField(related_name='products', to='catalog.Category')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.ProductImage', verbose_name='Изображение товара')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.Manufacturer')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Product')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.Type')),
            ],
            options={
                'abstract': False,
            },
            bases=(SaveModelSlugMixin, models.Model),
        ),
    ]
