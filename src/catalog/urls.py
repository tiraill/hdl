from django.urls import path

from .views import index, product_card

urlpatterns = [
    path('', index, name="catalog-index"),
    path('product/<str:slug>', product_card, name="catalog-product"),
]
