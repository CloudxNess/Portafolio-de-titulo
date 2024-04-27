from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Reserva_Mesa)
admin.site.register(Mesa)
admin.site.register(Pedidos)
admin.site.register(Ingredientes)
admin.site.register(Bodega)
admin.site.register(Platos)
admin.site.register(Receta)
admin.site.register(Descripción_Pedidos)