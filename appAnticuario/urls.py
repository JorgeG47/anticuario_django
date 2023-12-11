from django.urls import path

from . import views

from appAnticuario.views import agregarProducto, eliminarProducto, restarProducto, limpiarCarrito

urlpatterns = [
    path('', views.Anticuario, name='Anticuario'),
    path('index', views.index, name='index'),
    path('Anticuario', views.Anticuario, name='Anticuario'),
    path('Etiquetas', views.Etiquetas, name='Etiquetas'),
    path('ServicioAlCliente', views.ServicioAlCliente, name='ServicioAlCliente'),

    path('Filtros', views.Filtros, name='Filtros'),

    path('Ofertas', views.Ofertas, name='Ofertas'),  
    
    path('agregar/<int:id_prod>/', agregarProducto, name="Add"),
    path('eliminar/<int:id_prod>/', eliminarProducto, name="Del"),
    path('restar/<int:id_prod>/', restarProducto, name="Sub"),
    path('limpiar/', limpiarCarrito, name="CLS"),

    path('Menaje', views.Menaje, name='Menaje'),
    path('Instrumentos', views.Instrumentos, name='Instrumentos'),
    path('Dormitorio', views.Dormitorio, name='Dormitorio'),

    path('formularioCompra', views.formularioCompra, name='formularioCompra'),

    path('Productos', views.get_productos, name='Productos'),

]

