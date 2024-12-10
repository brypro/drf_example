from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Patient

class PatientAPITestCase(APITestCase):

    def setUp(self):
        # Creamos algunos pacientes de prueba
        self.patient1 = Patient.objects.create(
            rut="11111111-1",
            apellidos="Perez",
            nombres="Juan",
            diagnostico="Gripal",
            doctor="Dr. Gonzalez",
            fecha_atencion="2024-12-10",
            hora_atencion="10:00:00"
        )
        self.patient2 = Patient.objects.create(
            rut="22222222-2",
            apellidos="Gomez",
            nombres="Maria",
            diagnostico="Migraña",
            doctor="Dr. Lopez",
            fecha_atencion="2024-12-11",
            hora_atencion="11:30:00"
        )

        self.list_url = reverse('patients-list')  # De router: 'patients' es el basename => patients-list para GET, POST
        # para acciones detail tenemos: patients-detail con pk=<id>
        self.por_diagnostico_url = reverse('patients-por-diagnostico')  # acción personalizada

    def test_list_patients(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # tenemos dos pacientes creados en setUp

    def test_create_patient(self):
        data = {
            "rut": "33333333-3",
            "apellidos": "Rodriguez",
            "nombres": "Pedro",
            "diagnostico": "Gastritis",
            "doctor": "Dr. Alvarez",
            "fecha_atencion": "2024-12-12",
            "hora_atencion": "09:00:00"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 3)  # Ahora 3 pacientes

    def test_update_patient(self):
        # Actualizar el nombre del paciente1
        detail_url = reverse('patients-detail', args=[self.patient1.id])
        data = {
            "rut": self.patient1.rut,
            "apellidos": "Perez",
            "nombres": "Juan Carlos",  # Actualizamos este campo
            "diagnostico": "Gripal",
            "doctor": "Dr. Gonzalez",
            "fecha_atencion": "2024-12-10",
            "hora_atencion": "10:00:00"
        }
        response = self.client.put(detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.patient1.refresh_from_db()
        self.assertEqual(self.patient1.nombres, "Juan Carlos")

    def test_delete_patient(self):
        detail_url = reverse('patients-detail', args=[self.patient2.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 1)  # Eliminamos uno, debería quedar 1

    def test_filter_by_diagnosis(self):
        # Probamos la acción personalizada /patients/por_diagnostico/?q=gripal
        response = self.client.get(f"{self.por_diagnostico_url}?q=gripal")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Solo patient1 tiene "Gripal"
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['rut'], "11111111-1")

        # Probar sin pasar q
        response_no_q = self.client.get(self.por_diagnostico_url)
        self.assertEqual(response_no_q.status_code, status.HTTP_400_BAD_REQUEST)
