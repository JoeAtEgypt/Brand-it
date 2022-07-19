from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from service.urls import service_urls

schema_view = get_schema_view(openapi.Info(
        title="BrandIt API",
        default_version='v1',
        description="Test APIs",
        terms_of_service="localhost:2002",
        contact=openapi.Contact(email="youssefaymanshaker@gmail.com"),
        license=openapi.License(name="Test License"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('services/', include('service.urls')),
    path('works/', include('work.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
