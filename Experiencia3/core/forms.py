from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cuenta, Publicacion

class publicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['Correo','Nombre','Categoria','Detalles','Cuenta']
        labels = {'Correo' : 'Correo del USER',
                'Nombre' : 'ingrese el nombre del USER',
                'Categoria' : 'ingrese la categoria de la publicacion',
                'Detalles' : 'detalles de la publicacion',
                'Cuenta' : 'ingrese el nombre de la cuenta',}
        wirgets = {
            'Correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo'
                    'id': 'Correo'
                }
            )
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre'
                    'id': 'Nombre'
                }
            )
            'Categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese categoria'
                    'id': 'Categoria'
                }
            )
            'Detalles': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese detalles'
                    'id': 'Detalles'
                }
            )
            'Cuenta': forms.Text.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'Cuenta'
                }
            )
        }