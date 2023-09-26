from django.db import models
from animals.models import Animal
from user.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)