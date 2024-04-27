from django.shortcuts import render

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


def registrouser (request):
    return render(request,"registration/registro.html")