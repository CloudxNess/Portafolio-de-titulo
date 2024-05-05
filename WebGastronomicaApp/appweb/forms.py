from django import forms
from .models import *

class agregarform(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"


class agregaringreform(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = ["nombre", "Costo", "unidad_medida"]


class Sol_Ingredientesform(forms.ModelForm):
    class Meta:
        model = Sol_Ingredientes
        fields = ["Ingrediente", "Cantidad"]



class agregaringrebodeform(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ["Cantidad", "ID_Ingrediente"]


class mesaform(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"

class platosform(forms.ModelForm):
    class Meta:
        model = Platos
        fields = "__all__"


class reservamesaform(forms.ModelForm):
    class Meta:
        model = Reserva_Mesa
        fields = ["nombre", "correo", "fecha", "hora", "cantidad_comensales"]

        widgets = {
            "fecha" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d')),
            "hora" : forms.TimeInput(attrs={'type': 'time'}, format=('%H-%M')) 
              }

       