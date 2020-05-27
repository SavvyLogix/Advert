from django.shortcuts import render
from django.views import generic
from .models import Advert

class AdvertListView(generic.ListView):
    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    context_object_name = 'adv'

