from django.views import generic
from .forms import AdvertForm
from .models import Advert, Photo, Gallery


class AdvertListView(generic.ListView):
    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    context_object_name = 'adv'
    paginate_by = 4

class AdvertDetailView(generic.DetailView):
    ''' Детализированная форма обьявления '''
    model = Advert
    template_name = 'main/advertdetail.html'
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        qsetAdvert = Advert.objects.values('gallery_id').filter(pk=pk)
        gallery = qsetAdvert.get().get('gallery_id')
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(gallery=gallery)
        return context

class AdvertCreate(generic.CreateView):
    ''' Создание нового обьявления '''
    form_class = AdvertForm
    template_name = 'main/advertcreate.html'

class AdvertUpdate(generic.UpdateView):
    ''' Редактирование обьявления '''
    model = Advert
    form_class = AdvertForm
    template_name = 'main/advertupdate.html'
    context_object_name = 'adv'

class AdvertDelete(generic.DeleteView):
    ''' Удаление обьявления '''
    model = Advert
    context_object_name = 'adv'
    template_name = 'main/advert_confirm_delete.html'
    success_url = '/'

class GalleryCreateView(generic.CreateView):
    ''' Добавление галереи '''
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'




