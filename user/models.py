from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.IntegerField

class UserMedia(models.Model):
    media_link = models.TextField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

