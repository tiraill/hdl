from django.shortcuts import render

from .models import Category, Type, Manufacturer, Product

from src.core.utils import create_pagination


def index(request):

    get_params = request.GET.copy()


    products = Product.objects.all()

    paginated_products = create_pagination(request, products)

    ctx = {
        'categories': Category.objects.all(),
        'types': Type.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'products': paginated_products
    }

    return render(request,
                  template_name="catalog/index.html",
                  context=ctx)
