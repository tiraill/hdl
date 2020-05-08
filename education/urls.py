from django.urls import path

from .views import index, buspro, knx

urlpatterns = [
    path('', index, name="education-index"),
    path('buspro/', buspro, name="education-buspro"),
    path('knx/', knx, name="education-knx"),
]
