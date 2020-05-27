from django.contrib import admin
from .models import Advert
''' Нужно импортировать модель, чтобы она была тут доступна '''

admin.site.register(Advert)
''' Подключаем нашу модель Advert к админке '''
