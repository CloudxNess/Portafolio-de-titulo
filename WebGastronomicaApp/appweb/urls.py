from django.urls import path
from .views import *


urlpatterns = [
     path('',splash , name="splash"),
     path('splash',splash,name="splash"),
     path('home/',home , name="index"),
     path('menu',menu , name="menu"),
     path('reservamesa',reservamesa , name="reservamesa"),
     path('registrouser',registrouser,name='registrouser'),
     path('registro',registro,name='registro'),
     path('registro_cli',registro_cli,name='registro_cli'),
     path('estadopedidoc',estadopedidoc,name='estadopedidoc'),
     path('estadopedidog',estadopedidog,name='estadopedidog'),
     path('mesas',mesas,name='mesas'),
     path('agregarplato', agregarplato, name='agregarplato'),
     path('listaringredientes', listaringredientes, name='listaringredientes' ),
     path('agregaringredientes', agregaringredientes, name='agregaringrediente' ),
     path('listarusuarios',listarusuarios,name='listarusuarios'),
     path('sol_ingredientes',sol_ingredientes,name='sol_ingredientes'),
     path('DescargarReporteExcel', DescargarReporteExcel, name='DescargarReporteExcel'),
     path('menuadmin', menuadmin , name='menuadmin'),
     path('modificarmenu/<NombreBuscado>', modificarmenu, name='modificarmenu'), 
     path('activaplato/<NombreBuscado>', activaplato, name='activaplato'), 
     path('desactivaplato/<NombreBuscado>', desactivaplato, name='desactivaplato'),
     path('menu', menu, name='menu'),
     path('actualizar_ingrediente2/<ingredientebusca>', actualizar_ingrediente2, name='actualizar_ingrediente2'),
     path('descuenta_ingrediente/<IdSolicitud>', descuenta_ingrediente, name='descuenta_ingrediente'),
     path('listaragendamiento', listaragendamiento, name='listaragendamiento' ),
     path('mesasparapedido',mesasparapedido,name='mesasparapedido'),
     path('ingresopedidomesa/<Mesa>',ingresopedidomesa,name='ingresopedidomesa'),
     path('actualizar_agendamiento/<reserva>', actualizar_agendamiento, name='actualizar_agendamiento'),
     path('inicia_pedido/<Mesaa>',inicia_pedido,name='inicia_pedido'),
     path('termina_pedido/<Mesaa>',termina_pedido,name='termina_pedido'),
     path('termina_pedido_nulo/<Mesaa>',termina_pedido_nulo,name='termina_pedido_nulo'),
     path('pedidolista/<Mesaa>/<Plato>',pedidolista,name='pedidolista'),
     path('eliminapedidolista/<Mesaa>/<pedido>',eliminapedidolista,name='eliminapedidolista'),
     path('enviapedidococina/<Mesaa>',enviapedidococina,name='enviapedidococina'),
     path('boleta/<Boleta>',boleta,name='boleta'),
     path('pedidosingresadoscocina',pedidosingresadoscocina,name='pedidosingresadoscocina'),
     path('estadoplatolisto/<Id_pedido>',estadoplatolisto,name='estadoplatolisto'),
     path('pago/<Boleta>',pago,name='pago'),
     path('pagado/<Boleta>',pagado,name='pagado'),
     path('carrito',carrito,name='carrito'),
     path('funciones/<Id_user>',funciones,name='funciones'),
     path('limpiarreserva',limpiarreserva,name='limpiarreserva'),
     path('agregar_plato/<int:plato_id>',agregar_plato, name="agregar_plato"),
     path("eliminar/<int:plato_id>/",eliminar_plato, name="eliminar_plato"),
     path("restar_plato/<int:plato_id>/",restar_plato, name="restar_plato"),
     path("limpiar/",limpiar_carro, name="limpiar_carro"),
     path('eliminar_colaborador/<usuario>', eliminar_colaborador,name='eliminar_colaborador'),
     path('modificar_colaborador/<usuario>', modificar_colaborador,name='modificar_colaborador'),
     path('eliminar_colaborador/<username>', eliminar_colaborador,name='eliminar_colaborador'),
     path('modificar_colaborador/<rut>', modificar_colaborador,name='modificar_colaborador'),
     path('inicia_pedido_online', inicia_pedido_online,name='inicia_pedido_online'),
     path('lista_pedidos_online', lista_pedidos_online,name='lista_pedidos_online'),
     path('pedido_online_cocina/<plato>/<cantidad>', pedido_online_cocina,name='pedido_online_cocina'),
     path('termino_pedido_online/<Mesaa>', termino_pedido_online,name='termino_pedido_online'),
     path('boletaonline', boletaonline,name='boletaonline'),
     path('eliminarP', eliminarP,name='eliminarP'),
]
