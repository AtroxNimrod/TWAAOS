
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('app_one', include('app_one.urls')),
    path('admin/', admin.site.urls),
    path('',include('app_one.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
