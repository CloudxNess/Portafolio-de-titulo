from django.urls import path
from .views import *


urlpatterns = [
     path('',splash , name="splash"),
     path('splash',splash,name="splash"),
     path('home',home , name="index"),
     path('menu',menu , name="menu"),
     path('reservamesa',reservamesa , name="reservamesa"),
     path('registrouser',registrouser,name='registrouser'),
     path('registro',registro,name='registro'),
     path('registro_cli',registro_cli,name='registro_cli'),
     path('mesas',mesas,name='mesas'),
     path('agregarplato', agregarplato, name='agregarplato'),
     path('listaringredientes', listaringredientes, name='listaringredientes' ),
     path('agregaringredientes', agregaringredientes, name='agregaringrediente' ),
     path('listarusuarios',listarusuarios,name='listarusuarios'),
     path('sol_ingredientes',sol_ingredientes,name='sol_ingredientes'),
     path('DescargarReporteExcel', DescargarReporteExcel, name='DescargarReporteExcel'),
     path('menuadmin', menuadmin , name='menuadmin'),
     path('modificarmenu/<NombreBuscado>', modificarmenu, name='modificarmenu'), 
     path('activaplato/<NombreBuscado>', activaplato, name='activaplato'), 
     path('desactivaplato/<NombreBuscado>', desactivaplato, name='desactivaplato'),
     path('menu', menu, name='menu'),
     path('actualizar_ingrediente/', actualizar_ingrediente, name='actualizar_ingrediente'),
]
