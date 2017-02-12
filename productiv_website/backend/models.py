from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    sites = models.ManyToManyField("Website", through="UserWebsite")

    def __str__(self):
        return self.user.username


class Website(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.user.username


class UserWebsite(models.Model):
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    site = models.ForeignKey("Website", on_delete=models.CASCADE)
    useful = models.BooleanField(default=True)

    def __str__(self):
        return self.user + ": " + self.site + " - " + self.useful
