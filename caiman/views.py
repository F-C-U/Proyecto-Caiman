from django.shortcuts import render
from .forms import ProductoForm, UpdateProductoForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Producto

# Create your views here.
def agregarproducto(request):
    form=ProductoForm()
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

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
    
    datos={
        "form":form,
        "producto":producto
    }

    return render(request,'caiman/modificarproducto.html',datos)