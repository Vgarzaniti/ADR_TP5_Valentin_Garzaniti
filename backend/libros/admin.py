from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'anio')
    search_fields = ('titulo', 'autor')

# Register your models here.
