from django.shortcuts import render

from .models import BrochureCategory, Brochure


def index(request):
    ctx = {
        'categories': BrochureCategory.objects.order_by('priority'),
        'brochures': Brochure.objects.order_by('priority'),
    }
    return render(
        request,
        template_name="brochure/index.html",
        context=ctx
    )
