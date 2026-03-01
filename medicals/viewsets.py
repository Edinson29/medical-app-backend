from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MedicalSerializer, DepartmentSerializer, MedicalAvailabilitySerializer, MedicalNoteSerializer
from .models import Medical, Department, MedicalAvailability, MedicalNote
from .permissions import IsDoctor
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment

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
    
    @action(["POST", "GET", "PUT", "DELETE"], detail=True, serializer_class=AppointmentSerializer, url_path="appointments(?:/(?P<appointment_id>[^/.]+))?")
    def appointments(self, request, pk=None, appointment_id=None):
        medical = self.get_object()

        if request.method == "POST":
            data = request.data.copy()
            data["medical"] = medical.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == "GET":
            if appointment_id:
                try:
                    appointment = medical.appointments.get(id=appointment_id)
                    serializer = AppointmentSerializer(appointment)
                    return Response(serializer.data)
                except Appointment.DoesNotExist:
                    return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                appointments = medical.appointments.all()
                serializer = AppointmentSerializer(appointments, many=True)
                return Response(serializer.data)
            
        if request.method == "PUT":
            if not appointment_id:
                return Response({"error": "Appointment ID is required in the URL."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                appointment = medical.appointments.get(id=appointment_id)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.method == "DELETE":
            if not appointment_id:
                return Response({"error": "Appointment ID is required in the URL."}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                appointment = medical.appointments.get(id=appointment_id)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
            
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class MedicalAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalAvailabilitySerializer
    queryset = MedicalAvailability.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()