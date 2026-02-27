from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet
from .views import ListPatientsView, DetailPatientView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'insurances', InsuranceViewSet, basename='insurance')
router.register(r'medical-records', MedicalRecordViewSet, basename='medical-record')

urlpatterns = [] + router.urls