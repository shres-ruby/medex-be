from django.shortcuts import render
from django.views.generic import CreateView

from users.models import CustomUser, Patient, Doctor
from users.forms import PatientSignupForm, DoctorSignupForm

class patient_signup_view(CreateView):
    model = CustomUser
    form_class = PatientSignupForm
    template_name = 'users/patient_profile.html'

class doctor_signup_view(CreateView):
    model = CustomUser
    form_class =  DoctorSignupForm
    template_name = 'users/doctor_profile.html'