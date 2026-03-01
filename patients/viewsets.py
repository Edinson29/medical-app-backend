from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    throttle_classes = [] # Elimina la limitación de tasa para este ViewSet

    @action(detail=True, methods=['get'], url_path='medical-history')
    def get_medical_history(self, request, pk=None):
        patient = self.get_object()
        return Response({'medical_history': patient.medical_history})


class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()