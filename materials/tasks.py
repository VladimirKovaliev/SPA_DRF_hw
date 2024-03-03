from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def update_alert(email, course):
    send_mail(
        subject='Обновление на платформе',
        message=f'Ваш курс "{course}" был обновлен',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
