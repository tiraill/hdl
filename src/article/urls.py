from django.urls import path

from .views import index, article_card

urlpatterns = [
    path('', index, name="article-index"),
    path('article/<str:slug>', article_card, name='article-card'),
]
