from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientsListView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls)),
    path('lista_pacientes/', PatientsListView.as_view(), name='patients_list_page'),
]
