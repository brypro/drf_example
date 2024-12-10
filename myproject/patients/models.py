from django.db import models

class Patient(models.Model):
    rut = models.CharField(max_length=12, unique=True, help_text="RUT del paciente (ej: 12345678-9)")
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=200)
    doctor = models.CharField(max_length=100)
    fecha_atencion = models.DateField()
    hora_atencion = models.TimeField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.rut}"
