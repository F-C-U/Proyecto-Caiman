from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def agregarproducto(request):
    form=ProductoForm()
    print(form)
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

    datos={
        "form":form
    }


    return render(request,'caiman/agregarproducto.html',datos)