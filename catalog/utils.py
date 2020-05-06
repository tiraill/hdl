import os
import datetime

from uuid import uuid4
from django.core.exceptions import ValidationError

from django.conf import settings


class RandomFilename:

    def __init__(self, folder=settings.PRODUCT_IMAGES_ROOT):
        self.folder = folder

    def __call__(self, instance, filename):
        return self.get_random_filename(filename)

    def get_random_filename(self,
            filename, unique_file_name=True, add_current_date=True
    ):
        if unique_file_name:
            _, ext = os.path.splitext(filename)
            filename = "%s%s" % (str(uuid4()), ext)

        components = []
        if add_current_date:
            components.append(datetime.date.today().strftime("%Y/%m/%d"))
        components.append(filename)

        return os.path.join(*components)


def get_random_filename(*args):
    rnd_filename = RandomFilename()
    return rnd_filename.get_random_filename(args[-1])


def file_size_and_extension(value):
    if value.size > settings.FILE_UPLOAD_LIMIT:
        raise ValidationError(f'Файл слишком большой.'
                              f' Размер файла не должен превышать {settings.FILE_UPLOAD_LIMIT_MULTIPLIER} Мб.')
    elif value.name.split(".")[-1] != "pdf":
        raise ValidationError(f'Файл имеет расширение отличное от .pdf.')