from django.shortcuts import render, redirect
from .forms import *
from  django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def splash(request):
    return render(request,"splash.html")

def home(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")


def reservamesa(request):
    return render(request, "reservamesa.html")

def login (request):
    return render(request,"registration/login.html")

def registro (request):

    data = {
        "mensaje":""
    }

    if request.method == "POST":
        nombre=request.POST.get("nombre")
        apellido=request.POST.get("apellido")
        correo=request.POST.get("correo")
        password=request.POST.get("password")
        
        usu = User()
        usu.set_password(password)
        usu.username = nombre
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido
        grupomec = Group.objects.get(name="Cocinero")
    
        try:
            usu.save()
            usu.groups.add(grupomec)
            user = authenticate(username=usu.username, password=password)
            login(request, user)
            
        except:
            data["mensaje"] = "hubo un error"
        
        messages.success(request,"Usuario Creado Exitosamente")
        return redirect(to="registro")

    return render(request,"registration/registro.html")



def registrouser (request):
    data = {
        'form' : agregarform
    }
    return render(request,"mantenedor/admin/agregaruser.html", data)

