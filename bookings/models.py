from django.db import models
from medicals.models import Medical
from patients.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='appointments', on_delete=models.CASCADE
    )
    medical = models.ForeignKey(
        Medical, related_name='appointments', on_delete=models.CASCADE
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=10)

class MedicalNote(models.Model):
    appointment = models.ForeignKey(
        Appointment, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
