from django.urls import path
from .views import list_medicals, detail_medical
from rest_framework.routers import DefaultRouter
from .viewsets import MedicalViewSet, DepartmentViewSet, MedicalAvailabilityViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register(r'medicals', MedicalViewSet, basename='medical')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'medical-availabilities', MedicalAvailabilityViewSet, basename='medical-availability')
router.register(r'medical-notes', MedicalNoteViewSet, basename='medical-note')


urlpatterns = [] + router.urls
