from django.contrib.auth import get_user_model
from django.db import models
from slugify import slugify


class Group(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='group_image/', null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(max_length=512, verbose_name='Описание')
    participants = models.ManyToManyField(get_user_model(), related_name='group_member', verbose_name='Участники')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Message(models.Model):
    text = models.TextField(max_length=4096, verbose_name='Текст')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_messages', null=True, verbose_name='Автор')
    recipient = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='received_messages', null=True, verbose_name='Получатель')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages', null=True,  verbose_name='Группа')
    # обратившись к answer_messages мы можем получить данные сообщения, которое было написано в ответ на данное сообщение
    answer_on = models.ForeignKey('Message', on_delete=models.SET_NULL, related_name='answer_messages', null=True, verbose_name='Ответ на')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в')

    def __str__(self):
        return f'Сообщение №{self.pk}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

