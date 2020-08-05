from django.http import HttpResponseRedirect
from django.views import generic
from .forms import AdvertForm
from .models import Advert, Photo, Gallery
from django.contrib.auth.mixins import LoginRequiredMixin
from main.permissions import UserIsOwnerOrAdminMixin


class AdvertListView(generic.ListView):
    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    context_object_name = 'adv'
    paginate_by = 4


class AdvertDetailView(LoginRequiredMixin, generic.DetailView):
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
        context['permit'] = UserIsOwnerOrAdminMixin.has_permission(self)
        return context


class AdvertCreate(LoginRequiredMixin, generic.CreateView):
    ''' Создание нового обьявления '''
    # form_class = AdvertForm
    template_name = 'main/advertcreate.html'

    def get_form(self, form_class=AdvertForm):
        form = AdvertForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        bindform = AdvertForm(request.user, request.POST)
        post = bindform.save(commit=False)
        post.user = request.user
        post.save()
        return HttpResponseRedirect('/')


class AdvertUpdate(UserIsOwnerOrAdminMixin, generic.UpdateView):
    ''' Редактирование обьявления '''
    model = Advert
    form_class = AdvertForm
    template_name = 'main/advertupdate.html'
    context_object_name = 'adv'
    form_class.user = 1 #todo не забыть исправить заглаушки


class AdvertDelete(UserIsOwnerOrAdminMixin, generic.DeleteView):
    ''' Удаление обьявления '''
    model = Advert
    context_object_name = 'adv'
    template_name = 'main/advert_confirm_delete.html'
    success_url = '/'


