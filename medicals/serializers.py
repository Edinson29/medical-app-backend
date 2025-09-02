from rest_framework import serializers
from .models import Medical, Department, MedicalAvailability, MedicalNote


class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ("id", "first_name", "last_name", "qualification", "contact_number", "email", "address", "biography")


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name", "description")


class MedicalAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAvailability
        fields = ("id", "medical", "start_date", "end_date", "start_time", "end_time")


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = ("id", "medical", "note", "date")
