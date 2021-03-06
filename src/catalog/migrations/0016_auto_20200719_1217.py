# Generated by Django 2.2 on 2020-07-19 12:17

from django.db import migrations, models
import django.db.models.deletion

TECHDOC_LINKS = {}


def move_image_links_to_m2m_model(apps, schema_editor):
    ProductImage = apps.get_model('catalog', 'ProductImage')
    ProductXImage = apps.get_model('catalog', 'ProductXImage')

    for product_image in ProductImage.objects.all():
        product_x_image = ProductXImage(
            product=product_image.product,
            link=product_image,
            priority=product_image.priority,
        )
        product_x_image.save()


def save_techdoc_links_to_m2m_model(apps, schema_editor):
    TechDoc = apps.get_model('catalog', 'TechDoc')

    for doc in TechDoc.objects.all():
        TECHDOC_LINKS[doc.product.id] = doc.uid


def load_techdoc_links_to_m2m_model(apps, schema_editor):
    TechDoc = apps.get_model('catalog', 'TechDoc')
    Product = apps.get_model('catalog', 'Product')

    for product_id, techdoc_uid in TECHDOC_LINKS.items():
        doc = TechDoc.objects.get(uid=techdoc_uid)
        product = Product.objects.get(id=product_id)
        doc.product.add(product)
        doc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200604_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория продукта', 'verbose_name_plural': 'Категории продуктов'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Изображение товара', 'verbose_name_plural': 'Изображения товара'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Серия продукта', 'verbose_name_plural': 'Серии продуктов'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип продукта', 'verbose_name_plural': 'Типы продуктов'},
        ),
        migrations.RunPython(save_techdoc_links_to_m2m_model),
        migrations.RemoveField(
            model_name='techdoc',
            name='product',
        ),
        migrations.AddField(
            model_name='techdoc',
            name='product',
            field=models.ManyToManyField(blank=True, help_text='В этом поле можно использовать автозаполнение',
                                         related_name='instructions', to='catalog.Product',
                                         verbose_name='Товары к которым привязана инструкция'),
        ),
        migrations.RunPython(load_techdoc_links_to_m2m_model),
        migrations.CreateModel(
            name='ProductXImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductImage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_links', to='catalog.Product')),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.RunPython(move_image_links_to_m2m_model),
        migrations.RemoveField(
            model_name='productimage',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ManyToManyField(blank=True, help_text='В этом поле можно использовать автозаполнение', through='catalog.ProductXImage', to='catalog.Product', verbose_name='Товары к которым привязана картинка'),
        ),
    ]
