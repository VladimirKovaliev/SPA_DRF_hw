# Generated by Django 5.0.1 on 2024-02-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('transfer', 'Перевод на счет'), ('cash', 'Наличный')], default='transfer', max_length=8, verbose_name='Способ оплаты'),
        ),
    ]
