from django.urls import path
from .views import * # Asegúrate de importar la clase

urlpatterns = [
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
]
