from django.db import models
from django.contrib.auth.models import User

class Horse(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}"
    
class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Corrigido max_length
    horses = models.ManyToManyField(Horse, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"