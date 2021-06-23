from django import forms
from django.forms import ModelForm, widgets
from .models import Publicacion

class publicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['Correo','Nombre','Categoria','Detalles','cuenta']


        labels ={'Correo' : 'Correo del USER',
                'Nombre' : 'ingrese el nombre del USER',
                'Categoria' : 'ingrese la categoria de la publicacion',
                'Detalles' : 'detalles de la publicacion',
                'cuenta' : 'ingrese el nombre de la cuenta',}
        widgets = {
            'Correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Correo',
                    'name': 'Correo',
                    'placeholder': 'Ingrese Correo'
                }
            ),
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Nombre',
                    'placeholder': 'Ingrese Nombre'
                }
            ),
            'Categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese categoria',
                    'id': 'Categoria'
                }
            ),
            'Detalles': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese detalles',
                    'id': 'Detalles'
                }
            ),
            'cuenta': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'cuenta'
                }
            )
        }