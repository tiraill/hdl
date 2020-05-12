import logging

from django.db import models
from mptt.models import MPTTModel


log = logging.getLogger(__name__)


class EmailReceivers(models.Model):
    class Meta:
        verbose_name = 'Получатель уведомлений'
        verbose_name_plural = 'Получатели уведомлений'

    email = models.CharField(max_length=250, verbose_name="Почта", blank=False)
    is_send_email_notifications = models.BooleanField(default=True, verbose_name="Отправлять сообщения по почте")

    def __str__(self):
        return f'{self.email}'


class FeedbackHistory(models.Model):
    class Meta:
        verbose_name = 'История уведомлений'
        verbose_name_plural = 'Истории уведомлений'

    first_name = models.CharField(max_length=50, verbose_name="Имя", blank=True)
    email = models.CharField(max_length=50, verbose_name="Email")
    phone_number = models.CharField(max_length=25, verbose_name="Телефон")
    comment = models.CharField(max_length=999, verbose_name="Комментарий", blank=True)
    datatime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.email}'
