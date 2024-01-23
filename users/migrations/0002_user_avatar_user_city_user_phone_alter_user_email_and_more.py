# Generated by Django 5.0.1 on 2024-01-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='город'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='фамилия'),
        ),
    ]
