from django.urls import path

from .views import index, about, contacts, support, send_feedback, confident_politics, core_search_request

urlpatterns = [
    path('', index, name="core-index"),
    path('about/', about, name="core-about"),
    path('contacts/', contacts, name="core-contacts"),
    path('support/', support, name="core-support"),
    path('send_feedback/', send_feedback, name="send_feedback"),
    path('site-search/', core_search_request, name="core_search_request"),
    path('politics/', confident_politics, name="core-politics")
]
