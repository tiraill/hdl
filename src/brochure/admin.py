from django.contrib import admin

from .models import BrochureCategory, Brochure


@admin.register(BrochureCategory)
class BrochureCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = ('title',)
