from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import FeedbackHistory, EmailReceivers


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'creation_date')
    ordering = ('-creation_date',)
    list_filter = ('creation_date',)
    search_fields = ('email',)
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
    }



@admin.register(EmailReceivers)
class EmailReceiversAdmin(admin.ModelAdmin):
    list_display = ('email',)
