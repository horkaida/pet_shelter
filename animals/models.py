from django.db import models
from django.contrib.auth.models import User

class AnimalType(models.Model):
    type = models.CharField(max_length=200)

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sex = models.BooleanField()
    age = models.IntegerField()
    breed = models.CharField(max_length=200)
    availability = models.BooleanField()
    description = models.TextField()
    healthy = models.BooleanField()
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)


class AnimalMedia(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    media_link = models.TextField()
    is_main = models.BooleanField()


class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Feedback(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)