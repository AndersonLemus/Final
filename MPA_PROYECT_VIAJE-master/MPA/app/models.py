from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    año = models.CharField(max_length=4)
    dias = models.CharField(max_length=2)
    calificacion = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre