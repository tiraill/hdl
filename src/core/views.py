import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from core.contact import ContactForm, SearchForm
from django.core.mail import EmailMessage
from django.db.models import Q
from hdl_settings.settings import EMAIL_SENDER
from .models import FeedbackHistory, EmailReceivers

from news.models import News
from article.models import Article
from catalog.models import Product
from brochure.models import Brochure

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


def prepare_elements(elements_result, url_tag: str = None) -> list:
    return [{'url_tag': url_tag, 'element': element} for element in elements_result]


def core_search_request(request):

    if request.method == 'POST':
        search_request_form: SearchForm = SearchForm(request.POST)
        if search_request_form.is_valid():
            result = []
            news = News.objects.filter(Q(title__icontains=search_request_form.data['search_q'])|
                                       Q(text__icontains=search_request_form.data['search_q']))
            articles = Article.objects.filter(Q(title__icontains=search_request_form.data['search_q'])|
                                              Q(text__icontains=search_request_form.data['search_q']))
            products = Product.objects.filter(Q(title__icontains=search_request_form.data['search_q'])|
                                              Q(qualifier__icontains=search_request_form.data['search_q']))
            brochures = Brochure.objects.filter(title__icontains=search_request_form.data['search_q'])

            if news:
                result.extend(prepare_elements(news, 'news-card'))
            if articles:
                result.extend(prepare_elements(articles, 'article-card'))
            if products:
                result.extend(prepare_elements(products, 'catalog-product'))
            if brochures:
                result.extend(prepare_elements(brochures))

            return render(request, 'site_search_result.html',
                          context={"results": result})
        return render(request, 'index.html', {'search_form': search_request_form})
