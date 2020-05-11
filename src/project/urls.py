from django.urls import path

from .views import living, commercial, hotels, index

urlpatterns = [
    path('', index, name="project-index"),
    path('living/', living, name="project-living"),
    path('commertial/', commercial, name="project-commercial"),
    path('hotels/', hotels, name="project-hotels"),
]
