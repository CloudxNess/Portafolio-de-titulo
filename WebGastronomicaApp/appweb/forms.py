from django import forms
from .models import *

class agregarform(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"


class mesaform(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"

class platosform(forms.ModelForm):
    class Meta:
        model = Platos
        fields = "__all__"