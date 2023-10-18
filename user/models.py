from django.db import models
from django.contrib.auth.models import User

class UserMedia(models.Model):
    media_link = models.TextField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

