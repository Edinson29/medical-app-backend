from django.urls import path
from .views import list_medicals, detail_medical
from rest_framework.routers import DefaultRouter
from .viewsets import MedicalViewSet

router = DefaultRouter()
router.register(r'medicals', MedicalViewSet, basename='medical')


urlpatterns = [] + router.urls
