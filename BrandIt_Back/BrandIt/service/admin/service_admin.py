from django.contrib import admin

from translations.admin import TranslatableAdmin, TranslationInline

from ..models.service_models import *


class EventImageInline(admin.TabularInline):
    model = EventImage


class MainServiceAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


class ServiceAdmin(TranslatableAdmin, admin.ModelAdmin):
    model = Service
    search_fields = ('name', 'description')
    inlines = [TranslationInline, EventImageInline]


admin.site.register(MainService, MainServiceAdmin)
admin.site.register(Service, ServiceAdmin)