from django.contrib import admin
from django.urls import path, include

from service.urls import service_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls'))
]
