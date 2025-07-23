from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    generos = models.ManyToManyField(Genero, through='LibroGenero', related_name='libros')

    def __str__(self):
        return self.titulo


class LibroGenero(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('libro', 'genero')

    def __str__(self):
        return f"{self.libro.titulo} - {self.genero.nombre}"
