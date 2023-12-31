
from django.contrib import admin
from django.urls import path, include

#show media files
from django.conf import settings
from django.contrib. staticfiles.urls import static



urlpatterns = [
    path("", include('Tracker.urls')),
    path("login/", include('Login.urls')),
    path("admin/", admin.site.urls),
    path("api/", include('Api.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)