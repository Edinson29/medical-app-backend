from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet
from .views import ListPatientsView, DetailPatientView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [] + router.urls