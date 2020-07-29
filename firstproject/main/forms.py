from django import forms
from main.models import Advert, Gallery


class AdvertForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        if user:
            pk = user
        else:
            pk = self.user
        super().__init__(*args, **kwargs)
        self.fields['gallery'].queryset = Gallery.objects.filter(user=pk)

    class Meta:
        model = Advert
        fields = ['title', 'text', 'phone', 'email', 'gallery']
        # fields = ['title', 'text', 'phone', 'email']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gallery': forms.Select(attrs={'class': 'form-control'}),
        }
