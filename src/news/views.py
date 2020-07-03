from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import News

from core.utils import create_pagination, slice_into_columns


def index(request):
    news = News.objects.all()

    paginated_news = create_pagination(request, news)
    chunked_news = slice_into_columns(news_lst=paginated_news.object_list)

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
