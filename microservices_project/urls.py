from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del schema
schema_view = get_schema_view(
   openapi.Info(
      title="SIT API",
      default_version='v1',
      description="Documentación de la API de SIT (Academics + Users)",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="soporte@sit.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('api/academics/', include('academics.urls')),
    path('api/auth/', include('users.urls')),

    # Swagger/OpenAPI
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
