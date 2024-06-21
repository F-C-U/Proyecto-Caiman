from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    descripcion=models.TextField(max_length=50, null=False)
    cantidad=models.PositiveIntegerField(null=False)
    precio=models.PositiveIntegerField(null=False)
    imagen=models.ImageField(upload_to='productos', null=False)



