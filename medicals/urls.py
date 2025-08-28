from django.urls import path
from .views import list_medicals, detail_medical

urlpatterns = [
    path("medicals/", list_medicals),
    path("medicals/<int:pk>/", detail_medical),
]
