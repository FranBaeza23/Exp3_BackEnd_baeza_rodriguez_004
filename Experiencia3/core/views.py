from django.shortcuts import render

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
