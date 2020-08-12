from django.shortcuts import render

from users.models import CustomUser
from users.forms import UserForm, PatientSignupForm, DoctorSignupForm


def patient_signup_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = PatientSignupForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            
            user.patient_profile.dob = profile_form.cleaned_data.get('dob')
            user.patient_profile.address = profile_form.cleaned_data.get('address')
            user.patient_profile.save()

    else:
        user_form = UserForm
        profile_form = PatientSignupForm
        
    return render(request, 'users/patient_profile.html', {
        'user_form' : user_form,
        'profile_form' : profile_form
        })

def doctor_signup_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = DoctorSignupForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            user.doctor_profile.specialty = profile_form.cleaned_data.get('specialty')
            user.doctor_profile.availability = profile_form.cleaned_data.get('availability')
            user.patient_profile.save()

    else:
        user_form = UserForm
        profile_form = DoctorSignupForm
        
    return render(request, 'users/doctor_profile.html', {
        'user_form' : user_form,
        'profile_form' : profile_form
        })
