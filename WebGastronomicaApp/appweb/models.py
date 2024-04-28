from django.db import models

# Create your models here


class Usuarios(models.Model):
    Rut = models.CharField(primary_key=True, max_length=15, help_text="Rut usuario")
    Correo = models.EmailField(unique=True, help_text="Correo electronico del usuario")
    Nombre = models.CharField(max_length=50, help_text="Nombre del usuario")
    Direccion = models.CharField(max_length=100, help_text="Dirección del usuario")
    Telefono = models.IntegerField(help_text="Numero telefonico del usuario")
    Contraseña = models.CharField(max_length=30,help_text="Contraseña del usuario")
    Tipo_Usuario = models.CharField(max_length=20, help_text="Tipo de usuario")

    def __str__(self):
        return str(self.Rut)



class Platos(models.Model):
    ID_Plato = models.IntegerField(primary_key=True,help_text="Id del plato")
    Nombre = models.CharField(max_length=50 , help_text="Nombre del plato")
    Costo = models.IntegerField(help_text="Valor del plato")
    Region = models.CharField(max_length=50, help_text="Región a la cual pertenece el plato")
    Cantidad_Comensales = models.IntegerField(help_text="Cantidad de personas que pueden comer de este plato")
    Descripcion = models.TextField(max_length=200, help_text="Breve descripción del plato")

    def __str__(self):
        return self.Nombre
    

class Ingredientes(models.Model):
    ID_Ingrediente = models.IntegerField(primary_key=True,help_text="Id del ingrediente")
    nombre = models.CharField(max_length=50 , help_text="nombre del ingrediente")
    Costo = models.IntegerField(help_text="Valor del ingrediente")
    unidad_medida = models.CharField(max_length=4 , help_text="Unidad de medida del ingrediente")

    def __str__(self):
        return self.nombre

class Bodega(models.Model):
    ID_Ing_Bod = models.IntegerField(primary_key=True,help_text="Id del ingrediente en la bodega")
    Cantidad = models.IntegerField(help_text="Cantidad de ingredientes en bodega")
    ID_Ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, help_text="Id del ingrediente")

    def __int__ (self):
        return str(self.ID_Ing_Bod)
    

class Receta(models.Model):
    ID_Ingrediente_Receta = models.IntegerField(primary_key=True,help_text="Id del ingrediente")
    ID_Plato = models.ForeignKey(Platos, on_delete=models.CASCADE, help_text="Id del plato")
    ID_Ingrediente_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, help_text="Id del ingrediente en bodega")
    Cantidad_Ingredientes = models.IntegerField(help_text="Cantidad de ingredientes necesarios")

    def __int__ (self):
        return self.ID_Ingrediente_Receta


class Mesa (models.Model):
    ID_Mesa = models.IntegerField(primary_key=True, help_text="Id de la mesa")
    Nombre_Mesa = models.CharField(max_length=10, help_text="Identificador de la mesa")
    Estado_Ocupado = models.BooleanField()
    Estado_Reservado = models.BooleanField()

    def __str__(self):
        return self.Nombre_Mesa

class Pedidos(models.Model):
    ID_Pedido = models.IntegerField(primary_key=True, help_text="Id del pedido")
    ID_Mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, help_text="Id de la mesa")
    Estado = models.CharField(max_length=20, help_text="Estado en el cual se encuentra el pedido")
    Correo_Sol = models.EmailField(help_text="Correo electronico del usuario")

    def __str__(self):
        return str(self.ID_Pedido)

class Boletas(models.Model):
    ID_Boleta = models.IntegerField(primary_key=True, help_text="Id de la boleta")
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
    ID_reserva = models.IntegerField()
    nombre = models.CharField(max_length=50 , help_text="Ingrese Nombre")
    correo = models.EmailField(help_text="Ingrese Correo")
    fecha = models.DateField(help_text="Ingrese fecha")
    hora = models.TimeField(help_text="Ingrese hora")
    cantidad_comensales = models.IntegerField(help_text="Ingrese cantidad de comensales")
    ID_Mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, help_text="Id de la mesa")

    def __str__(self):
        return str(self.ID_reserva) 