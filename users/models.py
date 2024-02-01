from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}

PAYMENT_CHOICE = {
    ('cash', 'Наличный'),
    ('transfer', 'Перевод на счет')
}


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')

    city = models.TextField(max_length=100, verbose_name='город', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Польхователь - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_payment = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)
    payment_amount = models.SmallIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=8, default='transfer', choices=PAYMENT_CHOICE,
                                      verbose_name='Способ оплаты')

    def __str__(self):
        if self.course:
            return f'Курс {self.course.title} оплачен на сумму {self.payment_amount}'
        return f'Урок {self.lesson.title} оплачен на сумму {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
