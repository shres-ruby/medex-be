from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import CustomUser, Patient, Doctor

USER = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','password1','password2')
    
    def clean_email(self):
        if USER.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("An account already exists with this email")
        return self.cleaned_data['email']
    
    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match") 


class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('dob','address','phone')


class DoctorSignupForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('phone','specialty','availability')
