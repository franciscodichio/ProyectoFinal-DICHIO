from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
    
class Articulo(models.Model):
    descripcion = models.CharField(max_length=40)
    codigo = models.IntegerField()
    cantidad= models.IntegerField()

class Cliente(models.Model, LoginRequiredMixin):
    nom_ape = models.CharField(max_length=40)
    cuil_t = models.IntegerField()
    sit_fis = models.CharField(max_length=40)

class Operaciones(models.Model):
    banco = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)
    cbu = models.IntegerField() 
    
    

    