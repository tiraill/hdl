from django.urls import path

from .views import living, commercial, hotels, index, morpheus

urlpatterns = [
    path('', index, name="project-index"),
    path('living/', living, name="project-living"),
    path('commertial/', commercial, name="project-commercial"),
    path('hotels/', hotels, name="project-hotels"),
    path('morpheus/', morpheus, name="project-hotels-morpheus"),
]
