from django.urls import path
from .views import RegistroUsuario  # Asegúrate de importar la clase

urlpatterns = [
    path('registro/', RegistroUsuario.as_view(), name='registro'),
]
