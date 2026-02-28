from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer
from datetime import datetime


class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()
    class Meta:
        model = Patient
        fields = (
            "id",
            "first_name",
            "last_name",
            "age",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments",
        )

    def validate_date_of_birth(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("La fecha de nacimiento debe ser en el pasado.")
        return value
    
    def get_age(self, obj):
        today = datetime.now().date()
        birth_date = obj.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ("id", "patient", "provider", "policy_number", "expiration_date")


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ("id", "patient", "date", "diagnosis", "treatment", "follow_up_date")
