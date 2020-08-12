"""
This module creates a CustomUser class that removes the username
field and makes the email field required and unique
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Remove the username field and make the email field required
    and unique
    """
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE,
    related_name= 'patient_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE,
    related_name= 'doctor_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    specialty = models.CharField(max_length=100)
    availability = models.CharField(max_length=200)

