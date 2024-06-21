
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from os import remove, path
from django.conf import settings

# Create your views here.



from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View


from caiman.forms import *

class RegistroUsuario(View):
    def get(self, request):
        return render(request, 'caiman/registrouser.html')

    def post(self, request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        userName = request.POST['userName']
        mail = request.POST['mail']
        telefono = request.POST['telefono']
        ciudad = request.POST['ciudad']
        direccion = request.POST['direccion']
        pass1 = request.POST['pass']
        pass2 = request.POST['rePass']

        if pass1 == pass2:
            if User.objects.filter(username=userName).exists():
                messages.info(request, 'El nombre de usuario ya existe')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'El correo electrónico ya está registrado')
            else:
                user = User.objects.create_user(username=userName, password=pass1, email=mail, first_name=nombre, last_name=apellido)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Las contraseñas no coinciden')
        
        return render(request, 'caiman/registrouser.html')
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

