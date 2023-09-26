from django.db import models
from user.models import User
class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    sex = models.IntegerField
    age = models.IntegerField
    breed = models.CharField(max_length=200)
    availability = models.BooleanField
    description = models.TextField
    healthy = models.BooleanField


class AnimalMedia(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    media_link = models.TextField
    main = models.BooleanField


class Schedule(models.Model):
    start_time = models.DateTimeField
    end_time = models.DateTimeField
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
