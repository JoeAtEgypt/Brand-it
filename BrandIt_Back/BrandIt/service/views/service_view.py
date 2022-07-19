from django.utils import translation

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from ..models.service_models import MainService, Service
from ..serializers.service_serializers import MainServiceSerializer, ServiceDetailSerializer


class ServiceListAPI(APIView, LimitOffsetPagination):

    def get(self, request):
        lang = translation.get_language_from_request(request)
        context = {"lang": lang}
        content = MainService.objects.translate(lang).last()
        serializer = MainServiceSerializer(content, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceDetailAPI(APIView):

    def get(self, request, slug):
        lang = translation.get_language_from_request(request)
        content = Service.objects.translate(lang).get(slug=slug)
        serializer = ServiceDetailSerializer(content)
        return Response(serializer.data, status=status.HTTP_200_OK)
