from django.shortcuts import render
from .forms import ProductoForm, UpdateProductoForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from os import remove, path
from django.conf import settings

# Create your views here.
def productos(request):
    productos=Producto.objects.all()
    datos={
        "productos":productos
    }


    return render(request,'caiman/productos.html',datos)

def agregarproducto(request):
    form=ProductoForm()
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="productos")

    datos={
        "form":form
    }


    return render(request,'caiman/agregarproducto.html',datos)

def modificarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    print(producto)
    form = UpdateProductoForm(instance=producto)
    
    
    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST,files=request.FILES,instance=producto)
        if form.is_valid():
            form.save()
        return redirect(to="productos")
    
    datos={
        "form":form,
        "producto":producto
    }

    return render(request,'caiman/modificarproducto.html',datos)

def eliminarproducto(request, id):
    producto=get_object_or_404(Producto, id=id)
    
    if request.method=="POST":
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+producto.imagen.url)
        producto.delete()
        return redirect(to="productos")
        
    datos={
        "producto":producto
    }

    return render(request,'caiman/eliminarproducto.html',datos)