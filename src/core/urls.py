from django.urls import path

from .views import index, about, contacts, support, send_feedback, confident_politics
from catalog.views import index as catalog_index

urlpatterns = [
    path('', index, name="core-index"),
    path('about/', about, name="core-about"),
    path('contacts/', contacts, name="core-contacts"),
    path('support/', support, name="core-support"),
    path('send_feedback/', send_feedback, name="send_feedback"),
    path('site-search/', catalog_index, name="core_search_request"),
    path('politics/', confident_politics, name="core-politics")
]
