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
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE,
    related_name= 'patient_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE,
    related_name= 'doctor_profile', primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    specialty = models.CharField(max_length=100)
    availability = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class HealthProfile(models.Model):
    user = models.OneToOneField(Patient, on_delete= models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    blood_pressure = models.CharField(max_length=20, blank=True)
    health_conditions = models.TextField(max_length=200, blank=True)
    doctor = models.ManyToManyField(Doctor, blank=True)
    medicines = models.ManyToManyField('products.Medicines', blank=True)
    ayurvedic = models.ManyToManyField('products.AyurvedicMedicines', blank=True)
    supplements = models.ManyToManyField('products.HealthSupplements', blank=True)
    essentials = models.ManyToManyField('products.DailyEssentials', blank=True)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    upload_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

