from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Description(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # Wyświetla tylko pierwsze 50 znaków opisu

class Plant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plant_images/')
    water_last = models.DateField()
    water_cycle = models.IntegerField()
    fertilizer_last = models.DateField()
    fertilizer_cycle = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True, blank=True)  # Opcjonalne pole description

    def __str__(self):
        return self.name

