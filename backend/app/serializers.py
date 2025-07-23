from rest_framework import serializers
from .models import Libro, Genero, LibroGenero

class LibroSerializer(serializers.ModelSerializer):
    generos = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genero.objects.all()
    )

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'anio', 'generos']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']