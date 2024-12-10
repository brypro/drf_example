from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import TemplateView
from drf_spectacular.utils import extend_schema, OpenApiParameter

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # Ejemplo de acción personalizada para filtrar por diagnóstico
    # Se podrá acceder a esta acción vía: GET /patients/por_diagnostico/?q=gripal
    @extend_schema(
        parameters=[
            OpenApiParameter(name='diagnostico', description='Diagnóstico a filtrar', required=False, type=str)
        ]
    )
    @action(detail=False, methods=['get'], url_path='por_diagnostico')
    def por_diagnostico(self, request):
        diagnostico_query = request.query_params.get('diagnostico', None)
        if diagnostico_query:
            pacientes = self.queryset.filter(diagnostico__icontains=diagnostico_query)
            serializer = self.get_serializer(pacientes, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No se especificó un diagnóstico para filtrar."}, status=400)

class PatientsListView(TemplateView):
    template_name = 'patients/index.html'