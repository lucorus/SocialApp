from rest_framework import serializers
from . import models
from chat.models import Group


class CustomUserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj):
        try:
            return obj.avatar.url
        except:
            # пока что будем возвращаем None, если лого нет. в будущем можно будет заменить на аватар по умолчанию
            return None

    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'slug', 'is_banned', 'avatar_url']


class GroupSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    class Meta:
        models = Group
        fields = ['id', 'title', 'slug', 'description', 'participants']
