from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import CustomUser, Patient, Doctor


class PatientSignupForm(UserCreationForm):
    
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','first_name','last_name','password1','password2')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient =  True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.first_name = self.cleaned_data.get('first_name')
        patient.last_name = self.cleaned_data.get('last_name')
        patient.dob = self.cleaned_data.get('dob')
        patient.address = self.cleaned_data.get('address')
        patient.phone = self.cleaned_data.get('phone')
        patient.save()
        return user


class DoctorSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    specialty = forms.CharField(required=True)
    availability = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','first_name','last_name','password1','password2')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name = self.cleaned_data.get('first_name')
        doctor.last_name = self.cleaned_data.get('last_name')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.specialty = self.cleaned_data.get('specialty')
        doctor.availability = self.cleaned_data.get('availability')
        doctor.save()
        return user