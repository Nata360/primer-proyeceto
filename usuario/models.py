from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# cómo utilizar una imagen dentro de un modelo (minuto 1:25:26 playground avanzado III)
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)