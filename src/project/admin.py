from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import ProjectCategory, Project, ProjectImage


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'cols': 80, 'rows': 10})},
    }


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('uid', 'get_project')
    list_filter = ('project__title',)
    search_fields = ('project__title',)
    autocomplete_fields = ('project',)
    exclude = ('uid',)

    def get_project(self, instance):
        if instance and instance.project:
            return instance.project.title
        else:
            return f"Проект не указан, либо был удален"
    get_project.short_description = "Проект, к которому прикреплено фото"
