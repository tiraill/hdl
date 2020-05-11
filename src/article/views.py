from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import Article

from core.utils import create_pagination, slice_into_columns


def index(request):
    articles = Article.objects.all()

    paginated_articles = create_pagination(request, articles)
    chunked_articles = slice_into_columns(news_lst=paginated_articles.object_list)

    ctx = {
        'articles': chunked_articles,
        'articles_paginator': paginated_articles
    }

    return render(request,
                  template_name="article/index.html",
                  context=ctx)


def article_card(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request,
                  template_name="article/card.html",
                  context={"article": article})
