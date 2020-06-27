from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True, max_length=15, verbose_name='Имя пользователя')
    last_name = models.CharField(blank=True, null=True, max_length=15, verbose_name='Фамилия')
    avatar = models.ImageField(verbose_name='Avatar',
                               default='profiles/avatar.png',
                               upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(blank=True, null=True, max_length=15, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk':self.pk})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, id=instance.id)

    @receiver
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
