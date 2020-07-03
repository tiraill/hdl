import sys
import logging

from PIL import Image
from io import BytesIO
from uuslug import uuslug

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

log = logging.getLogger(__name__)


class SaveModelSlugMixin:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(s=self.title, instance=self)
        super().save(*args, **kwargs)


class SaveModelImageMixin:

    def save(self, *args, **kwargs):
        try:
            temporary_image = Image.open(self.image)
            output_io_stream = BytesIO()
            temporary_image = temporary_image.convert("RGB")
            temporary_image.thumbnail(settings.IMAGE_THUMBNAIL_SIZE, Image.ANTIALIAS)
            temporary_image.save(output_io_stream, format='JPEG', quality=85)
            output_io_stream.seek(0)
            self.image = InMemoryUploadedFile(output_io_stream, 'image',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(output_io_stream), None)
        except ValueError:
            log.warning("Удалён image файл с сохранением объекта")
        super().save(*args, **kwargs)


class SaveModelSlugImageMixin:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(s=self.title, instance=self)
        try:
            temporary_image = Image.open(self.image)
            output_io_stream = BytesIO()
            temporary_image = temporary_image.convert("RGB")
            temporary_image.thumbnail(settings.IMAGE_THUMBNAIL_SIZE, Image.ANTIALIAS)
            temporary_image.save(output_io_stream, format='JPEG', quality=85)
            output_io_stream.seek(0)
            self.image = InMemoryUploadedFile(output_io_stream, 'image',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(output_io_stream), None)
        except ValueError:
            log.warning("Удалён image файл с сохранением объекта")
        super().save(*args, **kwargs)