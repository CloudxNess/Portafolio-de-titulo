from django.urls import path
from .views import *


urlpatterns = [
     path('',home , name="index"),
     path('menu',menu , name="menu"),
     path('reservamesa',reservamesa , name="reservamesa"),
     
]
