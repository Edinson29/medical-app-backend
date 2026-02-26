from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MedicalSerializer
from .models import Medical

class MedicalViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalSerializer
    queryset: QuerySet = Medical.objects.all()
    
    @action(detail=True, methods=['post'], url_path='toggle-vacation')
    def toggle_vacation(self, request, pk=None):
        medical = self.get_object()
        medical.is_on_vacation = not medical.is_on_vacation
        medical.save()
        return Response(f"Medical updated {medical.is_on_vacation}")