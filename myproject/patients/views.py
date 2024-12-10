from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # Ejemplo de acción personalizada para filtrar por diagnóstico
    # Se podrá acceder a esta acción vía: GET /patients/por_diagnostico/?q=gripal
    @action(detail=False, methods=['get'], url_path='por_diagnostico')
    def por_diagnostico(self, request):
        diagnostico_query = request.query_params.get('q', None)
        if diagnostico_query:
            pacientes = self.queryset.filter(diagnostico__icontains=diagnostico_query)
            serializer = self.get_serializer(pacientes, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No se especificó un diagnóstico para filtrar."}, status=400)
