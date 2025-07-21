from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

    def validate(self, data):
        for field in ['titulo', 'autor', 'genero', 'anio']:
            if not data.get(field):
                raise serializers.ValidationError(f"El campo '{field}' es obligatorio.")
        return data
