from itertools import chain

from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import Category, Type, Series, Product

from core.utils import create_pagination


def index(request):
    get_params = request.GET.copy()
    products = Product.objects.all()

    if 'search' in get_params:
        search_query = get_params.pop('search')
        products = products.filter(Q(title__icontains=search_query[0])|
                                   Q(qualifier__icontains=search_query[0]))

    if get_params:
        if 'page' in get_params:
            get_params.pop('page')
        slugged_get_params = {f'{key}__slug': value for key, value in get_params.items()}
        products = products.filter(**slugged_get_params)
        product_types = set([product.type for product in products if product.type])
        product_series = set([product.series for product in products if product.series])

        paginated_products = create_pagination(request, products)

        ctx = {
            'categories': Category.objects.all().order_by('title'),
            'types': product_types,
            'series': product_series,
            'products': paginated_products
        }

        return render(request,
                      template_name="catalog/index.html",
                      context=ctx)

    paginated_products = create_pagination(request, products)

    ctx = {
        'categories': Category.objects.all().order_by('title'),
        'types': Type.objects.all(),
        'series': Series.objects.all(),
        'products': paginated_products
    }

    return render(request,
                  template_name="catalog/index.html",
                  context=ctx)


def product_card(request, slug):

    try:
        product = Product.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request,
                  template_name="catalog/card.html",
                  context={'product': product})

