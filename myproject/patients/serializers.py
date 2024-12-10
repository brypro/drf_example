from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'rut',
            'apellidos',
            'nombres',
            'diagnostico',
            'doctor',
            'fecha_atencion',
            'hora_atencion'
        ]
