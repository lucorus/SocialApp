from rest_framework import serializers
from . import models
from chat.models import Group


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'slug', 'is_banned']


class GroupSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    class Meta:
        models = Group
        fields = ['id', 'title', 'slug', 'description', 'participants']
