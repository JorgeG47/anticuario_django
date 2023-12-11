from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from django.db.models import Q

from appAnticuario.Carrito import Carrito

from .models import producto
# Create your views here.

def index(request):
    productos= producto.objects.all()
    context={"productos":productos}
    return render(request, 'appAnticuario/index.html', context)

def get_productos(request):
    productos= list(producto.objects.values())  
    
    if (len(productos)>0):
        data={'message': "Success", 'productos':productos}
    else:
        data={'message':"Data Not Found"}
    
    return JsonResponse(data)

def Anticuario(request):
    productos= producto.objects.all()
    context={"productos":productos}
    return render(request, 'appAnticuario/Anticuario.html', context)

def Etiquetas(request):
    productos= producto.objects.all()
    context={"productos":productos}
    return render(request, 'appAnticuario/Etiquetas.html', context)

def Filtros(request):
    busqueda =request.GET.get('buscar')
    busquedaPrecio =request.GET.get('buscarPrecio')
    productos= producto.objects.all()
    if busqueda:
        productos = producto.objects.filter(
            Q(nom_prod__icontains = busqueda)|
            Q(desc_prod__icontains = busqueda)
        ).distinct()

    elif busquedaPrecio:
        productos = producto.objects.filter(precio_prod__lte = busquedaPrecio)

    context={"productos":productos}
    return render(request, 'appAnticuario/Filtros.html', context)

def Ofertas(request):
    productos = producto.objects.filter(enOferta=True)
    context = {"productos": productos}
    return render(request, 'appAnticuario/Ofertas.html', context)

def agregarProducto(request, id_prod):
    carrito= Carrito(request)
    productos= producto.objects.get(id_prod=id_prod)
    carrito.agregar(productos)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminarProducto(request, id_prod):
    carrito= Carrito(request)
    productos= producto.objects.get(id_prod=id_prod)
    carrito.eliminar(productos)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def restarProducto(request, id_prod):
    carrito= Carrito(request)
    productos= producto.objects.get(id_prod=id_prod)
    carrito.restar(productos)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def limpiarCarrito(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def ServicioAlCliente(request):
    productos= producto.objects.all()
    context={"productos":productos}
    return render(request, 'appAnticuario/ServicioAlCliente.html', context)


def Dormitorio(request):
    # Reemplaza 'id_prod_etiqueta' con el ID que deseas filtrar
    productos = producto.objects.filter(id_prod_etiqueta='Dormitorio')
    context = {"productos": productos}
    return render(request, 'appAnticuario/Dormitorio.html', context)

def Menaje(request):
    # Reemplaza 'id_prod_etiqueta' con el ID que deseas filtrar
    productos = producto.objects.filter(id_prod_etiqueta='Menaje')
    context = {"productos": productos}
    return render(request, 'appAnticuario/Menaje.html', context)

def Instrumentos(request):
    # Reemplaza 'id_prod_etiqueta' con el ID que deseas filtrar
    productos = producto.objects.filter(id_prod_etiqueta='Instrumentos')
    context = {"productos": productos}
    return render(request, 'appAnticuario/Instrumentos.html', context)

def formularioCompra(request):
    productos= producto.objects.all()
    context={"productos":productos}
    return render(request, 'appAnticuario/formularioCompra.html', context)
