from django.urls import path
from .views import PlantList, PlantCreate, PlantDelete, UpdatePlantWaterLast

urlpatterns = [
    path('plants/', PlantList.as_view(), name='plant-list'),
    path('add-plant/', PlantCreate.as_view(), name='add-plant'),
    path('delete-plant/<int:pk>/', PlantDelete.as_view(), name='delete-plant'),
    path('update-plant-water-last/<int:pk>/', UpdatePlantWaterLast.as_view(), name='update_plant_water_last'),
]
