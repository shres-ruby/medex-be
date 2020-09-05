from django.urls import path,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (UserListView, UserDetailView, PatientListView, 
DoctorListView, PrescriptionView, PatientSignupAPI, DoctorSignupAPI,
ProfileView, ProfileDetailView, AppointmentView)


r = DefaultRouter()
r.register('allusers', UserListView)
r.register('patients', PatientListView)
r.register('doctors', DoctorListView)
r.register('prescriptions', PrescriptionView)
r.register('profile', ProfileView, basename='profile')
r.register('appointments', AppointmentView)

urlpatterns=[
    path('login/', obtain_auth_token),
    path('patientsignup/', PatientSignupAPI.as_view()),
    path('doctorsignup/', DoctorSignupAPI.as_view()),
    path('profile/<str:user__email>/', ProfileDetailView.as_view({'get':'retrieve', 'put':'update'})),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] + r.urls