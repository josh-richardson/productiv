from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Website(models.Model):
    url = models.TextField()
    useful = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username