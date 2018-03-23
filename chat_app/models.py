from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250, default="Hello")
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username + "  " + str(self.date)