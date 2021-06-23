from django.urls import path
from .views import index
from .views import ApiMonedas
from .views import galeria
from .views import QS
from .views import Registro
from .views import Publicacion

urlpatterns = [
    path ('',index,name="index"),
    path ('',ApiMonedas,name="Apimonedas"),
    path ('',galeria,name="galeria"),
    path ('',QS,name="QS"),
    path ('',Registro,name="Registro"),
    path ('',Publicacion,name="Publicacion"),

]


