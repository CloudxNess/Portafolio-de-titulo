from django import forms
from .models import *
from datetime import time

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
        fields = ["Nombre", "Costo", "Region","Cantidad_Comensales", "Descripcion", "imagen"]


class reservamesaForm(forms.ModelForm):
    class Meta:
        model = Reserva_Mesa
        fields = ["nombre", "correo", "fecha", "hora", "cantidad_comensales"]
        widgets = {
            "fecha": forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d')),
           "hora": forms.Select(choices=[(f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}") for h in range(10, 22) for m in [0, 30]], attrs={'class': 'form-control'}),
        }

    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        hora_minima = time(10, 0)  # 10:00 AM
        hora_maxima = time(22, 0)  # 10:00 PM

        if hora < hora_minima or hora > hora_maxima:
            raise forms.ValidationError("La hora debe estar entre las 10:00 y las 22:00.")

        return hora



class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['Cantidad']  # Campos que se pueden editar en el formulario