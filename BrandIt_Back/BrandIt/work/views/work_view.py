from django.utils import translation

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from ..models.work_model import MainWork, Work
from ..serializers.work_serializer import MainWorkSerializer, WorkListSerializer, WorkDetailSerializer


class WorkAPI(APIView, LimitOffsetPagination):

    def get(self, request):
        lang = translation.get_language_from_request(request)

        main_content = MainWork.objects.translate(lang).last()
        main_data = MainWorkSerializer(main_content, context={'lang':lang}).data

        category = request.query_params.get('category')
        if not category:
            works = Work.objects.all()
        else:
            works = Work.objects.filter(category__slug=category)

        works = works.translate(lang)
        paginated_queryset = self.paginate_queryset(works, request, view=self)
        serializer = WorkListSerializer(paginated_queryset, many=True)
        works_data = self.get_paginated_response(serializer.data).data
        return Response({'main': main_data,
                         'works': works_data
                         }, status=status.HTTP_200_OK)


class WorkDetailAPI(APIView):

    def get(self, request, slug):
        lang = translation.get_language_from_request(request)

        work_content = Work.objects.translate(lang).get(slug=slug)
        data = WorkDetailSerializer(work_content).data
        return Response(data, status=status.HTTP_200_OK)


