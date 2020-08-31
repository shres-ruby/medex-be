from django.urls import path,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (UserListView, UserDetailView, PatientListView, 
DoctorListView, PrescriptionView, PatientSignupAPI, DoctorSignupAPI,
ProfileView, ProfileDetailView, EditProfile)


r = DefaultRouter()
r.register('allusers', UserListView)
r.register('patients', PatientListView)
r.register('doctors', DoctorListView)
r.register('prescriptions', PrescriptionView)
r.register('profile', ProfileView)

urlpatterns=[
    path('login/', obtain_auth_token),
    path('patientsignup/', PatientSignupAPI.as_view()),
    path('doctorsignup/', DoctorSignupAPI.as_view()),
    path('profile/<str:user__user__email>/', ProfileDetailView.as_view({'get':'retrieve', 'put':'update'})),
    path('edit/', EditProfile.as_view())
] + r.urls