from django.urls import path

from users.views import patient_signup_view, doctor_signup_view


urlpatterns = [
    path('signup/patient/', patient_signup_view.as_view()),
    path('signup/doctor/', doctor_signup_view.as_view())
    ]   
