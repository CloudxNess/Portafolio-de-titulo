from django.db import models

# Create your models here

class Reserva_Mesa(models.Model):
    id_reserva = models.IntegerField()
    nombre = models.CharField(max_length=50 , help_text="Ingrese Nombre")
    correo = models.EmailField(help_text="Ingrese Correo")
    fecha = models.DateField(help_text="Ingrese fecha")
    hora = models.IntegerField(help_text="Ingrese hora")
    cantidad_comensales = models.IntegerField(help_text="Ingrese cantidad de comensales")
    

    def __str__(self):
        return self.id_reserva