# Generated by Django 3.0.6 on 2020-06-05 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200526_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.AlterField(
            model_name='advert',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст обьявления'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=50, verbose_name='заглавие'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Фотография')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Advert', verbose_name='Обьявление')),
            ],
        ),
    ]
