from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)  # Tekst
    image = models.ImageField(upload_to='plant_images/')  # Ścieżka do pliku obrazu
    water_last = models.DateField()  # Data ostatniego podlewania
    water_cycle = models.IntegerField()  # Liczba dni do kolejnego podlewania
    fertilizer_last = models.DateField()  # Data ostatniego nawożenia
    fertilizer_cycle = models.IntegerField()  # Liczba dni do kolejnego nawożenia

    def __str__(self):
        return self.name
