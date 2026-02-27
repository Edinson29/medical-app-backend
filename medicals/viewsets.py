from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MedicalSerializer, DepartmentSerializer, MedicalAvailabilitySerializer, MedicalNoteSerializer
from .models import Medical, Department, MedicalAvailability, MedicalNote
from .permissions import IsDoctor

class MedicalViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalSerializer
    queryset: QuerySet = Medical.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]
    
    @action(detail=True, methods=['post'], url_path='toggle-vacation')
    def toggle_vacation(self, request, pk=None):
        medical = self.get_object()
        medical.is_on_vacation = not medical.is_on_vacation
        medical.save()
        return Response(f"Medical updated {medical.is_on_vacation}")


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class MedicalAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalAvailabilitySerializer
    queryset = MedicalAvailability.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()