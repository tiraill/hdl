from django.contrib import admin
from django.db import models
from django.forms import Textarea
from mptt.admin import MPTTModelAdmin

from .models import BrochureCategory, Brochure


@admin.register(BrochureCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Brochure)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
