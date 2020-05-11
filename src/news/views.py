from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import News

from src.core.utils import create_pagination, chunks


def index(request):
    news = News.objects.all()

    paginated_news = create_pagination(request, news)

    chunked_news = chunks(paginated_news.object_list, 3)

    ctx = {
        'news': chunked_news,
        'news_paginator': paginated_news
    }

    return render(request,
                  template_name="news/index.html",
                  context=ctx)


def news_card(request, slug):
    try:
        news = News.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request,
                  template_name="news/card.html",
                  context={"news": news})
