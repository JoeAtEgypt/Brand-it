from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from translations.models import Translatable

from Utilities.Global_Utilities import FileSize, image_extensions, allowed_image_extensions_msg


class MainWork(Translatable):
    main_title = models.CharField(max_length=60, verbose_name="Main Title")
    background_image = models.FileField(upload_to="MainWork/", verbose_name="Background Image",
                                        validators=[
                                            FileSize,
                                            FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                                        ])

    def __str__(self):
        return self.main_title

    class TranslatableMeta:
        fields = ["main_title", ]

    class Meta:
        verbose_name = "Main Work"
        verbose_name_plural = "Main Work"


class Category(Translatable):
    slug = models.SlugField(default="")
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class TranslatableMeta:
        fields = ["title", ]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Work(Translatable):
    slug = models.SlugField(default="")
    # list
    title = models.CharField(max_length=60, verbose_name="Title")
    background_image = models.FileField(upload_to="MainWork/work/", verbose_name="Background Image",
                                        validators=[
                                            FileSize,
                                            FileExtensionValidator(image_extensions, allowed_image_extensions_msg)
                                        ])
    # Detail
    duration = models.CharField(max_length=60, verbose_name="Duration")
    description = models.TextField(max_length=500, verbose_name="Description")


    # related models
    main_work = models.ForeignKey(MainWork, on_delete=models.CASCADE, related_name="main_works",
                                  verbose_name="Main Work")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_works",
                                 verbose_name = "Category")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class TranslatableMeta:
        fields = ["title", "duration", "description"]

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"


class WorkImage(models.Model):
    image = models.FileField(upload_to="MainWork/work/", verbose_name="Image")

    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="work_images", verbose_name="Work")

    class Meta:
        verbose_name = "Work Image"
        verbose_name_plural = "Work Images"

