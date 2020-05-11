from django.urls import path

from .views import index, about, contacts, support, confident_politics

urlpatterns = [
    path('', index, name="core-index"),
    path('about/', about, name="core-about"),
    path('contacts/', contacts, name="core-contacts"),
    path('support/', support, name="core-support"),
    path('politics/', confident_politics, name="core-politics")
]
