from django.contrib import admin
from .models import Advert, Photo
''' Нужно импортировать модель, чтобы она была тут доступна '''

admin.site.register(Advert)
''' Подключаем нашу модель Advert к админке '''

@admin.register(Photo)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('advert',)
''' Подключаем нашу модель Photo к админке '''

