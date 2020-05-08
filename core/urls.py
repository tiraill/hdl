from django.urls import path

from .views import index, about, contacts, support

urlpatterns = [
    path('', index, name="core-index"),
    path('about/', about, name="core-about"),
    path('contacts/', contacts, name="core-contacts"),
    path('support/', support, name="core-support"),
]
