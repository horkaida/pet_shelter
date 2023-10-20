from django.db import models
from animals.models import Animal

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
