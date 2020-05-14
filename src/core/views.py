import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from core.contact import ContactForm
from django.core.mail import EmailMessage
from hdl_settings.settings import EMAIL_SENDER
from .models import FeedbackHistory, EmailReceivers


log = logging.getLogger(__name__)


def index(request):

    return render(request,
                  template_name="index.html")


def about(request):

    return render(request,
                  template_name="about.html")


def contacts(request):

    return render(request,
                  template_name="contacts.html")


def support(request):

    return render(request,
                  template_name="support.html")


def confident_politics(request):

    return render(request,
                  template_name="confident.html")


def send_feedback(request):

    if request.method == 'POST':
        form: ContactForm = ContactForm(request.POST)
        if form.is_valid():
            body = f'''Поступила новая заявка
            Имя: {form.data['first_name']}
            Email: {form.data['email']}
            Телефон: {form.data['phone_number']}
            Комментарий: {form.data['comment']}
            Дополнительная информация по заявке: {form.data['additional_info']}
            '''
            email = EmailMessage(
                from_email=EMAIL_SENDER,
                subject='Новая заявка',
                body=body,
            )
            comment = f"ТИП ЗАЯВКИ: {form.data['additional_info']}\n\n" \
                      f"Комментарий клиента: {form.data['comment']}"
            feedback = FeedbackHistory(
                first_name=form.data['first_name'],
                email=form.data['email'],
                phone_number=form.data['phone_number'],
                comment=comment
            )
            feedback.save()
            receivers = EmailReceivers.objects.filter(is_send_email_notifications=True)
            if receivers:
                email.to = [user.email for user in receivers]
                try:
                    email.send()
                except Exception as exc:
                    log.exception(exc)
            return HttpResponseRedirect(reverse('core-index'))
        return render(request, 'index.html', {'contact_form': form})
