from rest_framework import generics, status
from rest_framework.response import Response
from .models import Plant
from .serializers import PlantSerializer



class PlantList(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantCreate(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)