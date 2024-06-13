from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View

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
