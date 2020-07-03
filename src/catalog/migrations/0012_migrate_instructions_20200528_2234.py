from django.db import migrations
from django.core.files.base import ContentFile
from catalog.models import TechDoc, Product


def move_instructions_to_new_model(self, orm):
    products = Product.objects.all()

    for product in products:
        if product.instruction.name:
            with open(product.instruction.path, 'rb') as file:
                tech_instance = TechDoc(product_id=product.id)
                new_file_instance = ContentFile(file.read())
                tech_instance.instruction.name = product.instruction.name
                tech_instance.instruction.file = new_file_instance
                tech_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20200528_1904'),
    ]

    operations = [
        migrations.RunPython(move_instructions_to_new_model),
        migrations.RemoveField(
            model_name='product',
            name='instruction',
        ),
    ]
