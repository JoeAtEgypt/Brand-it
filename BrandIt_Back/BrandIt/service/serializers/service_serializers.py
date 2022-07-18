from rest_framework import serializers

from ..models.service_models import Service, EventImage


class ServiceListSerializer(serializers.Serializer):
    svg = serializers.FileField()
    name = serializers.CharField()
    description = serializers.CharField(max_length=250)


class MainServiceSerializer(serializers.Serializer):
    main_title = serializers.CharField()
    title = serializers.CharField()
    services = serializers.SerializerMethodField()

    def get_services(self, main):
        lang = self.context.get("lang")
        services = Service.objects.filter(main_service=main).translate(lang)
        data = ServiceListSerializer(services, many=True).data
        return data


class EventImageListSerializer(serializers.Serializer):
    image = serializers.FileField()


class ServiceDetailSerializer(serializers.Serializer):
    # slug = serializers.SlugField()
    background_image = serializers.FileField()
    name = serializers.CharField()
    description = serializers.CharField(max_length=250)
    events_title = serializers.CharField()
    event_description = serializers.CharField(max_length=250)
    event_image = serializers.FileField()
    event_images = EventImageListSerializer(many=True).data
