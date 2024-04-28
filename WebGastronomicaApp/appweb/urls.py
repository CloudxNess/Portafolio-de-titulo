from django.urls import path
from .views import *


urlpatterns = [
     path('',home , name="index"),
     path('splash',splash,name="splash"),
     path('home',home , name="index"),
     path('menu',menu , name="menu"),
     path('reservamesa',reservamesa , name="reservamesa"),
     path('registrouser',registrouser,name='registrouser'),
     path('registro',registro,name='registro'),
     path('registro_cli',registro_cli,name='registro_cli'),
     path('mesas',mesas,name='mesas'),
     
     
]
