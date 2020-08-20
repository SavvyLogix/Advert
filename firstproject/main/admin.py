from django.contrib import admin
from .models import Advert, Photo, Gallery
''' Нужно импортировать модели, чтобы они были тут доступны '''

admin.site.register(Advert)
''' Подключаем нашу модель Advert к админке '''

@admin.register(Photo)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('gallery',)
''' Подключаем нашу модель Photo к админке '''

admin.site.register(Gallery)
''' Подключаем нашу модель Gallery к админке '''
