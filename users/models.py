from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from slugify import slugify


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=True, verbose_name='Имя пользователя')
    avatar = models.ImageField(upload_to='images/avatars/', null=True, blank=True, verbose_name='Аватар')
    is_banned = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


@receiver(post_delete)
def delete_related_image(instance, **kwargs):
    """При удалении аватара пользователем, он удаляется из папки"""
    try:
        if instance.avatar:
            storage, path = instance.avatar.storage, instance.avatar.path
            storage.delete(path)
    except:
        pass


@receiver(pre_save, sender=CustomUser)
def delete_related_image_edit(sender, instance, **kwargs):
    """При обновлении аватара пользователя, его старый аватар удаляется из папки"""
    try:
        if instance.id:
            old_instance = sender.objects.filter(pk=instance.id).first()
            if old_instance.avatar != instance.avatar:
                old_instance.avatar.delete(save=False)
    except:
        pass
