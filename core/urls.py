from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name="core-index"),
    path('about/', index, name="core-about"),
    path('contacts/', index, name="core-contacts"),
]
