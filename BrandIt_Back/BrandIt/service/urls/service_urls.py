from django.urls import path

from ..views.service_view import *


urlpatterns = [
    path('', ServiceListAPI.as_view(), name='services'),
    path('<slug:slug>/',ServiceDetailAPI.as_view(), name='service-detail'),
]