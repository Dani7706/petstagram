from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_last.common.urls')),
    path('accounts/', include('petstagram_last.accounts.urls')),
    path('pets/', include('petstagram_last.pets.urls')),
    path('photos/', include('petstagram_last.photos.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)