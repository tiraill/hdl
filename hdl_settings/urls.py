from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('article/', include('article.urls')),
    path('brochure/', include('brochure.urls')),
    path('catalog/', include('catalog.urls')),
    path('education/', include('education.urls')),
    path('news/', include('news.urls')),
    path('project/', include('project.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
