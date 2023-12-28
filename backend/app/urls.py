from django.urls import path
from .views import PlantList
from .views import PlantCreate

urlpatterns = [
    path('plants/', PlantList.as_view(), name='plant-list'),
    path('add-plant/', PlantCreate.as_view(), name='add-plant'),
]