from django.db import models

# Create your models here.
class Pilotos(models.Model):
    nombre = models.CharField(max_length=50)
    equipo = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='media')
    campeonatos = models.CharField(max_length=10)


