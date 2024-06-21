from django.urls import include, path
from .views import productos, agregarproducto, modificarproducto, eliminarproducto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productos/', productos, name='productos'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('modificarproducto/<id>', modificarproducto, name='modificarproducto'),
    path('eliminarproducto/<id>', eliminarproducto, name='eliminarproducto'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)