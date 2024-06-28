from django.contrib import admin
from django.contrib.admin import register
from . import models


@register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'slug', 'email', 'is_banned']
    # form =
