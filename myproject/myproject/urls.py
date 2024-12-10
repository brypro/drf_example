from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patients.urls')), 

    # OpenAPI schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Documentación Swagger
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Documentación ReDoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

