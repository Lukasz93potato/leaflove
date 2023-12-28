from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'image', 'water_last', 'water_cycle', 'fertilizer_last', 'fertilizer_cycle']