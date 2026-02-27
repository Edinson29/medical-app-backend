from rest_framework import serializers
from .models import Medical, Department, MedicalAvailability, MedicalNote


class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = (
            "id",
            "first_name",
            "last_name",
            "qualification",
            "contact_number",
            "email",
            "address",
            "biography",
            "is_on_vacation",
        )

    def validate_email(self, value):
        if not value.endswith("@develop.com"):
            raise serializers.ValidationError("El correo debe terminar con @develop.com")
        return value
    
    def validate(self, data):
        if data["is_on_vacation"] and len(data["contact_number"]) < 10:
            raise serializers.ValidationError("El número de contacto debe tener al menos 10 dígitos si el médico está de vacaciones.")
        return data



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
