from django.contrib import admin
from django.contrib.admin import register
from . import models


@register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    # form =


@register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'recipient', 'group', 'created_at']
    # form
