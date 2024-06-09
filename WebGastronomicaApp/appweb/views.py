from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import *
from  django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import platosform
from .models import *
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from itertools import groupby
from django.http import JsonResponse
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.staticfiles.storage import staticfiles_storage



# Create your views here.



def splash(request):
    return render(request,"splash.html")

def home(request):
    # 6 platos más vendidos
    top_platos = Descripción_Pedidos_Historico.objects.values('ID_Platos').annotate(total=Count('ID_Platos')).order_by('-total')[:6]

    # información adicional de cada plato
    platos_data = []
    for item in top_platos:
        plato = Platos.objects.get(ID_Plato=item['ID_Platos'])
        platos_data.append({
            'nombre': plato.Nombre,
            'imagen': plato.imagen.url if plato.imagen else None,
            'costo': plato.Costo,
            
        })

    context = {
        'platos_data': platos_data,
    }
    return render(request, 'index.html', context)

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
        usu.is_staff=(1)
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
            bodega = Bodega.objects.create(ID_Ingrediente=ingre, Cantidad=0)
            messages.success(request,"Ingrediente agregado correctamente")
            
           
        except:
            data["mensaje"] = "hubo un error"
        
        
        

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


def estadoplatolisto(request, Id_pedido):

    platom = get_object_or_404(Descripción_Pedidos, ID=Id_pedido)
    platom.Listo=(1) 
    platom.save()    
    return redirect(to="estadopedidoc" )




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
    if ingre.Cantidad >= 0:
        ingre.save()    
        Soli.Realizado=(1)
        Soli.save()
        messages.success(request,"Solicitud aprobada")
    else:
            messages.error(request,"Sin Stock Suficiente, Considere Comprar Mas Ingredientes")
    return redirect(to="listaringredientes" )




def listaragendamiento(request):

    Agendamientos = Reserva_Mesa.objects.all()
    fecha_hoy = timezone.localtime(timezone.now()).date()  

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


def ingresopedidomesa (request,Mesa):

    Menu_local = Platos.objects.all()
    Pedidoss = Descripción_Pedidos.objects.all().filter(ID_Pedido=Mesa)
    try:
        pedido = Pedidos.objects.get(ID_Pedido=Mesa)
    except Pedidos.DoesNotExist:
        pedido = None

    total_cantidad = Pedidoss.aggregate(Sum('Costo'))['Costo__sum']
    if total_cantidad is None:
        total_cantidad = 0

    data = {
        "Menu" : Menu_local ,
        "mesa":Mesa,
        "Pedido":Pedidoss,
        "Pedi":pedido,
        "total_cantidad": total_cantidad,
        
    }
    return render (request,"mantenedor/garzon/ingresopedidomesa.html",data)


def inicia_pedido (request, Mesaa):
    mesita = get_object_or_404(Mesa, ID_Mesa=Mesaa)
    mesita.Estado_Ocupado=(1)
    mesita.save()
    pedido = Pedidos.objects.create(ID_Pedido=Mesaa,Correo_Sol="ftecnofood@gmail.com",ID_Mesa=mesita,Estado="Sin Solicitud")

    return redirect("ingresopedidomesa",Mesa=Mesaa )


def termina_pedido_nulo (request, Mesaa):
    
    pedido = get_object_or_404(Pedidos, ID_Pedido=Mesaa)
    pedido.delete()
    mesita = get_object_or_404(Mesa, ID_Mesa=Mesaa)
    mesita.Estado_Ocupado=(0)
    mesita.save()
    return redirect("ingresopedidomesa",Mesa=Mesaa )

def termina_pedido (request, Mesaa):
    pedido = get_object_or_404(Pedidos, ID_Pedido=Mesaa)
    valor=0
    mesita = get_object_or_404(Mesa, ID_Mesa=Mesaa)
    mesita.Estado_Ocupado=(0)
    mesita.save()
    pedidos = get_list_or_404(Descripción_Pedidos, ID_Pedido=Mesaa)
    mes = get_object_or_404(Mesa, ID_Mesa=Mesaa)
    for X in pedidos:
        valor = X.Costo + valor
    boleta=Boletas.objects.create(ID_Mesa=mes,Costo_Total=valor)
    bol=boleta.ID_Boleta
    for Y in pedidos:
        pedi_histo=Descripción_Pedidos_Historico.objects.create(ID_Boleta=boleta,ID_Platos=Y.ID_Platos,Costo=Y.Costo)
    pedido.delete()
    return redirect("boleta",Boleta=bol )

def boleta (request, Boleta):

    bol = get_object_or_404(Boletas, ID_Boleta=Boleta)
    hist = get_list_or_404(Descripción_Pedidos_Historico, ID_Boleta=Boleta)
    data = {
        'mi_boleta' : bol ,
        'mis_peticiones' : hist
    }


    return render (request,"mantenedor/garzon/boleta.html",data)


