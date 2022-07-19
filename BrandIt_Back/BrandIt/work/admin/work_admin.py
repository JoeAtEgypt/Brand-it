from django.contrib import admin

from translations.admin import TranslatableAdmin, TranslationInline

from ..models.work_model import *


class MainWorkAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


class CategoryAdmin(TranslatableAdmin, admin.ModelAdmin):
    model = Category
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [TranslationInline]


class WorkImageInline(admin.TabularInline):
    model = WorkImage


class WorkAdmin(TranslatableAdmin, admin.ModelAdmin):
    model = Work
    list_display = ('title', 'category', 'duration')
    search_fields = ('title', 'category', 'description', 'duration')
    inlines = [TranslationInline, WorkImageInline]


admin.site.register(MainWork, MainWorkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Work, WorkAdmin)