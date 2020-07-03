from django.contrib import admin

from .models import Topic, Article


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'get_topic', 'date')
    list_filter = ('topic__title', 'date')
    search_fields = ('title', 'topic__title')

    def get_topic(self, instance):
        if instance and instance.topic:
            return instance.topic.title
        else:
            return f"Тема не указана, либо была удалена"
    get_topic.short_description = "Категория статьи"
