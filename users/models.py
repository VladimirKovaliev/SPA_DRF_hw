from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')

    city = models.TextField(max_length=100, verbose_name='город', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
