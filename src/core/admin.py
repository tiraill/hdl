from django.contrib import admin

from .models import FeedbackHistory, EmailReceivers


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(EmailReceivers)
class EmailReceiversAdmin(admin.ModelAdmin):
    list_display = ('email',)
