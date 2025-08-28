from rest_framework import serializers
from .models import Medical, Department, MedicalAvailability, MedicalNote

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class MedicalAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'