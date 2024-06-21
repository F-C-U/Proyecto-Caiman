from django.urls import include, path
from .views import agregarproducto

urlpatterns = [
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    
]
