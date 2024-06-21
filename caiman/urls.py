
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import * # Asegúrate de importar la clase

urlpatterns = [
    path('productos/', productos, name='productos'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
    path('eliminarproducto/<id>', eliminarproducto, name='eliminarproducto'),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)