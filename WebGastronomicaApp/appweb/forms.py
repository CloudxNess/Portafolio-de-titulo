from django import forms
from .models import *

class agregarform(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"