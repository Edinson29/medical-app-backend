from rest_framework import viewsets
from .serializers import MedicalSerializer
from .models import Medical
from django.db.models import QuerySet

class MedicalViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalSerializer
    queryset: QuerySet = Medical.objects.all()
    