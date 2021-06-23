from django.shortcuts import render, redirect
from .models import Publicacion
from .forms import publicacionForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def QS(request):
    return render(request, 'QS.html')

def galeria(request):
    return render(request, 'galeria.html')

def ApiMonedas(request):
    return render(request, 'ApiMonedas.html')

def Publicacion(request):
    return render(request, 'Publicacion.html')

def Registro(request):
    return render(request, 'Registro.html')

def form_publicacion(request):
    if request.method == 'POST':
        publicacion_form = publicacionForm(request.POST)
        if publicacion_form.is_valid():
            publicacion_form.save()
            return redirect('index')
    else: 
        publicacion_form = publicacionForm()
    return render(request, 'core/form_publicacion.html', {'publicacion_form': publicacion_form})
def Ver(request):
     Publicacion = Publicacion.objects.all()

    return render(request, 'core/ver.html', {'publicacion': Publicacion})