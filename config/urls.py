from django.contrib import admin
from django.urls import path, include
from core.views import bienvenida
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', bienvenida, name='bienvenida'),
    path('admin/', admin.site.urls),
    path('api/', include('core.api_urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
]