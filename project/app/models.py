from django.db import models


# Create your models here.
class UserModel(models.Model):
    user = models.EmailField(max_length=60)
    password = models.CharField(max_length=20)


def __str__(self):
    return self.user
