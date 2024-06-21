from django.contrib import admin
from .models import *

class AdmProducto(admin.ModelAdmin):
    list_display= ['nombre','descripcion','cantidad','precio','imagen']

# Register your models here.
admin.site.register(Producto, AdmProducto)