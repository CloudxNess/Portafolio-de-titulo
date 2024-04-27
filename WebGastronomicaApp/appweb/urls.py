from django.urls import path
from .views import *


urlpatterns = [
     path('',home , name="index"),
     path('splash',splash,name="splash"),
     path('home',home , name="index"),
     path('menu',menu , name="menu"),
     path('reservamesa',reservamesa , name="reservamesa"),
     path('login',login,name='login'),
     path('registrouser',registrouser,name='registrouser'),
     
     
]
