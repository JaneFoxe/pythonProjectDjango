from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULL_PARAM


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to="user/", verbose_name="Аватар", **NULL_PARAM)
    phone = models.CharField(max_length=30, unique=True, verbose_name='Номер телефона', **NULL_PARAM)
    country = models.CharField(max_length=100, verbose_name="Страна")

    token = models.CharField(max_length=100, verbose_name='Token', **NULL_PARAM)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
