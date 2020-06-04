import logging

from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import Category, Type, Series, Product

from core.contact import SearchForm
from core.utils import create_pagination

logger = logging.getLogger('catalog')


def index(request):
    get_params = request.GET.copy()
    products = Product.objects.all()

    ctx = {'categories': Category.objects.all().order_by('title')}

    if request.method == 'POST':
        ctx.update({
            'types': Type.objects.all(),
            'series': Series.objects.all(),
        })
        search_request_form: SearchForm = SearchForm(request.POST)
        if search_request_form.is_valid():
            products = Product.objects.filter(Q(title__icontains=search_request_form.data['search_q'])|
                                              Q(qualifier__icontains=search_request_form.data['search_q']))
            paginated_products = create_pagination(request, products)
            ctx.update({'products': paginated_products})
            return render(request,
                          template_name="catalog/index.html",
                          context=ctx)
        ctx.update({
            'search_form': search_request_form,
            'products': Product.objects.all()
        })
        return render(request,
                      template_name="catalog/index.html",
                      context=ctx)

    if 'search' in get_params:
        search_query = get_params.pop('search')
        products = products.filter(Q(title__icontains=search_query[0])|
                                   Q(qualifier__icontains=search_query[0]))

    if get_params:
        products, product_types, product_series = filter_with_get_params(get_params, products)
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


def filter_with_get_params(get_params, products):
    # first we remove filter
    if 'page' in get_params:
        get_params.pop('page')

    # here we create params to filter from all products with received filters
    slugged_get_params = {f'{key}__slug': value for key, value in get_params.items()}
    logger.debug('Filters slug %s' % slugged_get_params)
    # here we need variable which'll be used for adding a filter after receiving info
    # about filter types
    additional_type_filter = {}
    if ('category' in get_params) and ('type' in get_params):
        # removing additional type filtering, just category
        additional_type_filter['type__slug'] = slugged_get_params.pop('type__slug')
    logger.debug('Filters slug after type removal %s' % slugged_get_params)
    logger.debug('Additional filter slug %s' % additional_type_filter)
    products = products.filter(**slugged_get_params)
    # receiving all types in current category, so we could present it on page
    product_types = set([product.type for product in products if product.type])
    if additional_type_filter:
        # adding type filter, if it's needed
        products = products.filter(**additional_type_filter)
    product_series = set([product.series for product in products if product.series])
    return products, product_types, product_series


def product_card(request, slug):

    try:
        product = Product.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request,
                  template_name="catalog/card.html",
                  context={'product': product})

