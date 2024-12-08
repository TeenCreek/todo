from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=200, db_index=True)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)
    is_completed = models.BooleanField('Заверешена', default=False)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='tasks',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('id', 'created_at')
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
