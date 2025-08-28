from .serializers import MedicalSerializer
from .models import Medical

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def list_medicals(request):

    if request.method == "GET":
        patients = Medical.objects.all()
        serializer = MedicalSerializer(patients, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = MedicalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    

@api_view(["GET", "PUT", "DELETE"])
def detail_medical(request, pk):
    try:
        medical = Medical.objects.get(id=pk)
    except Medical.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MedicalSerializer(medical)
        return Response(serializer.data)
    elif request.method == "PUT":        
        serializer = MedicalSerializer(medical, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        medical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)