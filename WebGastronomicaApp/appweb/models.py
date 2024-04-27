from django.db import models

# Create your models here
class Mesa (models.Model):
    ID_Mesa = models.IntegerField(primary_key=True, help_text="Id de la mesa")
    Nombre_Mesa = models.CharField(max_length=10, help_text="Identificador de la mesa")
    Estado_Ocupado = models.BooleanField()
    Estado_Reservado = models.BooleanField()

    def __str__(self):
        return self.Nombre_Mesa


class Reserva_Mesa(models.Model):
    ID_reserva = models.IntegerField()
    nombre = models.CharField(max_length=50 , help_text="Ingrese Nombre")
    correo = models.EmailField(help_text="Ingrese Correo")
    fecha = models.DateField(help_text="Ingrese fecha")
    hora = models.TimeField(help_text="Ingrese hora")
    cantidad_comensales = models.IntegerField(help_text="Ingrese cantidad de comensales")
    ID_Mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, help_text="Id de la mesa")

    def __str__(self):
        return self.ID_reserva 