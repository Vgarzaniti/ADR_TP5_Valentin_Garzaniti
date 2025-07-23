from rest_framework import viewsets, filters
from .models import Libro,Genero,LibroGenero
from .serializers import LibroSerializer, GeneroSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'autor']
    ordering_fields = ['anio']

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer