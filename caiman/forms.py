from django import forms
from .models import *

class ProductoForm(forms.Form):
    class Meta:
        model=Producto
        fields=['nombre','descripcion','cantidad','precio','imagen']
