from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from  django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import platosform
from .models import *
from django.utils import timezone
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from itertools import groupby
from django.http import JsonResponse



# Create your views here.



def splash(request):
    return render(request,"splash.html")

def home(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")


def reservamesa(request):
    fecha_hoy = timezone.now().date()  
    
    data= {"formremesa" : reservamesaForm }

    if request.method=="POST":
            formulario = reservamesaForm(data=request.POST)
            
            if formulario.is_valid():
                fecha_reserva = formulario.cleaned_data.get('fecha')
                
                if fecha_reserva > fecha_hoy:
                    formulario.save()
                    messages.success(request,"Reserva Enviada Exitosamente, Espere Confirmación")
                else:
                    messages.warning(request,"Debe Reservar con un dia de anticipación")
                    data["formremesa"] = formulario
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


    return render(request, "mantenedor/cocinero/agregarplato.html", data )


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
    peticiones = Sol_Ingredientes.objects.all()
    ingredientes = Bodega.objects.all()
    data = {
        'mis_ingredientes' : ingredientes ,
        'mis_peticiones' : peticiones
    }


    return render(request,"mantenedor/admin/listaringredientes.html", data )

  
def agregaringredientes(request):

    
    data = {
        "mensaje":""
    }

    if request.method == "POST":
        nombre=request.POST.get("nombre")
        costo=request.POST.get("costo")
        unidad=request.POST.get("unidad")

        ingre = Ingredientes()
        ingre.nombre=nombre
        ingre.Costo=costo
        ingre.unidad_medida=unidad
        print(ingre.nombre)
        print(ingre.Costo)
        print(ingre.unidad_medida)
        try:
            ingre.save()
            data["mensaje"] = "Ingrediente agregado correctamente"
            bodega = Bodega.objects.create(ID_Ingrediente=ingre, Cantidad=0)
            print("de pana choro")
            
        except:
            data["mensaje"] = "hubo un error"
        
        messages.success(request,"Ingrediente agregado correctamente")
        


    return render(request, "mantenedor/admin/agregaringrediente.html", data )



def sol_ingredientes(request):

    data = {"form_solicitaringrediente" : Sol_Ingredientesform}
    bodegas = Bodega.objects.all()

    

    if request.method=="POST":
            formulario = Sol_Ingredientesform(data=request.POST)

            if formulario.is_valid():
                formulario.save()

            else:
                data["mensaje"] = "Error"
                data["form_solicitaringrediente"] = formulario


    return render(request, "mantenedor/cocinero/Solicitudingredientes.html", {'data': data, 'bodegas': bodegas} )


def listarusuarios(request):

    Usuarios_local = User.objects.all()

    data = {
        "Usuarios" : Usuarios_local
    }


    return render(request,"mantenedor/admin/listarusuarios.html",data)   



def menuadmin(request):

    Menu_local = Platos.objects.all()

    data = {
        "Menu" : Menu_local
    }

    return render(request,"mantenedor/admin/menuadmin.html", data)



def modificarmenu(request, NombreBuscado):

    platom = get_object_or_404(Platos, Nombre=NombreBuscado)

    data = {

        'form': platosform(instance=platom)
    } 

    if request.method == "POST":
        formulario = platosform(data=request.POST, instance=platom, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="menuadmin")
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request,"mantenedor/admin/modificarmenu.html", data)




def activaplato(request, NombreBuscado):

    platom = get_object_or_404(Platos, Nombre=NombreBuscado)
    platom.Disponibilidad=(1) 
    platom.save()    
    return redirect(to="menuadmin" )



def desactivaplato(request, NombreBuscado):

    platom = get_object_or_404(Platos, Nombre=NombreBuscado)
    platom.Disponibilidad=(0) 
    platom.save()    
    return redirect(to="menuadmin" )




def DescargarReporteExcel(request):
    ingrediente = Bodega.objects.all()

    wb = Workbook()
    ws = wb.active

    ws.append(['ID','Ingrediente','Cantidad'])

    

    header_font = Font(bold=True)
    header_fill = PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')

    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill

    for x in ingrediente:
        ws.append([x.ID_Ing_Bod,x.ID_Ingrediente.nombre, x.Cantidad, ])


    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max(max_length, 15) + 2
        ws.column_dimensions[column_letter].width = adjusted_width

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Inventario.xlsx'
    wb.save(response)
    
    return response
    for x in ingrediente :
        ws.append([x.ID_Ing_Bod, x.Cantidad,x.ID_Ingrediente.nombre])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Reporte_Inventario.xlsx'
        wb.save(response)
        return response
    


def menu(request):

    Menu_platos = Platos.objects.all().filter(Disponibilidad=True)

    data = {
        "MenuP" : Menu_platos
    }
    



    return render(request,"menu.html", data)



    
   
def menu(request):
    
    Menu_Platos = Platos.objects.filter(Disponibilidad=True).order_by('Region')

    platos_por_region = {}
    for region, MenuP in groupby(Menu_Platos, key=lambda x: x.Region):
        platos_por_region[region] = list(MenuP)

    data = {
        "platos_por_region": platos_por_region
    }

    return render(request, "menu.html", data)    
    

def modificarIngrediente(request, NombreBuscado):

    ModificarI = get_object_or_404(Bodega, Nombre=NombreBuscado)

    data = {

        'form': BodegaForm(instance=ModificarI)
    } 

    if request.method == "POST":
        formulario = BodegaForm(data=request.POST, instance=ModificarI, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listaringredientes")
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request,"mantenedor/admin/listaringredientes.html", data)

 

def actualizar_ingrediente2(request, ingredientebusca):

    ingre = get_object_or_404(Bodega, ID_Ing_Bod=ingredientebusca)
    cantidadAgregar = request.POST.get("cantidad")
    ingre.Cantidad = int(cantidadAgregar) + ingre.Cantidad
    ingre.save()    
    return redirect(to="listaringredientes" )


def descuenta_ingrediente(request, IdSolicitud):

    Soli = get_object_or_404(Sol_Ingredientes, ID_Solicitud_Ingrediente=IdSolicitud)
    cantidadRestar = Soli.Cantidad
    ingre = get_object_or_404(Bodega, ID_Ing_Bod=Soli.Ingrediente.ID_Ingrediente)
    ingre.Cantidad = ingre.Cantidad - cantidadRestar
    ingre.save()    
    Soli.Realizado=(1)
    Soli.save()
    return redirect(to="listaringredientes" )




def listaragendamiento(request):

    Agendamientos = Reserva_Mesa.objects.all()
    fecha_hoy = timezone.now().date()  

    data = {
        "Agendamientos" : Agendamientos,
         'fecha_hoy': fecha_hoy,
        
    }

    return render(request,"mantenedor/admin/listar_agendamiento.html", data)



def mesasparapedido (request):

    mesaspedido =  Mesa.objects.all()

    data = {
        "Mesas": mesaspedido,
          }


    return render(request, "mantenedor/garzon/mesasparapedido.html", data)