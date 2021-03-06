# Generated by Django 3.0.6 on 2020-05-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст обьявления'),
        ),
    ]
