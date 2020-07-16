# Generated by Django 3.0.6 on 2020-06-22 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Фамилия')),
                ('avatar', models.ImageField(blank=True, default='profiles/avatar.png', null=True, upload_to='profiles/', verbose_name='Avatar')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
