from django.urls import path

from .views import index, news_card

urlpatterns = [
    path('', index, name="news-index"),
    path('news/<str:slug>', news_card, name='news-card'),
]
