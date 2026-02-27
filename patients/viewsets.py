from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


    @action(detail=True, methods=['get'], url_path='medical-history')
    def get_medical_history(self, request, pk=None):
        patient = self.get_object()
        return Response({'medical_history': patient.medical_history})