from django.db import models
from django.utils import timezone

## No se sabe si se usa la tabla

tipo_usuario_choices = ("GAR", "Garzon") , ("COC", "Cocinero")

class Usuarios(models.Model):

    Rut = models.CharField(primary_key=True, max_length=15, help_text="Rut usuario")
    Correo = models.EmailField(unique=True, help_text="Correo electronico del usuario")
    Nombre = models.CharField(max_length=50, help_text="Nombre del usuario")
    Direccion = models.CharField(max_length=100, help_text="Dirección del usuario")
    Telefono = models.IntegerField(help_text="Numero telefonico del usuario")
    Contrasena = models.CharField(max_length=30,help_text="Contraseña del usuario")
    Tipo_Usuario = models.CharField(max_length=20, choices=tipo_usuario_choices, default='Garzón')
 
    def __str__(self):
        return str(self.Rut)

## No se sabe si se usa la tabla


class Platos(models.Model):
    ID_Plato = models.AutoField(primary_key=True, help_text="Id del plato")
    Nombre = models.CharField(max_length=50)
    Costo = models.IntegerField()
    Region = models.CharField(max_length=50)
    Cantidad_Comensales = models.IntegerField()
    Descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to="Platos", null=True)

    def __str__(self):
        return self.Nombre
    

class Ingredientes(models.Model):
    ID_Ingrediente = models.AutoField(primary_key=True,help_text="Id del ingrediente")
    nombre = models.CharField(max_length=50 , help_text="nombre del ingrediente")
    Costo = models.IntegerField(help_text="Valor del ingrediente")
    unidad_medida = models.CharField(max_length=4 , help_text="Unidad de medida del ingrediente")

    def __str__(self):
        return self.nombre


class Bodega(models.Model):
    ID_Ing_Bod = models.AutoField(primary_key=True,help_text="Id del ingrediente en la bodega")
    Cantidad = models.IntegerField(help_text="Cantidad de ingredientes en bodega")
    ID_Ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, help_text="Id del ingrediente")
    

    def __int__ (self):
        return str(self.ID_Ing_Bod)
    

class Receta(models.Model):
    ID_Ingrediente_Receta = models.AutoField(primary_key=True,help_text="Id del ingrediente") 
    ID_Plato = models.ForeignKey(Platos, on_delete=models.CASCADE, help_text="Id del plato")
    ID_Ingrediente_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, help_text="Id del ingrediente en bodega")
    Cantidad_Ingredientes = models.IntegerField(help_text="Cantidad de ingredientes necesarios")

    def __int__ (self):
        return self.ID_Ingrediente_Receta


class Mesa (models.Model):
    ID_Mesa = models.AutoField(primary_key=True, help_text="Id de la mesa")
    Nombre_Mesa = models.CharField(max_length=10, help_text="Identificador de la mesa")
    Estado_Ocupado = models.BooleanField()
    Estado_Reservado = models.BooleanField()

    def __str__(self):
        return self.Nombre_Mesa

class Pedidos(models.Model):
    ID_Pedido = models.AutoField(primary_key=True, help_text="Id del pedido")
    ID_Mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, help_text="Id de la mesa")
    Estado = models.CharField(max_length=20, help_text="Estado en el cual se encuentra el pedido")
    Correo_Sol = models.EmailField(help_text="Correo electronico del usuario")

    def __str__(self):
        return str(self.ID_Pedido)

class Boletas(models.Model):
    ID_Boleta = models.AutoField(primary_key=True, help_text="Id de la boleta")
    ID_Pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, help_text="Id del pedido")
    Fecha = models.DateField(help_text="Fecha de emision de la boleta")
    Costo_Total = models.IntegerField(help_text="Valor total de atención")

    def __str__(self):
        return str(self.ID_Boleta)
    

class Descripción_Pedidos(models.Model):
    ID_Pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, help_text="Id de pedido")
    ID_Platos = models.ForeignKey(Platos, on_delete=models.CASCADE, help_text="Id del plato")
    Costo = models.IntegerField(help_text="Valor total del pedido")      

    def __int__(self):
        return self.costo
    

class Reserva_Mesa(models.Model):
    ID_reserva = models.AutoField(primary_key=True, help_text="Id de la reserva")
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_comensales = models.IntegerField()
    ID_Mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, default="0")

    def __str__(self):
        return str(self.ID_reserva) 
    

class Sol_Ingredientes(models.Model):
    ID_Solicitud_Ingrediente = models.AutoField(primary_key=True,help_text="Id de la solicitud")
    Ingrediente = models.ForeignKey(Ingredientes,on_delete=models.CASCADE, default="0")
    Cantidad = models.IntegerField(help_text="Cantidad solicitada")
    fecha_y_hora = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.ID_Solicitud_Ingrediente
		