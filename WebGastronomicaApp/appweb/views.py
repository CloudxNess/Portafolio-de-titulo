from django.shortcuts import render, redirect
from .forms import *
from  django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import platosform
from .models import *
from openpyxl import Workbook
from django.http.response import HttpResponse

# Create your views here.



def splash(request):
    return render(request,"splash.html")

def home(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")


def reservamesa(request):
    
    data= {"formremesa" : reservamesaform }

    if request.method=="POST":
            formulario = reservamesaform(data=request.POST)

            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Reserva Exitosa"
            else:
                data["mensaje"] = "Error"
                data["formremesa"] = formulario


    return render(request, "reservamesa.html", data)


def login (request):
    return render(request,"registration/login.html")


def agregarplato(request):

    data = {"form_agregarplato" : platosform}


    if request.method=="POST":
            formulario = platosform(data=request.POST,files=request.FILES)

            if formulario.is_valid():
                formulario.save()
            else:
                data["mensaje"] = "Error"
                data["form_agregarplato"] = formulario


    return render(request, "mantenedor/garzon/agregarplato.html", data )


@login_required(login_url="/accounts/login")
@permission_required (['auth.add_user'], login_url="/")
def registro (request):

    data = {
        "mensaje":""
    }

    if request.method == "POST":
        nombre=request.POST.get("nombre")
        usuario=request.POST.get("usuario")
        apellido=request.POST.get("apellido")
        correo=request.POST.get("correo")
        password=request.POST.get("password")
        grupo1=request.POST.get("grupo")
        
        usu = User()
        usu.set_password(password)
        usu.username = usuario
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido
        grupo = Group.objects.get(name=grupo1)
        print (grupo)
    
        try:
            usu.save()
            usu.groups.add(grupo)
            user = authenticate(username=usu.username, password=password)
            login(request, user)
            
        except:
            data["mensaje"] = "hubo un error"
        
        messages.success(request,"Usuario Creado Exitosamente")
        return redirect(to="index")

    return render(request,"registration/registro.html")



def registro_cli (request):

    data = {
        "mensaje":""
    }

    if request.method == "POST":
        nombre=request.POST.get("nombre")
        usuario=request.POST.get("usuario")
        apellido=request.POST.get("apellido")
        correo=request.POST.get("correo")
        password=request.POST.get("password")
        
        usu = User()
        usu.set_password(password)
        usu.username = usuario
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido
        grupo = Group.objects.get(name="Cliente")
    
        try:
            usu.save()
            usu.groups.add(grupo)
            user = authenticate(username=usu.username, password=password)
            login(request, user)
            
        except:
            data["mensaje"] = "hubo un error"
        
        messages.success(request,"Usuario Creado Exitosamente")
        return redirect(to="home")

    return render(request,"registration/registro_cli.html")


def registrouser (request):
    data = {
        'form' : agregarform
    }
    return render(request,"mantenedor/admin/agregaruser.html", data)



def mesas (request):
     
    mesastb =  Mesa.objects.all()

    data = {
        "Mesas": mesastb,
          }


    return render(request, "mesas.html", data)


def listaringredientes (request):
    peticiones = Ingredientes.objects.all()
    ingredientes = Bodega.objects.all()
    data = {
        'mis_ingredientes' : ingredientes ,
        'mis_peticiones' : peticiones
    }


    return render(request,"mantenedor/admin/listaringredientes.html", data )

## no va a funcionar porque se tienen que colocar los ID, se tienen que editar los models.py para  
## intentar hacer la doble insersion sin ID desde esta oage, insertar en la de ingredientes y la de 
## la Bodega :3   
def agregaringredientes(request):

    data = {"form_agregaringrediente" : agregaringreform}


    if request.method=="POST":
            formulario = agregaringreform(data=request.POST)

            if formulario.is_valid():
                ingrediente = formulario.save()
                data["mensaje"] = "Ingrediente agregado correctamente"
                bodega = Bodega.objects.create(ID_Ingrediente=ingrediente, Cantidad=0)

            else:
                data["mensaje"] = "Error"
                data["form_agregaringrediente"] = formulario


    return render(request, "mantenedor/admin/agregaringrediente.html", data )




def listarusuarios(request):

    Usuarios_local = User.objects.all()

    data = {
        "Usuarios" : Usuarios_local
    }


    return render(request,"mantenedor/admin/listarusuarios.html",data)   




def DescargarReporteExcel (TemplateView):
    def get(self,request,*args,**kwargs):
        ingredientes = Bodega.objects.all()
        wb = Workbook()
        ws = wb.active
        ws ['B1'] = 'Reporte De Ingredientes'

        ws.merge_cells('B1:E1')
        ws['B3'] = 'Ingredientes'
        ws['C3'] = 'Cantidad'

        cont= 2

        for ingrediente in ingredientes :
            ws.cell(row = cont, column = 2).value = ingrediente.ingredientes
            ws.cell(row = cont, column = 3).value = ingrediente.cantidad
            cont+=1

        nombre_archivo = "ReporteIngredienteBodega.xlsx"
        response = HttpResponse(content_type ="application/ms-excel")
        content = "attachment; filename {0}".format(nombre_archivo)
        response['Content-Disposition'] = content
        wb.save(response)
        return response