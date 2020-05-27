from django.urls import path
from django.http import HttpResponse
from .views import AdvertListView

def testView(request):
    return HttpResponse('<div align="center"><h1 style="color:blue">Это тестовая страница!</h1></div>')

urlpatterns=[
    path('', AdvertListView.as_view(), name='adv_list')

]