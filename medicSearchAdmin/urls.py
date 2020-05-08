from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicSearch.urls.HomeUrls')),
    path('', include('medicSearch.urls.AuthUrls')),
    path('profile/', include('medicSearch.urls.ProfileUrls')),
    path('medic/', include('medicSearch.urls.MedicUrls')),
    path('my-profile/', include('medicSearch.urls.UserProfileUrls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

