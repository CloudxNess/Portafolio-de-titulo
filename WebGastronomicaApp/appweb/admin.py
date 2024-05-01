from django.contrib import admin
from .models import *

# Register your models here.

class Reserva_MesaAdmin(admin.ModelAdmin):
    list_display = ['ID_reserva', 'nombre', 'ID_Mesa']
    search_fields = ['ID_reserva']


class MesaAdmin(admin.ModelAdmin):
    list_display = ['Nombre_Mesa']
    search_fields = ['Nombre_Mesa']


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['ID_Pedido']
    search_fields = ['ID_Pedido']


class IngredientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'Costo']
    search_fields = ['nombre', 'Costo']


class BodegaAdmin(admin.ModelAdmin):
    list_display = ['ID_Ing_Bod', 'Cantidad']
    search_fields = ['ID_Ing_Bod']


class PlatosAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Costo', 'Region']
    search_fields = ['Nombre', 'Region']


class RecetaAdmin(admin.ModelAdmin):
    list_display = ['ID_Ingrediente_Receta']
    search_fields = ['ID_Ingrediente_Receta']


class Descripción_PedidosAdmin(admin.ModelAdmin):
    list_display = ['ID_Pedido', 'Costo']
    search_fields = ['ID_Pedido']


class BoletasAdmin(admin.ModelAdmin):
    list_display = ['ID_Boleta', 'Fecha']
    search_fields = ['ID_Boleta', 'Fecha']
    

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Rut', 'Tipo_Usuario']
    search_fields = ['Nombre', 'Rut', 'Tipo_Usuario']


admin.site.register(Reserva_Mesa, Reserva_MesaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Pedidos, PedidoAdmin)
admin.site.register(Ingredientes, IngredientesAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Platos, PlatosAdmin)
admin.site.register(Receta, RecetaAdmin)
admin.site.register(Descripción_Pedidos, Descripción_PedidosAdmin)
admin.site.register(Boletas, BoletasAdmin)
admin.site.register(Usuarios, UsuariosAdmin)