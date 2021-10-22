from django.db import models

# Create your models here.

class Mantenimiento(models.Model):
    
    fecha = models.DateField()
    solicitud = models.IntegerField()
    tiempoAtencion = models.IntegerField()


    # def __str__(self) :
    #   return self.
