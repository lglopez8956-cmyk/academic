from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    # Cambio de prueba