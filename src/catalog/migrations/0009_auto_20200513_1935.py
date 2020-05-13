# Generated by Django 2.2 on 2020-05-13 19:35

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200513_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(help_text='В этом поле можно использовать автозаполнение для поиска', related_name='products', to='catalog.Category', verbose_name='Категория продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='В этом поле можно использовать автозаполнение для поиска', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.ForeignKey(blank=True, help_text='В этом поле можно использовать автозаполнение для поиска', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.Series', verbose_name='Серия продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, help_text='В этом поле можно использовать автозаполнение для поиска', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.Type', verbose_name='Тип продукта'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, help_text='В этом поле можно использовать автозаполнение', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.Product', verbose_name='Товар для картинки'),
        ),
    ]
