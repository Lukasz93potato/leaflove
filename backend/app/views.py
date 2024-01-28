from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # Dodane import

from .models import Plant
from .serializers import PlantSerializer

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from rest_framework.permissions import AllowAny

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

class PlantDelete(generics.DestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def delete(self, request, *args, **kwargs):
        plant = get_object_or_404(Plant, pk=kwargs['pk'])
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdatePlantWaterLast(generics.UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def update(self, request, *args, **kwargs):
        try:
            plant = get_object_or_404(Plant, pk=kwargs['pk'])
            plant.water_last = request.data.get('water_last')  # timezone.now()
            plant.save()
            return JsonResponse({'message': 'Watering date updated successfully'}, status=200)
        except Plant.DoesNotExist:
            return JsonResponse({'error': 'Plant not found'}, status=404)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            return JsonResponse({'error': str(e)}, status=500)

    # def update_plant_water_last(self, request, *args, **kwargs):
    #     try:
    #         plant = get_object_or_404(Plant, pk=kwargs['pk'])
    #         plant.water_last = request.data.get('water_last') #timezone.now()
    #         plant.save()
    #         return JsonResponse({'message': 'Watering date updated successfully'}, status=200)
    #     except Plant.DoesNotExist:
    #         return JsonResponse({'error': 'Plant not found'}, status=404)
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=500)