# Generated by Django 2.2 on 2020-05-11 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200508_1117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacturer',
            new_name='Series',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Серия', 'verbose_name_plural': 'Серия'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='manufacturer',
            new_name='series',
        ),
    ]