from django.urls import path

from ..views.work_view import *


urlpatterns = [
    path('', WorkAPI.as_view(), name='works'),
    path('<slug:slug>/', WorkDetailAPI.as_view(), name='works'),
]
