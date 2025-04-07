from django import forms
from .models import Crud
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
class CrudForm(forms.ModelForm):
	class Meta:
		model= Crud
		fields = ['titre','contenu','date_publicatiôn','auteur','image']
        
		widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de l\'article'
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Contenu de l\'article'
            }),
            'date_publication': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'auteur': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
labels = {
            'titre': 'Titre',
            'contenu': 'Contenu',
            'date_publication': 'Date de publication',
            'auteur': 'Auteur',
            'image': 'Image associée'
        }
help_texts = {
            'image': 'Format accepté: JPG, PNG, GIF (max. 2MB)'
        }

def clean_titre(self):
        titre = self.cleaned_data.get('titre')
       
        return titre

def clean_date_publication(self):
        date_pub = self.cleaned_data.get('date_publication')
        
        return date_pub
        	