from django.db import models
from django.urls import reverse

class Advert(models.Model):
    '''
    Модель Advert, для хранения информации рекламного
    обьявления
    '''
    title = models.CharField(verbose_name='заглавие', max_length=50)
    text = models.TextField(verbose_name='Текст обьявления', null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=30, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    def get_detailUrl(self):
        return reverse('adv_detail', kwargs={'pk':self.pk})

    def get_absolute_url(self):
        return reverse('adv_list')

    def get_UpdateUrl(self):
        return reverse('adv_update', kwargs={'pk':self.pk})

    def get_DeleteUrl(self):
        return reverse('adv_delete', kwargs={'pk':self.pk})

