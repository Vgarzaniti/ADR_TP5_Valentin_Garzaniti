from django.db import models

# Create your models here.
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
