from django.contrib import admin
from converter.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'created_at']
    search_fields = ['message',]
