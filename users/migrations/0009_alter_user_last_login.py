# Generated by Django 4.2.10 on 2024-03-03 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_username_alter_payment_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Последняя авторизация'),
        ),
    ]
