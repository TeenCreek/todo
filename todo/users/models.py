from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


class MyUser(AbstractUser):
    age = models.PositiveSmallIntegerField(
        'Возраст', blank=True, null=True, validators=(MaxValueValidator(150),)
    )
    bio = models.TextField('Биография', blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
