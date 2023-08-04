
from django.contrib import admin
from django.urls import path

#show media files
from django.conf import settings
from django.contrib. staticfiles.urls import static

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)