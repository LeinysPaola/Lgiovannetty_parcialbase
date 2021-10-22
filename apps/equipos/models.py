from django.db import models
from django.db.models.manager import Manager

from apps.mantenimientos.models import Mantenimiento

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    mantenimientos = models.ManyToManyField(Mantenimiento, through='EquipoMantenimiento')


    def __str__(self) :
        return self.nombre



class EquipoMantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete= models.CASCADE, verbose_name="equipos")
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE, verbose_name="mantenimientos")
    descripcion = models.CharField(max_length=300)
    resultado = models.BooleanField()
    