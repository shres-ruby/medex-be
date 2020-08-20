from django.urls import path,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (UserListView, UserDetailView, PatientListView, 
DoctorListView, PatientSignupAPI)


r = DefaultRouter()
r.register('allusers', UserListView)
r.register('patients', PatientListView)
r.register('doctors', DoctorListView)

urlpatterns=[
    path('login/', obtain_auth_token),
    path('patientsignup/', PatientSignupAPI.as_view())
] + r.urls