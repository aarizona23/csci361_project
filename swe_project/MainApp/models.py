from django.db import models
from django.contrib.auth.hashers import make_password

class UserProfile(models.Model):
    STATUS_CHOICES = (
        (1, 'administrator'),
        (2, 'driver'),
        (3, 'maintenance_person'),
        (4, 'gas_fueling_person'),
    )
    username = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=128)
    user_status = models.IntegerField(choices=STATUS_CHOICES, default=1)