def eliminapedidolista (request, Mesaa, pedido):
    
    pedidoelimina = get_object_or_404(Descripción_Pedidos, ID=pedido)
    pedidoelimina.delete()
    return redirect("ingresopedidomesa",Mesa=Mesaa )


def enviapedidococina (request, Mesaa):
    
    pedidos = get_list_or_404(Descripción_Pedidos, ID_Pedido=Mesaa)
    for pedido in pedidos:
        pedido.Sol_cocina = (1)
        pedido.save()
    return redirect("ingresopedidomesa",Mesa=Mesaa )


def pedidolista (request, Mesaa, Plato):
    try:
        pedido = Pedidos.objects.get(ID_Pedido=Mesaa)
    except Pedidos.DoesNotExist:
        messages.error(request,"No se a iniciado Servicio")
        return redirect("ingresopedidomesa",Mesa=Mesaa )

    platom = get_object_or_404(Platos, ID_Plato=Plato)
    pedido= get_object_or_404(Pedidos, ID_Pedido=Mesaa)
    solicitud = Descripción_Pedidos.objects.create(ID_Pedido=pedido,ID_Platos=platom,Costo=platom.Costo)

    return redirect("ingresopedidomesa",Mesa=Mesaa )





def actualizar_agendamiento(request, reserva):     
    Reserva = get_object_or_404(Reserva_Mesa, ID_reserva=reserva)
    mesa = request.POST.get("mesa")
    anterior = get_object_or_404(Mesa, ID_Mesa=Reserva.ID_Mesa.ID_Mesa)
    nueva = get_object_or_404(Mesa, ID_Mesa=mesa)

    Reserva.ID_Mesa = nueva

    if nueva.Estado_Reservado == 0:
        anterior.Estado_Reservado = 0
        Reserva.save()
        nueva.Estado_Reservado=(1)
        nueva.save()
        anterior.save()
        messages.success(request, "Agendamiento Realizado con Exito...Enviando Correo de Confirmación al Cliente. ")
        
        imagen_url = staticfiles_storage.url("static/image/TecnoFood.png")
        mensaje_correo = f"""
        Agendamiento Realizado Con Exito 

        Detalles de la reserva:
        Nombre: {Reserva.nombre}
        Correo: {Reserva.correo}
        Fecha: {Reserva.fecha}
        Hora: {Reserva.hora}
        Cantidad de comensales: {Reserva.cantidad_comensales}
        Mesa: {nueva.Nombre_Mesa}
        
        <img src="{imagen_url}" alt="TecnoFood">


        Gracias Por Preferirnos , Equipo TecnoFood

       'ftecnofood@gmail.com'
        """

        send_mail(
            'Agendamiento Realizado' ,
             mensaje_correo,
            'ftecnofood@gmail.com',
            [Reserva.correo], 
            fail_silently=False,
        )
    elif nueva.ID_Mesa == 0:
        anterior.Estado_Reservado=(0)
        Reserva.save()
        anterior.save()
    else:
        messages.error(request, "Mesa ya reservada")

    return redirect(to="listaragendamiento") 


def pedidosingresadoscocina(request):

    
    mesaspedido =  Mesa.objects.all()
    pedidos =  Descripción_Pedidos.objects.all()
    reserv = Reserva_Mesa.objects.all()
    fecha_hoy = timezone.localtime(timezone.now()).date()

    data = {
        "Mesas": mesaspedido,
        "pedidos": pedidos,
        "reservas": reserv,
        "fecha_hoy":fecha_hoy
          }


    return render(request,"mantenedor/garzon/pedidosingresadoscocina.html",data)




def estadopedidog (request):
     
    pedidos =  Descripción_Pedidos.objects.all()

    data = {
        "pedidos": pedidos,
          }


    return render(request, "mantenedor/garzon/estadopedidog.html", data)



def estadopedidoc (request):
     
    pedidos =  Descripción_Pedidos.objects.all()

    data = {
        "pedidos": pedidos,
          }

    return render(request, "mantenedor/cocinero/estadopedidoc.html", data)



def pago (request, Boleta) :

    bol = get_object_or_404(Boletas, ID_Boleta=Boleta)
    data = {
        "mi_boleta": bol
          }

    return render(request,"mantenedor/garzon/pago.html",data)


def carrito(request):
    context = {}

    return render(request, 'Carrito/carrito.html', context)



def funciones (request, Id_user) :
 
    user = User.objects.get(id=Id_user) 
    groups = user.groups.all()  
    grupos = groups.first().id  

    data = {
        "usuario": Id_user,
        "grupo": grupos
    }
        
    return render(request,"funciones.html", data)



