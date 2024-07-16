from django.db import models
from django.contrib.auth.models import User
    
class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"

class Horse(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, default=None, blank=True, null=True)
    employees = models.ManyToManyField('Employee', through='TrainingSession')

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    horses = models.ManyToManyField(Horse, through='TrainingSession')

    def __str__(self):
        return f"{self.name}"

class TrainingSession(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()  # Duração do treinamento
    notes = models.TextField(blank=True, null=True)  # Notas sobre a sessão

    def __str__(self):
        return f"Training on {self.date} for {self.horse.name} by {self.employee.name}"