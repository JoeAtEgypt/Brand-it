from django.db import models
from django.core.validators import FileExtensionValidator

from translations.models import Translatable

from Utilities import FileSize, image_extensions, allowed_image_extensions_msg


class ClientPage(Translatable):
    background = models.FileField(upload_to='client_page/', verbose_name="Background_image",
                                  validators=[
                                      FileSize,
                                      FileExtensionValidator(image_extensions, allowed_image_extensions_msg)]
                                  )
    title = models.CharField(max_length=60, verbose_name="Title")

    clients_title = models.CharField(max_length=60, verbose_name="Clients Title")

    client_reviews_title = models.CharField(max_length=60, verbose_name="Clients Reviews Title")

    def __str__(self):
        return self.title

    class TranslatableMeta:
        fields = ['title', 'clients_title', 'clients_reviews_title']

    class Meta:
        verbose_name = "Client Page"
        verbose_name_plural = "Client Page"


class Clients(models.Model):
    svg = models.FileField(upload_to="client_page/clients/", verbose_name="Client_svg",
                           validators=[
                               FileSize,
                               FileExtensionValidator(['svg', 'SVG'], "Allowed Extension: '.svg'")
                           ])
    client_page = models.ForeignKey(ClientPage, on_delete=models.CASCADE,
                                    verbose_name="Client Page", related_name="page_clients")


