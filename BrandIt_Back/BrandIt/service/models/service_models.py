from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from translations.models import Translatable

from Utilities.Global_Utilities import FileSize, image_extensions, allowed_image_extensions_msg


class MainService(Translatable):
    main_title = models.CharField(max_length=60, verbose_name="Main Title")
    title = models.CharField(max_length=60, verbose_name="Title")
    background_image = models.FileField(upload_to="MainService/", verbose_name="Image", default='/test',
                             validators=[
                                 FileSize,
                                 FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                             ])

    def __str__(self):
        return self.main_title

    class TranslatableMeta:
        fields = ['main_title', 'title']

    class Meta:
        verbose_name = "Main Service"
        verbose_name_plural = "Main Service"


class Service(Translatable):
    slug = models.SlugField(max_length=60, default="")
    svg = models.FileField(upload_to="MainService/services/",
                           validators=[
                               FileSize,
                               FileExtensionValidator(['svg'], "Allowed Format is 'svg'")])
    name = models.CharField(max_length=60, verbose_name="Service Name")
    description = models.TextField(max_length=250, verbose_name="Service Description")
    background_image = models.FileField(upload_to="MainService/services/",
                                        verbose_name="Service Background",
                                        validators=[
                                            FileSize,
                                            FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                                        ])
    events_title = models.CharField(max_length=60, verbose_name="Event Title")
    event_description = models.TextField(max_length=250, verbose_name="Event Description")
    event_image = models.FileField(upload_to="MainService/services/events/",
                                        verbose_name="Event Image",
                                        validators=[
                                            FileSize,
                                            FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                                        ])

    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE, verbose_name="Main Service")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class TranslatableMeta:
        fields = ['name', 'description', 'events_title', 'event_description']

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class EventImage(models.Model):
    image = models.FileField(upload_to="MainService/services/events/", verbose_name="Event Image",
                             validators=[
                                 FileSize,
                                 FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                             ])
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Service")

    class Meta:
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"

