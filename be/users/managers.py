"""
This module creates a custom user model manager that enables the
use of email for authentication instead of username
"""

from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager that uses email as the unique
    identifier for authentication instead of username
    """

    def create_user(self, email, password, **kwargs):
        """
        Create and save a user using the given email and password
        """
        if not email:
            raise ValueError("Email addresss is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, password, **kwargs):
        """
        Create and save a superuser using the given email and password
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **kwargs)
