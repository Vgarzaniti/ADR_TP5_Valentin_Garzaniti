from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Libro
from .serializers import LibroSerializer

# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('-id')
    serializer_class = LibroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'autor']
