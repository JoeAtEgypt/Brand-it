from rest_framework import serializers


from ..models.work_model import Category

class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)

class MainWorkSerializer(serializers.Serializer):
    main_title = serializers.CharField(max_length=60)
    background_image = serializers.FileField()

    # Category List
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        lang = self.context.get('lang')
        queryset = Category.objects.all().translate(lang)
        data = CategorySerializer(queryset, many=True).data
        return data


class WorkListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    background_image = serializers.FileField()


class WorkDetailSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    background_image = serializers.FileField()
    duration = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=500)

