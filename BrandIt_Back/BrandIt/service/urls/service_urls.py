from django.urls import path

from ..views.service_view import *

app_name = 'service'

urlpatterns = [
    path('services/', ServiceListAPI.as_view(), name='services'),
    path('services/<slug:slug>/',ServiceDetailAPI.as_view(), name='services-detail'),
]