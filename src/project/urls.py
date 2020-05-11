from django.urls import path

from .views import living, commercial, hotels

urlpatterns = [
    path('', living, name="project-index"),
    path('living/', living, name="project-living"),
    path('commertial/', commercial, name="project-commercial"),
    path('hotels/', hotels, name="project-hotels"),
]
