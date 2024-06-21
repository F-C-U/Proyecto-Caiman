from django.urls import include, path
from .views import agregarproducto, modificarproducto

urlpatterns = [
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
]
